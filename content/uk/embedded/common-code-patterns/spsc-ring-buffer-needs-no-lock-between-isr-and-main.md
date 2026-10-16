---
id: emb-patterns-0007
title: "Що таке SPSC ring buffer і за яких умов він працює без блокування?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-circular-buffers
    title: "Linux kernel documentation: Circular Buffers"
    url: https://docs.kernel.org/core-api/circular-buffers.html
---

## Short answer

**SPSC (single-producer / single-consumer) кільцевий буфер** може не потребувати mutex, якщо індекси атомарні, а платформа забезпечує потрібний порядок публікації даних. Одного writer-а на індекс недостатньо.[^linux-circular-buffers]

Типовий варіант – producer в ISR (interrupt service routine), наприклад UART RX (universal asynchronous receiver-transmitter receive), та consumer у main loop. `head` і `tail` мають окремих власників, але конкретний спосіб атомарного доступу й ordering залежить від платформи.[^linux-circular-buffers]

Підходить для потокових даних із визначеною поведінкою при full/empty; перевір платформні гарантії перед використанням.[^linux-circular-buffers]

## Detailed explanation

SPSC означає, що протягом роботи черги є рівно один producer і один consumer. У кільцевому буфері producer додає елементи за `head`, а consumer бере наступний елемент за `tail`; індекси обертаються на початок масиву. Часто одну позицію залишають незайнятою: тоді рівність індексів означає empty, а наближення наступного `head` до `tail` означає full.[^linux-circular-buffers]

Окремі власники індексів зменшують взаємне втручання: producer змінює тільки `head`, consumer – тільки `tail`. Але це не доводить, що реалізація автоматично безпечна без synchronization. Consumer має побачити вміст слота до того, як побачить опублікований `head`; producer має не перезаписати слот до того, як побачить оновлений `tail`. Для Linux документація описує barriers та acquire/release операції саме для такого впорядкування.[^linux-circular-buffers]

У MCU-проєкті треба перевірити конкретний toolchain і архітектуру: чи є доступ до індексу атомарним, які гарантії мають переривання щодо main code, і який механізм забезпечує порядок доступів. `volatile` сам по собі не є повним протоколом синхронізації. Якщо гарантій немає, застосуй документований atomic primitive або коротку критичну секцію, якщо це допустимо для часових вимог.

**Типові помилки:**

- Дозволити другому ISR або task писати в ту саму чергу, зруйнувавши умову одного producer-а.
- Називати реалізацію lock-free лише через відсутність явного mutex.
- Не визначити політику переповнення й мовчки втратити або перезаписати дані.

Перш ніж обирати цей шаблон для UART чи ADC, зафіксуй producer, consumer, повний/порожній випадки й платформну гарантію синхронізації.[^linux-circular-buffers]
