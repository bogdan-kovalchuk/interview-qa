---
id: emb-raii-0028
title: "Чому RAII дає deterministic destruction, а garbage collection – ні?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-basic-stc-auto
    title: "C++ working draft: [basic.stc.auto]"
    url: https://eel.is/c++draft/basic.stc.auto
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
  - source_id: cpp-core-guidelines-r1
    title: "C++ Core Guidelines, R.1: Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cpp-draft-support-runtime
    title: "C++ working draft: [support.runtime] (setjmp, longjmp)"
    url: https://eel.is/c++draft/support.runtime
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
