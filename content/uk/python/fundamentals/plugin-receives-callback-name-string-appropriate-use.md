---
id: py-fund-0008
title: "Плагін отримує name callback як string: коли доречно використати `getattr(plugin, name)`, а коли безпечнішим API буде явний registry allowed callbacks?"
description: "getattr() доречний, коли dynamic attribute lookup є частиною довіреного контракту plugin API, а name уже перевірено."
track: python
section: fundamentals
level: middle
type: comparison
tags: [getattr-plugin-name]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L332-L393
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`getattr()` доречний, коли dynamic attribute lookup є частиною довіреного контракту plugin API, а name уже перевірено.**[^py314-reference-executionmodel] Якщо name надходить із конфігурації або зовнішнього вводу, явний registry краще фіксує allowlist, aliases і стабільний public API. Після `getattr()` все одно потрібно перевірити, що значення дозволене та callable.

## Detailed explanation

`getattr(obj, name)` – це звичайний доступ до атрибута, у якому ім'я обчислюється, а не записане в
коді. Він проходить той самий protocol, що й `obj.name`: `__getattribute__`, дескриптори, а за
відсутності – `__getattr__`.[^py314-reference-datamodel] Нічого «магічного» чи обхідного тут немає.

Питання не в тому, чи `getattr` безпечний сам собою, а в тому, **звідки взявся рядок**. Якщо ім'я
приходить із довіреного, зафіксованого контракту – наприклад, plugin оголошує набір hook-методів, і
ядро питає рівно про них – це нормальний dynamic dispatch.

Якщо ж рядок приходить із конфігурації, HTTP-запиту або бази даних, то `getattr` без перевірки
перетворює будь-який атрибут об'єкта на публічний API. Викликач може дістатися до приватних методів,
до `__class__` і далі, а помилка в конфізі дасть `AttributeError` замість зрозумілого повідомлення.

```python
# trusted: the hook set is part of the plugin contract, fixed in code
for hook in ('on_start', 'on_finish'):
    handler = getattr(plugin, hook, None)
    if handler is not None:
        handler()

# untrusted input: an allowlist decides, not the object's namespace
ACTIONS = {'export': do_export, 'import': do_import}
action = ACTIONS.get(user_supplied)      # None instead of a random attribute
```

Явний registry виграє не тим, що він «швидший», а тим, що робить дозволений набір даними: його видно
в коді, він діфиться в review, він не залежить від того, які ще атрибути має об'єкт, і він дозволяє
мати aliases та стабільні публічні імена, не прив'язані до імен методів.

**Що перевірити, якщо `getattr` усе-таки доречний:**
- ім'я входить у явний allowlist, а не просто «не починається з підкреслення»;
- отримане значення справді callable – інакше виклик дасть `TypeError` у випадковому місці;
- є `default` (третій аргумент), щоб відсутній hook не був винятком, коли він опційний;
- відсутність атрибута обробляється як штатний випадок, а не як помилка користувача.

Останнє, про що легко забути: `getattr` робить зв'язок невидимим для інструментів. Пошук по коду за
іменем методу не знайде місце виклику, а IDE не покаже, що метод узагалі
використовується.[^py314-reference-executionmodel] Для внутрішнього API це аргумент проти; для
plugin API, де реалізації пишуть інші люди, це прийнятна ціна за розширюваність.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
