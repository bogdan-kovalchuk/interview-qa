---
id: py-coll-0016
title: "Чому некоректний `__eq__` у custom objects може призвести до несподіваних результатів membership у set?"
description: "Set шукає елемент спочатку за hash() (bucket), потім порівнює __eq__; якщо __eq__ і __hash__ неузгоджені, membership дає хибні результати."
track: python
section: collections
level: senior
type: pitfall
tags: [eq]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L388-L440
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Set шукає елемент спочатку за `hash()` (bucket), потім порівнює `__eq__`; якщо `__eq__` і `__hash__` неузгоджені, membership дає хибні результати.**[^py314-library-stdtypes] Контракт: `a == b` -> `hash(a) == hash(b)`. Якщо `__eq__` повертає `True`, але `hash()` різний, set не знайде об'єкт у правильному bucket – `b in {a}` поверне `False`, хоча `a == b`. <span class="warn">Завжди визначайте `__hash__` і `__eq__` разом, використовуючи одні й ті самі поля.</span>

## Detailed explanation

Найпоширеніша пастка виникає ще до того, як хтось порушує сам contract: якщо клас визначає лише
`__eq__` і не визначає `__hash__`, Python автоматично встановлює `__hash__ = None`, і клас стає
unhashable – спроба покласти такий об'єкт у `set` чи використати як ключ `dict` кидає `TypeError`
ще до будь-якого membership-тесту.[^py314-library-stdtypes] Це рятує від тихого багу, але часто
дивує тих, хто очікував успадкувати hash за замовчуванням від `object` (він базується на `id()` і
теж працює, але порушує сам контракт "рівні об'єкти – однаковий hash").

Другий, тихіший варіант – коли `__hash__` обчислюється з тих самих полів, що і `__eq__`, але поля
мутабельні і клас усе одно кладуть у `set`. Приклад: `hash()` рахується з поля `name`, об'єкт
додано в `set`, а потім `name` змінили in-place. Bucket, у якому лежить об'єкт, залишається старим
– тим, куди його поклали за попереднім `hash()` – тому подальший пошук за новим значенням `name` не
знайде цей об'єкт, `in` поверне `False`, хоча об'єкт фізично присутній у множині. Це саме причина,
чому mutable-поля не варто включати в `__hash__`.

Третій випадок – асиметричне порівняння: якщо `A.__eq__` повертає `True` для `B`, але `B.__eq__`
не повертає `True` для `A` (наприклад, `B` – інший тип із власною, несумісною логікою), поведінка
`in` залежить від того, з якого боку викликається порівняння всередині bucket-а, і результат стає
непередбачуваним залежно від порядку вставки.

Практичний висновок – використовувати для `__hash__` лише ті поля, що незмінні протягом усього
часу життя об'єкта в колекції (в ідеалі – заморожені `frozen` dataclass чи `NamedTuple`, де
`__eq__` і `__hash__` генеруються узгоджено автоматично), і ніколи не покладатися на порівняння
з об'єктами інших типів без явної симетричної перевірки.

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
