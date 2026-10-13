---
id: emb-raii-0028
title: "Чому RAII дає deterministic destruction, а garbage collection – ні?"
description: "Деструктор виконується в точно відомий момент – при виході зі scope."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
content_revision: 2
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: [basic.stc.auto]"
    url: https://eel.is/c++draft/basic.stc.auto
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Точний пункт стандарту: автоматичний об’єкт з деструктором, що має побічні ефекти, не можна знищити раніше кінця його блоку. Не описує RTOS, ISR чи збирач сміття."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Примітка до [stmt.jump]: при виході з області видимості (будь-яким способом) автоматичні об’єкти, побудовані в ній, знищуються у зворотному порядку побудови; std::exit і std::abort можуть завершити програму без знищення таких об’єктів. Не описує embedded-ресурси."
  - source_id: cpp-core-guidelines-r1
    title: "C++ Core Guidelines, R.1: Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Правило R.1 керівних принципів C++ Core Guidelines: захоплення ресурсу в конструкторі і звільнення в деструкторі, що відбувається автоматично на всіх шляхах виконання, включно з винятками. Не описує збирач сміття."
  - source_id: cpp-draft-support-runtime
    title: "C++ working draft: [support.runtime] (setjmp, longjmp)"
    url: https://eel.is/c++draft/support.runtime
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Точний пункт стандарту: пара setjmp/longjmp має undefined behavior, якщо заміна на catch/throw викликала б нетривіальні деструктори автоматичних об’єктів. Не описує інші способи виходу з функції."
---

## Short answer

**Деструктор виконується в точно відомий момент – при виході зі scope.**

Для автоматичного об’єкта з деструктором, що має побічні ефекти, реалізація не може знищити його раніше кінця блоку.[^cpp-draft-basic-stc-auto] Тому ресурс, захоплений у конструкторі, звільняється при виході з блоку, без участі збирача сміття (GC).[^cpp-draft-stmt-jump]

Правило: ресурс, який треба звільнити вчасно, тримай в RAII-обгортці, а не в парному ручному виклику, який легко пропустити.[^cpp-core-guidelines-r1]

## Detailed explanation

Деструктор – це функція, яку мова викликає автоматично, коли закінчується тривалість життя об’єкта. Для автоматичних змінних, тобто локальних об’єктів блоку, це кінець блоку: якщо деструктор має побічні ефекти, реалізація не може знищити такий об’єкт раніше.[^cpp-draft-basic-stc-auto] Тому RAII-обгортка, яка в конструкторі захоплює шину SPI або м’ютекс, відпускає його в точно визначеній точці: при `return`, при виході з блоку[^cpp-draft-stmt-jump] і при розгортанні стеку винятком, якщо винятки використовуються.[^cpp-core-guidelines-r1]

```cpp
// Illustrative: SpiBusLock is an RAII wrapper around a bus mutex.
// SpiBusLock, spi_bus and spi_write are declared elsewhere.
void send_frame(const unsigned char* buf, unsigned n) {
    SpiBusLock lock{spi_bus};  // acquired in the constructor
    if (n == 0) {
        return;                // destructor runs here: bus released
    }
    spi_write(buf, n);
}                              // destructor runs here too
```

Перший `return` у прикладі звільняє шину, хоча функція не дійшла до запису. Без RAII довелося б пам’ятати про unlock перед кожним `return`, і кожен пропущений unlock залишав би шину зайнятою.

Межі цієї гарантії. Вона стосується нормального виходу з блоку і розгортання стеку винятком, але не завершення програми через `exit` чи `abort`: тоді локальні об’єкти не знищуються.[^cpp-draft-stmt-jump] Пара `setjmp`/`longjmp` має undefined behavior, якщо заміна на `catch`/`throw` викликала б нетривіальні деструктори автоматичних об’єктів.[^cpp-draft-support-runtime] Тож перехід через `longjmp` із RAII-об’єктами на стеку не можна вважати безпечним очищенням.

**Типові помилки:**

- Вважати, що деструктор викликається «колись», як у моделі GC, а не в точці виходу з блоку.
- Вручну звільняти ресурс перед кожним `return` замість деструктора RAII-обгортки.
- Використовувати `longjmp` для виходу з функції, де є RAII-об’єкти.

## Sources

<!-- generated from frontmatter -->
