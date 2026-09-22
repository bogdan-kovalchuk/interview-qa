---
id: py-objtypes-0019
title: "Яку проблему копіювання вирішує `memoryview` і чому lifetime базового buffer object має значення?"
description: "memoryview надає zero-copy доступ до внутрішнього buffer об'єкта, що підтримує buffer protocol (наприклад, bytes, bytearray, array.array), дозволяючи читати та змінювати ділянки пам'яті без створення копій."
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [memoryview]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L498-L586
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`memoryview` надає zero-copy доступ до внутрішнього buffer об'єкта, що підтримує buffer protocol (наприклад, `bytes`, `bytearray`, `array.array`), дозволяючи читати та змінювати ділянки пам'яті без створення копій.**[^py314-reference-datamodel] Це критично для великих binary даних, де slicing або `copy` створили б повну копію. Lifetime базового об'єкта має значення: `memoryview` не володіє даними, а посилається на buffer; у CPython memoryview тримає reference на base-об'єкт, запобігаючи його звільненню, а поки буфер експортований, спроба змінити розмір base (наприклад, `bytearray.extend()`) піднімає `BufferError` – спочатку треба викликати `release()`. <span class="warn">Після виклику `mv.release()` доступ до memoryview викликає `ValueError`.</span>

## Detailed explanation

`memoryview` дозволяє Python-коду ділитися та робити зрізи неперервних буферів пам'яті між різними об'єктами без копіювання даних, реалізуючи низькорівневий C buffer protocol на рівні мови.[^py314-reference-datamodel]

У звичайному Python операція взяття зрізу (наприклад, `b[10:100]`) виділяє новий об'єкт і повністю копіює туди 90 байтів. При роботі з великими двійковими даними (мережеві пакети у високонавантажених сокетах, обробка відеокадрів, масиви `numpy`) багаторазове копіювання фрагментів призводить до фрагментації пам'яті та значних накладних витрат $O(N)$ CPU. Натомість взяття зрізу від `memoryview` повертає новий екземпляр `memoryview`, який посилається на піддіапазон того самого буфера пам'яті через вказівник, довжину та крок (stride) без жодного копіювання даних ($O(1)$ за часом і пам'яттю). Якщо базовий буфер мутабельний (як `bytearray`), зміни через зріз миттєво змінюють оригінальний об'єкт.

Час життя (lifetime) та стан базового об'єкта мають вирішальне значення, оскільки `memoryview` не володіє пам'яттю, а лише посилається на неї. На рівні C-API створення `memoryview` експортує буфер через функцію `PyObject_GetBuffer()`, збільшуючи лічильник активних експортів (`bf_getbuffer`). У CPython це забезпечує два ключові інваріанти:
По-перше, збирач сміття (GC) не може передчасно звільнити пам'ять базового об'єкта, оскільки атрибут `memoryview.obj` утримує на нього сильне посилання (strong reference).
По-друге, щоб уникнути висячих вказівників (dangling pointers) та пошкодження пам'яті, базовий об'єкт блокує зміну розміру свого внутрішнього буфера: будь-яка операція, що вимагає реаллокації пам'яті (наприклад, `bytearray.extend()` чи `.append()`), піднімає виняток `BufferError`.[^py314-library-stdtypes]

Щоб зняти це блокування до спрацювання збирача сміття, розробник може явно викликати `mv.release()` або застосувати контекстний менеджер (`with memoryview(...) as mv:`). Після виклику `release()` об'єкт `memoryview` від'єднується від базового буфера, що дозволяє базовому об'єкту вільно змінювати розмір, проте будь-яке подальше читання чи запис через звільнений view призводить до винятку `ValueError`.

Демонстрація zero-copy зрізів, мутації через view та блокування зміни розміру буфера:

```python
# Underlying mutable buffer
data = bytearray(b"abcdefghij")

# Create a zero-copy memoryview and slice it
view = memoryview(data)
sub_view = view[3:7]  # zero-copy slice: references bytes 3..6 without copying
print(bytes(sub_view))  # b'defg'

# Mutating through sub_view directly modifies the underlying bytearray
sub_view[0] = ord("D")
print(data)  # bytearray(b'abcDefghij')

# Underlying buffer cannot change size while exported
try:
    data.extend(b"klm")
except BufferError as err:
    print(type(err).__name__)  # BufferError (Existing exports of data)

# Releasing the view releases the lock on the base object
sub_view.release()
view.release()
data.extend(b"klm")  # now resizing succeeds
print(len(data))  # 13

# Accessing a released view raises ValueError
try:
    _ = view[0]
except ValueError as err:
    print(type(err).__name__)  # ValueError (operation forbidden on released memoryview)
```

**Практичні наслідки та типові пастки при роботі з `memoryview`:**
- блокування зміни розміру: утримання активного `memoryview` на `bytearray` блокує будь-які методи, що перерозподіляють пам'ять (`extend`, `pop`, `resize`), викликаючи неочікувані `BufferError` в інших частинах коду;
- витік пам'яті через збереження посилання: оскільки `memoryview` тримає сильне посилання на весь базовий об'єкт, навіть крихітний зріз `mv[0:10]` не дасть GC звільнити гігабайтний буфер, доки живий цей `memoryview`;
- керування ресурсами: використання контекстного менеджера (`with memoryview(...) as mv:`) або явного `mv.release()` гарантує своєчасне звільнення експорту буфера;
- помилки доступу після звільнення: будь-яка спроба прочитати або змінити буфер через уже закритий `memoryview` генерує `ValueError`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
