---
id: py-fileio-0013
title: "Чому `pickle.loads()` не можна викликати для untrusted data навіть після перевірки expected object type?"
description: "Код може виконатися під час самого unpickling, до того як результат існує, тож перевірити тип отриманого об’єкта вже пізно."
track: python
section: files-and-io
level: senior
type: pitfall
tags: [pickle-loads]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-pickle-restricting-globals
    title: "Python 3.14: Library/pickle (Restricting Globals)"
    url: https://docs.python.org/3.14/library/pickle.html#pickle-restrict
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: за замовчуванням unpickling імпортує будь-який клас або функцію з даних, що дає змогу викликати довільний код."
  - source_id: py314-library-pickle-object-reduce
    title: "Python 3.14: Library/pickle (object.__reduce__)"
    url: https://docs.python.org/3.14/library/pickle.html#object.__reduce__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: __reduce__ повертає callable і кортеж аргументів, який викликається, щоб створити об’єкт під час відновлення."
  - source_id: py314-library-pickle-find-class
    title: "Python 3.14: Library/pickle (Unpickler.find_class)"
    url: https://docs.python.org/3.14/library/pickle.html#pickle.Unpickler.find_class
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: find_class викликається щоразу, коли запитується клас або функція; його перевизначення може зменшити ризики безпеки."
---

## Short answer

**`pickle.loads()` може виконати довільний код під час відновлення об’єкта, тож перевірка type результату вже запізнилася.**[^py314-library-pickle] Pickle-потік може імпортувати будь-яку функцію чи клас і викликати його з аргументами, наприклад `os.system`, а клас може сам вказати такий виклик через `__reduce__`.[^py314-library-pickle-restricting-globals][^py314-library-pickle-object-reduce] Обмеження через `find_class` може лише зменшити ризик, але не робить pickle безпечним для недовірених даних.[^py314-library-pickle-find-class][^py314-library-pickle] Для таких даних безпечніше взяти `json` або інший формат без виконання коду.[^py314-library-pickle]

## Detailed explanation

Unpickler не лише читає дані, а й виконує інструкції, які містить pickle-потік. Документація прямо попереджає, що pickle небезпечний: зловмисник може підготувати дані, які виконують довільний код під час unpickling, тож дані з ненадійного джерела або такі, що могли бути підмінені, розпаковувати не можна.[^py314-library-pickle] За замовчуванням unpickling імпортує будь-який клас або функцію, знайдені в даних, і це дозволяє викликати довільний код.[^py314-library-pickle-restricting-globals] Клас може сам задати такий виклик через `__reduce__`: метод повертає callable і кортеж аргументів, які unpickler викликає, щоб створити об’єкт.[^py314-library-pickle-object-reduce]

Приклад безпечний, бо замість `os.system` викликає `print`, але механізм той самий: виклик відбувається всередині `loads()`, і перевірка результату його вже не скасує.

```python
import pickle

class Payload:
    def __reduce__(self):
        # loads() calls print(...) while it rebuilds the object
        return (print, ("side effect during pickle.loads",))

untrusted = pickle.dumps(Payload())

obj = pickle.loads(untrusted)  # the side effect happens here, before loads() returns
print(type(obj))               # <class 'NoneType'>
print(isinstance(obj, dict))   # False: a check like this rejects the value, too late
```

`Unpickler.find_class()` викликається щоразу, коли потрібен глобальний клас або функція, тож його можна перевизначити та заборонити або звузити набір дозволених імен.[^py314-library-pickle-find-class] Але дозволена функція виконується з усіма своїми можливостями: якщо серед дозволених є щось, що читає файли або запускає процеси, такий список цього не зупинить. Обмеження зменшує поверхню атаки, але не перетворює unpickling на безпечну операцію для недовірених даних.[^py314-library-pickle]

Якщо дані надходять ззовні, використовуйте формат без виконання коду, наприклад `json`, і перевіряйте схему після розбору. Якщо pickle лишається потрібним між власними сервісами, автентифікуйте дані до виклику `loads()`: документація радить підписувати їх через `hmac`, щоб переконатися, що їх не підмінили.[^py314-library-pickle] Перевірка підпису має відбутися до будь-якого виклику `loads()`, інакше шкідливий потік уже виконався б.

**Типові помилки:**
- вважати, що `isinstance`-перевірка після `loads()` захищає від виконання коду;
- вважати, що allow-list у `find_class` робить pickle безпечним для недовірених даних;
- приймати pickle зі спільного кешу, черги чи каталогу, куди може писати інша сторона.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
