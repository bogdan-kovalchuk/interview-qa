---
id: py-modimp-0014
title: "Чим import package/module відрізняється від installable distribution project з build metadata?"
description: "Import package/module – це runtime-концепція: директорія з __init__.py або окремий .py-файл, який import system знаходить і завантажує."
track: python
section: modules-and-imports
level: middle
type: comparison
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційний посібник із packaging для Python."
  - source_id: py314-reference-import-regular-packages
    title: "Python 3.14: Reference/import, Regular packages"
    url: https://docs.python.org/3.14/reference/import.html#regular-packages
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: regular package зазвичай є директорією з __init__.py."
  - source_id: py314-reference-import-namespace-packages
    title: "Python 3.14: Reference/import, Namespace packages"
    url: https://docs.python.org/3.14/reference/import.html#namespace-packages
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: namespace package не має файлу __init__.py."
  - source_id: packaging-distribution-package-vs-import-package
    title: "Python Packaging User Guide: Distribution package vs. import package"
    url: https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package/#distribution-package-vs-import-package
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Офіційна сторінка PyPA: distribution package – це те, що встановлює pip, зазвичай синонім project; одна distribution може надавати кілька import packages, а імена не зобов’язані збігатися."
---

## Short answer

**Import package або module – це runtime-концепція: модуль, який import system знаходить і завантажує, зазвичай директорія з `__init__.py` або окремий `.py`-файл.**[^py314-reference-import-regular-packages] Distribution project – це packaging-концепція: source tree, зазвичай з `pyproject.toml`, де описано metadata (name, version, dependencies), а build backend створює з нього installable archive, наприклад wheel.[^py-packaging-guide] Одна distribution може надавати кілька import packages, а `pip install` ставить distribution, а не import package.[^packaging-distribution-package-vs-import-package]

## Detailed explanation

Import package і module належать до import system, тобто до того, як Python знаходить код під час `import`. Import package – це особливий вид модуля, який може містити підмодулі.[^packaging-distribution-package-vs-import-package] Зазвичай пакет – це директорія з `__init__.py`, але є і namespace packages, які не мають `__init__.py`.[^py314-reference-import-namespace-packages] Ім’я після `import` – це import name. Саме воно шукається під час виконання, незалежно від того, яким дистрибутивом пакет було встановлено.

Distribution – це те, що встановлює `pip`. Packaging-документація називає distribution package програмним забезпеченням, яке можна встановити; на практиці слово «project» здебільшого означає те саме.[^packaging-distribution-package-vs-import-package] Вихідний код проєкту описує метадані (`name`, `version`, `dependencies`) у `pyproject.toml`. Build backend читає конфігурацію проєкту і збирає з вихідних файлів distribution package, наприклад wheel.[^py-packaging-guide]

Зв’язок між іменами є домовленістю, а не правилом. Індекс на кшталт PyPI вимагає унікальності distribution names, але не прив’язує їх до import names. Тому можливі три ситуації: distribution `Pillow` надає import package `PIL`; distribution `attrs` надає два import packages, `attrs` і `attr`; і кілька distribution можуть надавати один і той самий import name, наприклад через форки.[^packaging-distribution-package-vs-import-package] Звідси й обережність: ім’я з PyPI не гарантує, що `import` з таким самим ім’ям принесе очікуваний пакет.

Приклад після `pip install pillow`: distribution називається `pillow`, а import name – `PIL`.

```python
import PIL                     # import name: the package directory PIL/
from PIL import Image          # a module inside the import package

try:
    import pillow              # the distribution name is not an import name
except ModuleNotFoundError as error:
    print(error)               # No module named 'pillow'
```

**Типові помилки:**
- вважати, що `pip install X` дає import package з ім’ям `X` (для Pillow це `PIL`);
- шукати модуль за назвою дистрибутива, а не за import name;
- вважати, що `name` у `pyproject.toml` створює import package: імена не зобов’язані збігатися.[^packaging-distribution-package-vs-import-package]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
