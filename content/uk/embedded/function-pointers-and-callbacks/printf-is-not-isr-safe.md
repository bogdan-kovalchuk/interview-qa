---
id: emb-fnptr-0027
title: "Trap: що небезпечно у виклику `printf` з ISR callback-а?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: newlib-stdio
    title: "The Red Hat newlib C Library: Standard C library I/O and reentrancy"
    url: https://www.sourceware.org/newlib/libc.html
  - source_id: arm-interrupt-latency
    title: "Arm: A Beginner’s Guide on Interrupt Latency"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/beginner-guide-on-interrupt-latency-and-interrupt-latency-of-the-arm-cortex-m-processors
---

## Short answer

<span class="warn">Не вважай `printf` ISR-safe без гарантії конкретної libc та output backend.</span>

Залежно від libc та backend, `printf` може використовувати stream state чи lock або чекати завершення UART-передачі. Повторний виклик під час друку з main/task може пошкодити чи перемішати output і надовго затримати ISR.

Захист: у ISR callback збережи компактний запис у буфер або встанови flag, а друк виконай у task/main context; спеціальний backend використовуй лише за його документованої ISR safety.[^embeddedinterviewlab] [^newlib-stdio]

## Detailed explanation

`printf` форматує та передає текст через стандартний output stream, але C API не обіцяє, що конкретна реалізація або її backend безпечно працюватимуть усередині ISR. Наприклад, документація Newlib описує stream-стан і механізми блокування для роботи з потоками, а самі операції виводу залежать від підтримки цільового середовища. UART backend може передавати байти polling-ом або чекати ресурс, тому час виклику не обов’язково малий чи обмежений.[^newlib-stdio]

ISR не є звичайним task-контекстом: якщо перерваний код уже виконував друк, виклик того самого механізму з ISR може повторно увійти в стан бібліотеки або backend. Якщо там є lock, переривання може чекати lock, який утримує перерваний код, що створює deadlock; навіть без lock довге очікування збільшує час обслуговування переривання і затримує іншу роботу. Чи станеться це, залежить від libc, RTOS, драйвера виводу та способу синхронізації, тому проблема не є однаковою на всіх платформах.[^newlib-stdio] [^arm-interrupt-latency]

Безпечніший шаблон – сформувати мінімальну подію без форматування: записати код події та потрібні числові поля у кільцевий буфер, або виставити flag. Звичайний task згодом читає запис і викликає `printf`, коли може безпечно чекати на output. Буфер має мати визначену політику переповнення; ISR не повинен блокуватися, очікуючи вільного місця. Якщо платформа надає спеціальну trace-функцію для ISR, перевір її документацію щодо reentrancy, блокувань, допустимого часу та розміру запису.[^newlib-stdio]

**Типова помилка:** додати `printf` «лише для діагностики» в ISR і потім пояснювати випадкові зависання шумом у UART. Симптом може проявлятися лише при одночасному друці з main/task або при великому обсязі повідомлень. Щоб уникнути цього, перевір контракт backend і виміряй worst-case час; за відсутності явної гарантії передавай компактні події для відкладеного форматування.[^newlib-stdio] [^arm-interrupt-latency]

Приклад: ISR таймера може покласти timestamp і короткий event code в попередньо виділений буфер. Logger task перетворить їх на текст і надрукує пізніше, тож форматування та UART очікування не займають interrupt context. Якщо потрібен бінарний trace, переконайся, що запис атомарний або коректно синхронізований між ISR і task.[^newlib-stdio]
