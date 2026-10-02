---
id: emb-dtypes-0044
title: "Що таке stack canary і як він захищає від stack overflow?"
description: "Stack canary - магічне значення перед адресою повернення, чия зміна при виході з функції виявляє переповнення стека."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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
  - source_id: gcc-stack-protector
    title: "GCC instrumentation options: stack protection"
    url: https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Поведінка прапорців GCC stack protector, умови інструментування, перевірка guard і обробка помилки; деталі залежать від цілі та runtime."
---

## Short answer

Stack canary – захисне значення, яке компілятор розміщує у кадрі деяких функцій і перевіряє перед поверненням; точне розташування залежить від ABI та реалізації.[^gcc-stack-protector]

Якщо перевірка виявить зміну, runtime виконує failure path; це свідчить про пошкодження захищеного кадру, але не доводить, що причиною був саме stack overflow.[^gcc-stack-protector]

У GCC захист можна ввімкнути прапорцем `-fstack-protector-strong`; у bare-metal потрібна сумісна реалізація runtime та обробника помилки.[^gcc-stack-protector]

## Detailed explanation

Stack canary – це значення-запобіжник, яке інструментований компілятор записує у кадр функції, а перед виходом порівнює з очікуваним значенням. Якщо значення змінилося, програма переходить до аварійної обробки замість звичайного повернення. У GCC параметр `-fstack-protector-strong` додає таку перевірку до функцій, які компілятор вважає вразливими за визначеними евристиками; сам факт наявності прапорця не означає, що кожна функція має canary.[^gcc-stack-protector]

Захист допомагає виявити деякі пошкодження пам’яті, наприклад переписування локального буфера, яке зачепило canary. Він зазвичай виявляє проблему під час епілогу функції, а не в момент першого запису поза межами. До цього часу пошкоджені дані могли вже вплинути на програму. Крім того, перевірка може спрацювати через інше пошкодження кадру; вона не визначає першопричину і не є повною перевіркою меж стеку.[^gcc-stack-protector]

Не слід трактувати canary як гарантоване значення `0xDEADBEEF` або як байти, обов’язково розташовані безпосередньо перед адресою повернення. Значення, компонування кадру і місце перевірки залежать від цільового ABI, компілятора та runtime. Після виявлення GCC викликає failure handler; у стандартному середовищі це зазвичай `__stack_chk_fail`, тоді як bare-metal має забезпечити відповідну реалізацію та спосіб повідомити або безпечно завершити систему.[^gcc-stack-protector]

**Приклад:** якщо локальний масив переповнено записами, а один із записів змінює canary, перевірка перед поверненням може зупинити звичайний перехід до адреси повернення. Якщо переповнення не торкнулося canary або функцію не інструментовано, цей механізм може не помітити помилку. Тому його поєднують із коректними межами буферів, аналізом стеку та іншими захистами, підібраними для платформи.[^gcc-stack-protector]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
