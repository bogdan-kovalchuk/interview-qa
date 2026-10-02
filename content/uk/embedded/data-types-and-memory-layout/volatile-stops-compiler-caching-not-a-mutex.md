---
id: emb-dtypes-0082
title: "Що таке `volatile` і як він взаємодіє з оптимізацією компілятора?"
description: "volatile забороняє кешувати чи видаляти звернення до змінної, але не дає atomicity чи memory ordering між потоками."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: gcc-volatiles
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Описує правила GCC для volatile accesses, зокрема межі щодо порядкування звичайної пам’яті; не є заміною синхронізації потоків."
---

## Short answer

`volatile` позначає доступи, які реалізація має трактувати як volatile; у вбудованому коді це часто потрібне для memory-mapped registers або значень, що змінюються поза звичайним потоком виконання.[^iso-c-n1570] [^gcc-volatiles]

Без volatile-доступу компілятор може оптимізувати повторні читання чи записи звичайної змінної, якщо за правилами мови її значення не змінюється спостережуваним способом.[^gcc-volatiles]

<span class="warn">volatile не є синхронізацією</span>: він не забезпечує atomicity і не створює міжпотокового happens-before. Для спільного стану потоків C++ застосовуй `std::atomic` або mutex відповідно до потрібного протоколу.[^gcc-volatiles] [^iso-c-n1570]

## Detailed explanation

`volatile` є кваліфікатором типу, який впливає на те, як програма спостерігає читання та записи об’єкта. Його типовий embedded-застосунок – memory-mapped register: кожне читання може повернути новий стан периферії, а запис може мати побічний ефект на пристрої. Інший приклад – змінна, яку змінює ISR. Саме оголошення має відповідати контракту доступу, наприклад `volatile uint32_t * const status = ...`; кваліфікатор не робить адресу правильною і не пояснює, які саме ширина та семантика регістра.[^iso-c-n1570] [^gcc-volatiles]

Звичайну змінну компілятор може зберегти в регістрі процесора або прибрати доступ, якщо це не змінює поведінку, визначену мовою. Для volatile object доступи мають іншу спостережуваність, але точне визначення volatile access частково лишається за реалізацією. У GCC volatile не є загальним бар’єром пам’яті: звичайні non-volatile об’єкти не отримують автоматичного порядкування відносно volatile-доступу, а кілька операцій усередині однієї full expression можуть комбінуватися чи переставлятися відповідно до правил компілятора.[^gcc-volatiles]

Особливо небезпечно трактувати `volatile` як засіб захисту спільної змінної між потоками. Два конкурентні неатомарні доступи можуть утворити data race в C++, а `volatile` цього не усуває і не робить read-modify-write атомарним. Для лічильника потрібен `std::atomic` з доречним memory order; для узгодженої зміни кількох полів зазвичай потрібен mutex. В ISR правила залежать від платформи: `volatile` може змусити повторно читати стан, але критичну секцію чи атомарний доступ усе одно треба визначати з урахуванням ширини операції та архітектури.[^iso-c-n1570] [^gcc-volatiles]

**Типові помилки:**

- Вважати `volatile` синонімом atomic або memory barrier. Це різні гарантії; обирай примітив, який задає потрібну синхронізацію.[^gcc-volatiles]
- Позначати volatile всі змінні «про всяк випадок». Це не усуває data race і може завадити оптимізаціям без додавання потрібного протоколу.
- Робити `counter++` у головному циклі й ISR та вважати операцію безпечною лише через volatile. Інкремент – читання, обчислення і запис; перевір атомарність саме на цільовому MCU або захисти операцію належним чином.[^iso-c-n1570]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
