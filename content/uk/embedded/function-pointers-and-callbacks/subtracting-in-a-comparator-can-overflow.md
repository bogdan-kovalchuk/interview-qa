---
id: emb-fnptr-0033
title: "Trap: що не так із comparator-ом для `qsort`?"
description: "Віднімання може переповнити int, що для signed overflow є undefined behavior."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
int cmp(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}
```

## Short answer

<span class="warn">Віднімання двох `int` може переповнити результат; signed overflow має undefined behavior у C.</span>

Якщо один елемент `INT_MIN`, а інший `INT_MAX`, математична різниця не представима в `int`; стандарт C визначає signed overflow як undefined behavior. Comparator має повертати порядок, а не обов’язково арифметичну різницю.[^iso-c-n1570]

Захист: використовуй `return (x > y) - (x < y);` після читання `x` і `y`.[^iso-c-n1570]

## Detailed explanation

Поширений comparator для цілих чисел повертає різницю `x - y`, сподіваючись отримати від’ємне, нульове або додатне значення. Але вираз обчислюється саме в типі `int`; якщо точна різниця виходить за його діапазон, результат не можна представити. Для signed integer arithmetic у C така ситуація є undefined behavior, а не гарантованим циклічним переходом до протилежного знака.[^iso-c-n1570]

Для прикладу, коли `x` дорівнює `INT_MIN`, а `y` дорівнює `INT_MAX`, вираз `x - y` вимагає значення нижче за `INT_MIN`. Аналогічно, `INT_MAX - INT_MIN` перевищує верхню межу. Обидві крайні пари можуть трапитися навіть тоді, коли звичайні невеликі значення проходили тести. Конкретний зовнішній симптом не визначений: comparator може повернути неочікуваний знак або оптимізований код може поводитися інакше, бо компілятор має право припускати відсутність undefined behavior.[^iso-c-n1570]

Це важливо для `qsort`, бо comparator має повідомити лише відносний порядок двох елементів. Контракту достатньо знака результату: від’ємне, нуль або додатне значення. Повна арифметична відстань між числами не потрібна, і обчислення її додає ризик без користі.[^iso-c-n1570]

Приклад: масив може містити `INT_MIN`, `0` та `INT_MAX`. Comparator на відніманні має правильно впорядкувати всі три, але порівняння крайніх значень створює результат поза діапазоном `int`. Тому помилка здатна змінити порядок сортування або з’явитися лише на даних, що містять граничні числа; запуск на тестовому масиві з малими додатними значеннями її не викриває.[^iso-c-n1570]

**Типові помилки:**

- Вважати, що signed overflow гарантовано обгортається так само, як unsigned арифметика.
- Перевірити лише типові значення й не включити `INT_MIN` та `INT_MAX`.
- Замінити `int` на ширший signed type, не довівши, що всі можливі різниці помістяться.

Щоб виправити comparator, порівнюйте через `<` і `>` та повертайте малу сталу різницю знаків. Так результат залежить тільки від порядку операндів, а не від величини їхньої різниці.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
