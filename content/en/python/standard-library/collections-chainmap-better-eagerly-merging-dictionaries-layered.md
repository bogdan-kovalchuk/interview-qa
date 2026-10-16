---
id: py-stdlib-0001
title: "When is `collections.ChainMap` better than eagerly merging dictionaries for layered configuration with precedence between the command line, environment, and defaults?"
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

**`ChainMap` searches the mappings successively from first to last and creates no merged dict, so changes in the lower layers are visible without a repeated merge.**[^py314-library-collections-chainmap] The search order follows the order of the arguments: in `ChainMap(cli, env, defaults)`, the CLI mapping is checked first.[^py314-library-collections-chainmap-maps] Writes, updates, and deletions affect only the first mapping.[^py314-library-collections-chainmap] It is useful for layered config where the layers are updated independently, because no repeated merge is needed after each change.

## Detailed explanation

An eager merge (`{**defaults, **env, **cli}`, or a loop with `update()`) copies the keys into a new dict at the moment of merging. After that, the result is a snapshot: a later change to `defaults` or `env` does not reach it. `ChainMap`, by contrast, keeps references to the original mappings and looks values up in them on every access, so updates to a layer are visible at once.[^py314-library-collections-chainmap]

An example: the CLI has the highest priority, then env, then defaults. The comments show what the `ChainMap` sees and what stays a snapshot.

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

A write goes to the first mapping: `config["port"] = 7000` changes `cli`, and `env` keeps 9000, so the lower layer is not overwritten.[^py314-library-collections-chainmap] Deletion works the same way: `del` of a key that is not in the first mapping raises `KeyError`, even if the key exists in a lower layer.

The limits of the approach: a `ChainMap` is not a `dict` (`isinstance(config, dict)` is `False`), so `json.dumps(config)` does not work, and a snapshot is taken with `dict(config)`. A lookup checks every mapping when the key is missing, so this cost is negligible for a few layers. The order of the arguments defines the priority: `ChainMap(defaults, env, cli)` gives `defaults` precedence, and `config["debug"]` becomes `False`.

**Common mistakes:**
- putting `defaults` first in the arguments: they then override the CLI and env values;
- expecting a write to `config` to change the layer where the key is defined: only the first mapping changes;
- assuming `ChainMap` keeps a snapshot of the configuration from the moment it was created, when changes in lower layers are visible at once.
