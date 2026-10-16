---
id: py-pkgenv-0001
title: "У чому різниця між requirements.txt і pyproject.toml для управління залежностями Python-проєкту?"
track: python
section: packaging-and-environments
sources:
  - source_id: pep621
    title: "PEP 621: Storing project metadata in pyproject.toml"
    url: https://peps.python.org/pep-0621/
  - source_id: packaging-guide
    title: "Python Packaging User Guide: Writing pyproject.toml"
    url: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
  - source_id: pip-requirements-format
    title: "pip documentation: Requirements File Format"
    url: https://pip.pypa.io/en/stable/reference/requirements-file-format/
  - source_id: packaging-install-requires-vs-requirements
    title: "Python Packaging User Guide: install_requires vs requirements files"
    url: https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/#install-requires-vs-requirements-files
---

## Short answer

**`pyproject.toml` є стандартизованою конфігурацією: `[build-system]` обирає build backend, а `[project].dependencies` оголошує вимоги для інсталяції, які стають метаданими distribution.**[^pep621][^packaging-guide] Файл `requirements.txt` зазвичай є вхідними даними pip для інсталяції середовища та може містити pins, hashes, indexes, URLs, constraints й includes; ні назва файла, ні фіксація версій не є обов’язковими.[^pip-requirements-format] Тому ці файли доповнюють, а не замінюють один одного: `pyproject.toml` описує проєкт і підтримувані діапазони залежностей, а для відтворюваного середовища зазвичай використовують lock file або повністю pinned requirements.

## Detailed explanation

`pyproject.toml` – стандартний файл із таблицями для збірки та для метаданих проєкту. Таблиця `[build-system]` вказує build backend і пакети для збірки.[^packaging-guide] Таблиця `[project]` визначена PEP 621: поля `name`, `version` і `dependencies` стандартизовані, а кожен рядок у `dependencies` має бути PEP 508-вимогою. Такий рядок стає записом `Requires-Dist` у core metadata збудованого distribution.[^pep621] Тому, коли хтось встановлює проєкт із wheel або sdist, pip бере залежності з цих метаданих автоматично.[^packaging-install-requires-vs-requirements]

`requirements.txt` має інший статус. Це список аргументів для `pip install`: кожен рядок є вимогою, опцією або посиланням на інший файл. Pip читає такий файл лише тоді, коли його передають через `-r` (наприклад, `pip install -r` або `pip download -r`), а не під час встановлення проєкту з його метаданих.[^packaging-install-requires-vs-requirements] Формат дозволяє точні pins, `--hash`, `--index-url`, `-r` для вкладених файлів і `-c` для constraints.[^pip-requirements-format] Водночас звичайний рядок без версії, наприклад `pytest`, також є допустимим, тож закріплення версій у цьому форматі не є обов’язковим.[^pip-requirements-format]

Типова розбіжність видна в прикладі. Бібліотека оголошує діапазон у `pyproject.toml`, а конкретна збірка середовища фіксує версію в `requirements.txt`:

```toml
# pyproject.toml: the project declares a range it supports
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "demo-app"
version = "0.1.0"
dependencies = ["httpx>=0.27,<1"]   # any httpx from 0.27 up to, not including, 1.0
```

```text
# requirements.txt: exact versions for one tested environment
httpx==0.28.1
```

Реальний requirements-файл зазвичай містить повний перелік закріплених версій, включно з транзитивними залежностями httpx, яких у прикладі немає. Саме так досягається повторюване встановлення.[^packaging-install-requires-vs-requirements] Для самої бібліотеки, навпаки, рекомендовано вказувати діапазон із мінімальною і, за потреби, верхньою межею. Точний pin у `dependencies` змушує споживачів відмовлятися від оновлень, тому це не вважають хорошою практикою.[^packaging-install-requires-vs-requirements]

**Типові помилки:**
- ставити точні версії в `[project].dependencies`, через що споживачі бібліотеки не можуть оновити залежність;
- вважати, що `requirements.txt` є частиною метаданих збірки: інсталятор проєкту його не читає;
- вважати, що ім’я файла має значення: pip приймає будь-яку назву в `-r`, бо `requirements.txt` є лише звичним іменем.[^pip-requirements-format]
