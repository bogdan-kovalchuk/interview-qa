---
id: emb-align-0027
title: "Навіщо вирівнювати буфер по cache line?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: stm32-an4839
    title: "STMicroelectronics AN4839: Level 1 cache on STM32F7 and STM32H7 Series"
    url: https://www.st.com/resource/en/application_note/an4839-level-1-cache-on-stm32f7-series-and-stm32h7-series-stmicroelectronics.pdf
  - source_id: linux-false-sharing
    title: "Linux kernel documentation: False Sharing"
    url: https://docs.kernel.org/kernel-hacking/false-sharing.html
---

## Short answer

**Щоб керувати розміщенням даних відносно cache line, коли цього вимагає сценарій.**

False sharing виникає, коли незалежні дані, до яких конкурентно звертаються ядра, потрапляють в одну cache line. Для DMA на кешованій пам’яті потрібна узгодженість через cache maintenance або некешовану область; саме вирівнювання її не забезпечує.[^stm32-an4839]

Розмір cache line і потрібну ізоляцію перевіряйте для конкретної платформи; виконання clean/invalidate залежить від напрямку DMA.[^stm32-an4839]

## Detailed explanation

Вирівнювання за cache line розміщує початок об’єкта на межі лінії кешу, але саме по собі не відокремлює сусідні об’єкти і не синхронізує кеш із DMA.[^stm32-an4839]

False sharing – це втрата продуктивності, коли різні ядра часто змінюють незалежні змінні, що лежать у тій самій cache line: протокол когерентності передає або інвалідує цілу лінію. Щоб ізолювати змінні, треба врахувати і початкову адресу, і розмір об’єкта, і межі сусідніх даних; вирівнювання лише початку може бути недостатнім.[^linux-false-sharing]

DMA має іншу проблему. Якщо CPU і DMA працюють із кешованою областю без узгодження, CPU може читати стару копію або DMA може побачити ще не записані в RAM дані. Для STM32F7/H7 з Cortex-M7 ST описує 32-байтові cache lines та приклади cache clean/invalidate; це значення й процедури не можна автоматично переносити на інші MCU.[^stm32-an4839]

Приклад: якщо конкретний контролер має 32-байтову лінію, окремий буфер можна розмістити на 32-байтовій межі, а його розмір округлити до цілої кількості ліній. Перед застосуванням операції кешу звірте її вирівнювальні та адресні вимоги з документацією платформи.

**Типові помилки:**

- Вважати, що будь-яке вирівнювання автоматично усуває false sharing.
- Вважати 32 або 64 байти універсальним розміром cache line.
- Виконувати cache maintenance без урахування напрямку передачі DMA.

Використовуйте padding або окрему область лише після вимірювання false sharing, а для DMA обирайте між некешованою пам’яттю та документованими cache maintenance операціями.
