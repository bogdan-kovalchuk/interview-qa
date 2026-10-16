---
id: py-perf-0008
title: "Чому repeated string concatenation у loop може спричиняти repeated copying і коли доречніше accumulated fragments зібрати через `\"\".join(...)`?"
track: python
section: performance
sources:
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
  - source_id: py314-library-stdtypes-repeated-concatenation
    title: "Python 3.14: Library/stdtypes, repeated concatenation"
    url: https://docs.python.org/3.14/library/stdtypes.html#typesseq-repeated-concatenation
  - source_id: cpython-bytecodes-inplace-add-unicode
    title: "CPython 3.14: Python/bytecodes.c"
    url: https://github.com/python/cpython/blob/v3.14.6/Python/bytecodes.c
  - source_id: cpython-unicodeobject-joinarray
    title: "CPython 3.14: Objects/unicodeobject.c"
    url: https://github.com/python/cpython/blob/v3.14.6/Objects/unicodeobject.c
---

## Short answer

**Оскільки `str` незмінний, конкатенація створює новий рядок, тож накопичення через повторне `+=` має квадратичну вартість за загальною довжиною.**[^py314-library-stdtypes-repeated-concatenation] Для багатьох фрагментів рекомендують складати їх у `list` і викликати `''.join(...)` один раз; `io.StringIO` теж є ефективним варіантом.[^py314-faq-programming-performance] CPython іноді розширює рядок на місці, але на це не варто покладатися.

## Detailed explanation

Рядок незмінний: `a + b` не змінює ні `a`, ні `b`, а створює новий об’єкт довжиною `len(a) + len(b)` і копіює в нього вміст обох рядків. Якщо в циклі до накопичувача додають фрагменти по `m` символів, то на `k`-му кроці копіюється `k*m` символів, а разом – `m*n*(n+1)/2` для `n` кроків. Звідси квадратична залежність від загальної довжини, яку документація описує прямо.[^py314-library-stdtypes-repeated-concatenation]

У CPython є виняток. Для `s += t` з локальною змінною інтерпретатор може розширити рядок на місці, якщо рядок більше ніде не посилається. Умову видно у вихідному коді: наступна інструкція має бути `STORE_FAST` у ту саму змінну.[^cpython-bytecodes-inplace-add-unicode] Атрибут `self.text += part` такого шляху не має, тому кожен виклик копіює весь текст. Приклад нижче порівнює варіант з атрибутом із `join`:

```python
import timeit

class Report:
    def __init__(self):
        self.text = ''

    def add(self, part):
        self.text += part          # attribute target: CPython does not extend it in place

def build_attr(parts):
    report = Report()
    for part in parts:
        report.add(part)
    return report.text

def build_join(parts):
    chunks = []
    for part in parts:
        chunks.append(part)
    return ''.join(chunks)         # one pass for the total length, then one copy per fragment

parts = ['x' * 10] * 20_000
print(build_attr(parts) == build_join(parts))   # True
slow = timeit.timeit(lambda: build_attr(parts), number=1)
fast = timeit.timeit(lambda: build_join(parts), number=1)
print(slow > 10 * fast)            # True on CPython 3.13 and 3.14
```

`str.join` працює інакше: CPython спочатку проходить по фрагментах і обчислює загальну довжину, потім одним виділенням створює результат і копіює кожен фрагмент один раз.[^cpython-unicodeobject-joinarray] Тому список із подальшим `join` доцільний, коли фрагментів багато і вони з’являються в циклі. Якщо текст однаково записується у файл, краще писати потоково у файл або в `io.StringIO`.

Для кількох конкатенацій без циклу `+` або f-рядок цілком прийнятні: це одна операція, і її вартість не росте з обсягом даних. Квадратичний ефект з’являється, коли кількість кроків росте разом із даними. Для `bytes` документація дає ті самі альтернативи: `bytes.join`, `io.BytesIO` або `bytearray`.[^py314-library-stdtypes-repeated-concatenation]

**Типові помилки:**
- вважати, що оптимізація `+=` в CPython діє завжди, і переносити цикл на атрибут або на змінну з іншими посиланнями;
- викликати `join` усередині циклу або для кожного фрагмента окремо, що знімає сенс збирання;
- накопичувати у `list` увесь великий вихід, коли його можна писати потоково.
