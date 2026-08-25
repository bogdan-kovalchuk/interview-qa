# Топікові брифи

23 дослідницькі брифи, перенесені з попереднього проєкту. Кожен має структуру:
`Goal and scope` → `Sources` → `Coverage plan` → `Sensitive boundaries`.

**Це сировина для `meta/objectives/`**, які ще не написані (`PROGRESS_TRACKING.md` §3a).
`Coverage plan` у брифі – це вже майже готова таблиця цілей:

```
| Cluster                              | Retrieval operation   | Middle | Senior |
| Coroutines awaitables and tasks      | distinguish and trace |   3    |   1    |
| Cancellation timeouts and shielding  | design and diagnose   |   2    |   2    |
```

Кластер + операція + розподіл за рівнями – це «ціль → сигнали → рівні» новою мовою.
Перетворення на `meta/objectives/python.yml` – робота M1.

Обмеження, яке треба пам'ятати: брифи писалися під стару таксономію з 23 тем і плоскими
номерами. Нова таксономія (`TAXONOMY.md`) інша, і теми 21–23 узагалі переїжджають в інші треки
(`cs`, `databases`, `engineering`). Мапа – `meta/migration/tag-mapping.md`.
