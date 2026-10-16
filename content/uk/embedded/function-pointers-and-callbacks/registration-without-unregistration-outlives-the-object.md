---
id: emb-fnptr-0043
title: "Trap: що не так із реєстрацією callback-а без unregister?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cppreference-pointer
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
  - source_id: cppcoreguidelines-lifetime
    title: "C++ Core Guidelines: Lifetime safety"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines
---

## Short answer

<span class="warn">Driver може викликати callback після знищення module/object-а.</span>

Особливо у C++ embedded: object destructor може завершитися, але C HAL усе ще зберігає `ctx = this`. Наступний interrupt викликає thunk із dangling `this` pointer.

Захист: у destructor або shutdown path unregister callback і disable interrupts/events перед знищенням state. Визнач ownership у API.[^cppcoreguidelines-lifetime]

## Detailed explanation

Зареєстрований callback стає небезпечним, якщо збережений ним object знищується раніше, ніж driver перестає його викликати.[^cppcoreguidelines-lifetime]

Під час реєстрації API зазвичай зберігає function pointer і, можливо, context pointer. Якщо контекстом є `this`, driver фактично зберігає адресу екземпляра, але не продовжує його час життя. Після виходу з області видимості або завершення destructor пам’ять більше не містить живого object-а цього класу. Наступний interrupt може викликати thunk, який розіменує застарілий вказівник; наслідком бувають пошкодження стану, падіння або зовні випадкова поведінка.[^cppreference-pointer]

Проблема стосується не лише C++ object-ів. У C так само небезпечно зберігати callback із контекстом на стекову структуру після повернення з функції. У багатопоточній чи interrupt-driven системі одного виклику `unregister` недостатньо, якщо callback уже виконується або pending event ще може його запустити. Потрібен протокол зупинки, визначений конкретним API: заборонити нові події, синхронізуватися з активним викликом і лише потім звільняти стан.

Наприклад, власник периферійного драйвера може в `shutdown` вимкнути переривання, дочекатися завершення обробника, зняти реєстрацію, а тоді знищити об’єкт. Порядок важливий: звільнення ресурсу перед припиненням джерела викликів залишає вікно для use-after-free.

**Типові помилки:**

- вважати, що завершення destructor-а автоматично прибирає реєстрацію;
- викликати `unregister`, не перевіривши його гарантії щодо активних callback-ів;
- покладатися на те, що dangling pointer «ще містить старі дані».
