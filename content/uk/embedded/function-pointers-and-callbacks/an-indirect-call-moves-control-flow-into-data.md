---
id: emb-fnptr-0057
title: "Trap: чому indirect call через function pointer може бути проблемою в safety-critical firmware?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: c11-function-pointers
    title: "ISO/IEC 9899:2011 Committee Draft N1570, 6.3.2.3"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">Він переносить control-flow decision у дані.</span>

Якщо function pointer пошкоджений через memory corruption, out-of-bounds access або stack bug, непрямий виклик може перейти не до очікуваної функції. Вплив залежить від архітектури, пам’яті та захистів системи.[^c11-function-pointers]

Захист: зберігай незмінні таблиці у read-only пам’яті, перевіряй індекси й вхідні значення та використовуй MPU/stack protection, якщо платформа їх підтримує.[^c11-function-pointers]

## Detailed explanation

Indirect call переносить вибір цілі керування з явного виклику на значення function pointer, яке програма зчитує під час виконання.[^c11-function-pointers]

У статичному виклику інструкція кодує переходи до конкретної функції. Для непрямого виклику код спершу бере адресу з pointer або таблиці, а тоді передає їй керування. Це корисно для callbacks і драйверних таблиць, але означає, що цілісність даних, які задають адресу, є частиною цілісності control flow.

Якщо помилка запису пошкодить pointer або індекс таблиці, процесор спробує виконати іншу адресу. Результатом може стати fault, аварійне завершення або поведінка, яку важко відтворити; конкретний наслідок залежить від MCU, memory protection і розміщення коду. Function pointer також має відповідати очікуваній сигнатурі: виклик через несумісний тип у C має undefined behavior, а не безпечне перетворення виклику.[^c11-function-pointers]

Приклад: індекс `mode` з пакета UART не можна напряму застосовувати до `handlers[mode]`. Спершу перевір межу таблиці та допустимість режиму. Якщо функціональність не потребує змінної таблиці, простий `switch` робить перелік переходів явним. Якщо таблиця потрібна, оголоси її read-only там, де це підтримує платформа, і не записуй у неї адреси з зовнішніх даних.

**Типова помилка:** вважати, що `const` сам по собі розміщує таблицю у захищеній Flash або усуває всі пошкодження. Перевір linker map і налаштування MPU, валідуй selector на межі input та аналізуй fault logs. Захист пам’яті зменшує ризик, але не замінює перевірку меж.
