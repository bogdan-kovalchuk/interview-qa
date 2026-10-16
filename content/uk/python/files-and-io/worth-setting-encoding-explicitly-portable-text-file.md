---
id: py-fileio-0002
title: "Чому для переносного text file варто задавати `encoding` явно, а не покладатися на platform default?"
track: python
section: files-and-io
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
  - source_id: py314-library-locale
    title: "Python 3.14: Library/locale"
    url: https://docs.python.org/3.14/library/locale.html#locale.getencoding
  - source_id: pep-0686
    title: "PEP 686: Make UTF-8 mode default"
    url: https://peps.python.org/pep-0686/
---

## Short answer

**Типове кодування визначає locale: на Windows `locale.getencoding()` повертає ANSI code page, а на більшості Unix-систем – `utf-8`.**[^py314-library-locale][^py314-library-io] Файл, записаний без явного `encoding`, може стати нечитабельним на іншій машині.[^py314-library-io] Явне `encoding="utf-8"` не залежить від locale. З Python 3.15 UTF-8 Mode є типовим,[^pep-0686] а в 3.14 і раніше типове значення залежить від locale, якщо UTF-8 Mode не ввімкнено.[^py314-library-io]

## Detailed explanation

Текстовий шар без параметра `encoding` бере кодування з locale. `locale.getencoding()` на Windows повертає ANSI code page, а на Unix – кодування локалі. Він ігнорує UTF-8 Mode: `locale.getpreferredencoding(False)` цей режим враховує, а `locale.getencoding()` ні.[^py314-library-locale] Наприклад, із `LC_ALL=POSIX` і `-X utf8` (перевірено на 3.12, 3.13 і 3.14) `locale.getencoding()` дає `ANSI_X3.4-1968`, тоді як `open()` використовує `utf-8`, бо в UTF-8 Mode це його типове значення.[^py314-library-io] Через це один і той самий код може писати й читати різні байти на різних машинах. Документація Python прямо називає це джерелом помилок: більшість Unix-платформ використовує UTF-8 локаль, тоді як для більшості користувачів Windows локальне кодування не UTF-8.[^py314-library-io]

Явний параметр варто задавати і при записі, і при читанні, тоді обидві сторони використовують один кодек:

```python
import locale
from pathlib import Path

Path("notes.txt").write_text("Привіт, світе\n", encoding="utf-8")   # explicit encoding: the codec does not depend on the locale
print(Path("notes.txt").read_text(encoding="utf-8"))                 # Привіт, світе
print(locale.getencoding())   # UTF-8 in this Linux run; the ANSI code page (often cp1252) on Windows
```

`Path.read_text()` без `encoding` працює так само, як `open()`: бере те саме locale-кодування.[^py314-library-pathlib][^py314-library-io] Вивід `locale.getencoding()` залежить від машини, тому його не варто вважати сталим значенням у тестах.

Помилка часто тиха. Байти, записані в одному кодуванні, інше може прочитати без винятку й отримати інший текст, тож тест на машині розробника може пройти, а на іншій – дати сміття. Щоб знайти місця, де програма покладається на типове кодування, запустіть її з `-X warn_default_encoding`: тоді `open()` без `encoding` видає `EncodingWarning`.[^py314-library-io] Якщо locale-кодування справді потрібне, пишіть `encoding="locale"` (його підтримано з Python 3.10), щоб намір був видно в коді.[^py314-library-io]

З Python 3.15 UTF-8 Mode є типовим (PEP 686),[^pep-0686] але код, який має працювати на 3.14 або раніше, все одно потребує явного `encoding`.[^py314-library-io] UTF-8 Mode, увімкнений на рівні процесу, змінює типове значення для всіх файлів програми; явний `encoding` у місці відкриття файлу видно в коді й не залежить від налаштувань запуску.

**Типові помилки:**
- тестувати лише на Linux з UTF-8 локаллю і вважати код переносним;
- вказати `encoding` тільки для читання або тільки для запису;
- вважати, що UTF-8 за замовчуванням у 3.15 знімає потребу в `encoding` у коді, який має працювати на 3.14 або раніше.
