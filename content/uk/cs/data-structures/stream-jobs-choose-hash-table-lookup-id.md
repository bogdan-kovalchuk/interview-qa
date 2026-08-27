---
id: cs-dstruct-0001
title: "Коли для потоку jobs обрати hash table для lookup by ID, а коли min-heap для постійного вилучення найменшого priority?"
description: "dict дає O(1) середню складність пошуку за ключем; min-heap на основі heapq дає O(log n) для push/pop і O(1) для перегляду найменшого елемента."
track: cs
section: data-structures
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-bisect
    title: "Python 3.14: Library/bisect"
    url: https://docs.python.org/3.14/library/bisect.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/data_structures.md#L85-L154
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`dict` дає O(1) середню складність пошуку за ключем; min-heap на основі `heapq` дає O(log n) для push/pop і O(1) для перегляду найменшого елемента.**[^py314-library-collections] Обирайте hash table, коли основна операція – пошук або оновлення job за унікальним ID. Обирайте min-heap, коли потрібно постійно вилучати job з найменшим priority – heap не підтримує O(1) довільний пошук за ID.

## Detailed explanation

Обидві структури мають фундаментально різну внутрішню організацію. `dict` – це хеш-таблиця: ключ
хешується, і за хешем обчислюється прямий індекс у внутрішньому масиві, тому пошук, вставка й
видалення за ключем – O(1) в середньому (гірший випадок O(n) при масових колізіях, що на
практиці рідкість завдяки якості хеш-функції). Але `dict` не підтримує впорядкований доступ –
"знайти мінімум" вимагав би O(n) проходу по всіх значеннях.

`heapq` реалізує min-heap як звичайний `list`, де для індексу `i` дочірні елементи лежать за
індексами `2i+1` і `2i+2`; ця неявна деревовидна структура гарантує, що `heap[0]` завжди
мінімальний, а `heappush`/`heappop` відновлюють інваріант просіюванням (`sift up`/`sift down`)
за O(log n). Але heap не індексує елементи за довільним ключем: щоб перевірити, чи job з певним
ID уже в купі, або оновити його priority, треба лінійний прохід O(n) – структура даних просто не
зберігає, де саме лежить конкретний елемент.

Саме тому для потоку jobs, де потрібні обидві операції – швидкий lookup за ID і постійне
вилучення мінімального priority – типове рішення поєднує обидві структури: `dict` мапить ID на
запис (job, priority, прапорець валідності), а `heapq` зберігає ті самі записи як кортежі
`(priority, id)`. Оновлення priority реалізують через lazy deletion: старий запис у купі
позначають недійсним (наприклад, зберігши окремий "живий" запис у `dict`) замість того, щоб
видаляти його з середини купи за O(n), а при `heappop` пропускають недійсні записи, поки не
знайдуть актуальний мінімум.[^py314-library-heapq]

Цей гібрид – класична "indexed priority queue" – дає O(log n) для push/pop-min і O(1) для
lookup за ID ціною трохи складнішої бухгалтерії валідності записів.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
