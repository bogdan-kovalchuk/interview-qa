---
id: py-modimp-0007
title: "Чому relative import може не спрацювати під час запуску package module як звичайного script file?"
track: python
section: modules-and-imports
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
  - source_id: py314-reference-import-special-main
    title: "Python 3.14: Reference/import (Special considerations for __main__)"
    url: https://docs.python.org/3.14/reference/import.html#special-considerations-for-main
  - source_id: py314-reference-datamodel-module-package
    title: "Python 3.14: Reference/datamodel (module.__package__)"
    url: https://docs.python.org/3.14/reference/datamodel.html#module.__package__
  - source_id: py314-reference-import-package-relative-imports
    title: "Python 3.14: Reference/import (Package Relative Imports)"
    url: https://docs.python.org/3.14/reference/import.html#package-relative-imports
  - source_id: py315-whatsnew-other-language-changes
    title: "Python 3.15: What's New (Other language changes)"
    url: https://docs.python.org/3.15/whatsnew/3.15.html#other-language-changes
---

## Short answer

**При запуску `python package/module.py` модуль отримує `__name__ = '__main__'` і `__spec__ = None`, тому relative import не знає свого пакета й викликає ImportError.**[^py314-reference-import-special-main] Import system визначає пакет через `__spec__.parent`; `__package__` є лише запасним варіантом, який застарів із 3.13.[^py314-reference-datamodel-module-package] What’s New для 3.15 досі називає його застарілим і запланованим до вилучення.[^py315-whatsnew-other-language-changes] Найпростіший правильний спосіб – `python -m package.module` з кореня проєкту: тоді `__spec__` встановлюється автоматично.[^py314-reference-import-special-main]

## Detailed explanation

Відносний import починається з крапки і стартує від поточного пакета: одна крапка означає поточний пакет, кожна наступна – ще один рівень вгору.[^py314-reference-import-package-relative-imports] Щоб знайти цей пакет, import system використовує `__spec__.parent`, тобто ім’я пакета зі spec модуля. `__package__` раніше виконував ту саму роль; з Python 3.13 його позначено як застарілий.[^py314-reference-datamodel-module-package] What’s New для 3.15 повторює, що його заплановано до вилучення.[^py315-whatsnew-other-language-changes]

Коли Python запускає файл напряму, він виконує його як `__main__` без імпорту як модуля: `__spec__` дорівнює `None`, тож пакета немає, і відносному import не на що спертися.[^py314-reference-import-special-main] Коли Python запускає `python -m package.module`, модуль знаходиться через import system, і `__spec__` містить spec з ім’ям `package.module`.[^py314-reference-import-special-main] В обох випадках `__name__` дорівнює `'__main__'`, тому саме це ім’я не показує, чи є пакет.

Ілюстративний файл, який падає при прямому запуску (виведення перевірено на 3.12, 3.13 і 3.14):

```python
# pkg/module.py (illustrative)
print(__name__, __package__, __spec__)
# python pkg/module.py    -> __main__ None None, then ImportError
# python -m pkg.module    -> __main__ pkg ModuleSpec(name='pkg.module', ...)
from . import sibling
```

Є два типові виправлення. Перше – запускати з кореня проєкту через `-m`. Друге – залишити модуль частиною пакета, а запускати окремий скрипт у корені, який імпортує його як `pkg.module`: тоді відносні import працюють, бо модуль завантажено штатно.

**Типові помилки:**
- вважати, що `__name__ == '__main__'` означає відсутність пакета: при `python -m` ім’я теж `__main__`, але `__spec__` і пакет є;
- писати новий код з `__package__`, хоча import system віддає перевагу `__spec__.parent`, а `__package__` застарілий і запланований до вилучення;
- додавати хак із `sys.path`, щоб обійти помилку, замість запуску через `-m` з кореня проєкту.
