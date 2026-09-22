---
id: py-objtypes-0017
title: "Чим `str` відрізняється від `bytes` і на якій межі програми має відбуватися encode/decode?"
description: "str – незмінна послідовність Unicode code point (текст), bytes – незмінна послідовність 8-бітних значень (двійкові дані); вони не сумісні напряму і потребують явного encode/decode."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [str, bytes]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
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

**`str` – незмінна послідовність Unicode code point (текст), `bytes` – незмінна послідовність 8-бітних значень (двійкові дані); вони не сумісні напряму і потребують явного encode/decode.**[^py314-reference-datamodel] Encode/decode має відбуватися на межі програми: decode при читанні зовнішніх даних (файли, мережа, CLI) у внутрішній `str`, encode при записі `str` назовні. <span class="warn">Змішування `str` і `bytes` в операціях викликає `TypeError`, а неявне кодування всередині програми призводить до помилок при зміні encoding.</span>

## Detailed explanation

`str` представляє людиночитний текст як незмінну послідовність абстрактних Unicode code points (символів), тоді як `bytes` представляє сирі двійкові дані як незмінну послідовність цілих чисел у діапазоні 0–255.[^py314-reference-datamodel]

У Python 3 текстові та двійкові дані повністю розділені на рівні типів. Об'єкт `str` не має фіксованого представлення у байтах, доступного з Python-коду: він абстрагує деталі збереження в пам'яті (внутрішньо CPython використовує гнучке представлення згідно з PEP 393). На противагу цьому, `bytes` оперує фізичними октетами, призначеними для передачі мережею або запису на диск. Оскільки абстрактні символи та двійкові послідовності семантично несумісні, Python забороняє будь-яке неявне приведення між ними: конкатенація `str` з `bytes` або операції порівняння порядку викликають `TypeError` (а перевірка рівності `str == bytes` завжди повертає `False`).[^py314-library-stdtypes]

Архітектурний підхід для обробки цих відмінностей відомий як «Unicode sandwich». На зовнішніх межах програми (файлові операції, мережеві сокети, бази даних, CLI) отримані сирі `bytes` негайно декодуються у `str` із явним зазначенням кодування (зазвичай UTF-8). Уся внутрішня бізнес-логіка оперує виключно текстом `str` без прив'язки до байтових деталей. На виході з програми текстові дані знову явно кодуються у `bytes` для передачі зовнішнім споживачам.

Приклад явного перетворення на межі програми та несумісності типів:

```python
# Raw binary data received from external source (network or disk)
raw_bytes = b"Hello, world!"

# Decode at input boundary into Unicode text
text = raw_bytes.decode("utf-8")
print(text)  # Hello, world!
print(type(text), len(text))  # <class 'str'> 13

# Direct operations between str and bytes are forbidden
try:
    _ = text + b"!"
except TypeError as err:
    print(type(err).__name__)  # TypeError

# Multi-byte characters show the difference between character count and byte length
euro = "\u20ac"  # Euro symbol: '€'
euro_bytes = euro.encode("utf-8")
print(len(euro), len(euro_bytes))  # 1 3
```

**Типові помилки при роботі зі `str` та `bytes`:**
- виконання decode або encode всередині бізнес-логіки замість межі програми, що розмиває відповідальність і призводить до дублювання перетворень;
- припущення, що `len(s)` для `str` дорівнює розміру даних у байтах, що ламає роботу з протоколами, де потрібен заголовок `Content-Length`;
- ігнорування параметра кодування (виклик `.encode()` або `.decode()` без аргументу), через що поведінка залежить від системної локалі замість стандартизованого UTF-8;
- спроба відкрити бінарний файл у текстовому режимі без вказання `mode='rb'`, що призводить до спотворення переносів рядків (`\r\n` на Windows) або винятків `UnicodeDecodeError`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
