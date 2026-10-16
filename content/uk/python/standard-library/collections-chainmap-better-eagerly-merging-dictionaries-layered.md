---
id: py-stdlib-0001
title: "Коли `collections.ChainMap` кращий за eager merge dictionaries для layered configuration з precedence між command line, environment і defaults?"
track: python
section: standard-library
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
  - source_id: py314-library-collections-chainmap
    title: "Python 3.14: Library/collections (ChainMap)"
    url: https://docs.python.org/3.14/library/collections.html#collections.ChainMap
  - source_id: py314-library-collections-chainmap-maps
    title: "Python 3.14: Library/collections (ChainMap.maps)"
    url: https://docs.python.org/3.14/library/collections.html#collections.ChainMap.maps
---

## Short answer

**`ChainMap` шукає ключі послідовно в mappings від першого до останнього і не створює merged dict, тому зміни в нижніх шарах видно без повторного merge.**[^py314-library-collections-chainmap] Порядок пошуку задає порядок аргументів: у `ChainMap(cli, env, defaults)` спершу перевіряється CLI.[^py314-library-collections-chainmap-maps] Запис, оновлення й видалення стосуються лише першого mapping.[^py314-library-collections-chainmap] Він корисний для layered config, де шари оновлюються незалежно, бо повторний merge після кожної зміни не потрібен.

## Detailed explanation

Eager merge (`{**defaults, **env, **cli}` або цикл із `update()`) копіює ключі в новий dict у момент злиття. Далі результат є знімком: зміна `defaults` чи `env` після цього в нього не потрапляє. `ChainMap` натомість зберігає посилання на вихідні mappings і шукає значення в них під час кожного доступу, тому оновлення шарів видно одразу.[^py314-library-collections-chainmap]

Приклад: CLI має найвищий пріоритет, далі env, далі defaults. Коментарі показують, що бачить `ChainMap`, а що лишається знімком.

```python
from collections import ChainMap

defaults = {"host": "localhost", "port": 8000, "debug": False}
env = {"port": 9000}
cli = {"debug": True}

config = ChainMap(cli, env, defaults)  # first mapping has the highest priority
print(config["port"])                  # 9000, found in env
env["host"] = "example.org"
print(config["host"])                  # example.org, the change is visible at once

merged = {**defaults, **env, **cli}    # eager merge: a snapshot
defaults["timeout"] = 30
print(config["timeout"])               # 30, the lower layer change is visible
print(merged.get("timeout"))           # None, the snapshot does not see it

config["port"] = 7000                  # writes go to the first mapping (cli)
print(cli)                             # {'debug': True, 'port': 7000}
print(env["port"])                     # 9000, env is unchanged
print(isinstance(config, dict))        # False
print(ChainMap(defaults, env, cli)["debug"])  # False: defaults now come first
```

Запис іде в перший mapping: `config["port"] = 7000` змінює `cli`, а `env` лишається з 9000, тобто нижній шар не переписується.[^py314-library-collections-chainmap] Видалення діє так само: `del` ключа, якого немає в першому mapping, дає `KeyError`, навіть якщо ключ є в нижньому шарі.

Межі підходу: `ChainMap` не є `dict` (`isinstance(config, dict)` дає `False`), тому `json.dumps(config)` не працює, а для знімка використовують `dict(config)`. Пошук проходить усі mappings, коли ключа немає, тож для кількох шарів це несуттєво. Порядок аргументів визначає пріоритет: `ChainMap(defaults, env, cli)` дає `defaults` перевагу, і `config["debug"]` стає `False`.

**Типові помилки:**
- ставити `defaults` першим аргументом: тоді вони перекривають CLI і env;
- очікувати, що запис у `config` змінить шар, у якому ключ визначено: змінюється лише перший mapping;
- вважати, що `ChainMap` зберігає знімок конфігурації на момент створення, хоча зміни нижніх шарів видно одразу.
