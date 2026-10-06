---
id: emb-raii-0001
title: "Що таке RAII і як розшифровується?"
description: "RAII (Resource Acquisition Is Initialization) – lifetime ресурсу прив’язаний до lifetime C++-об’єкта: конструктор захоплює, деструктор звільняє."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; це джерело не є доказом тверджень."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 2: при кожній передачі керування в межах функції (зокрема при поверненні з неї) automatic-змінні блоку, активні в точці відправлення й неактивні в точці призначення, знищуються у зворотному порядку конструювання. Не охоплює завершення програми через exit чи abort і не описує винятки."
  - source_id: cpp-draft-except-ctor
    title: "C++ working draft: Stack unwinding ([except.ctor])"
    url: https://eel.is/c++draft/except.ctor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Описує знищення automatic-об’єктів у зворотному порядку при винятку та те, що при винятку з конструктора деструктори викликаються для вже ініціалізованих підоб’єктів; не діє, якщо винятки вимкнено компілятором."
  - source_id: cpp-draft-except-handle
    title: "C++ working draft: Handling an exception ([except.handle])"
    url: https://eel.is/c++draft/except.handle
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 8: якщо відповідного handler не знайдено, викликається std::terminate, а чи розкручується стек перед цим – implementation-defined. Про поведінку при вимкнених exceptions нічого не каже."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що std::abort завершує програму без виконання деструкторів, а std::exit не знищує automatic-об’єкти; freestanding-реалізації можуть не мати цих функцій."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Настанова: обгортати ресурс із парними acquire/release в об’єкт, що захоплює в конструкторі й звільняє в деструкторі; приклади – файли, mutex, пам’ять, не апаратна периферія."
---

## Short answer

**RAII (Resource Acquisition Is Initialization)** – lifetime ресурсу прив’язаний до lifetime C++-об’єкта.

Конструктор захоплює ресурс, деструктор звільняє його. Деструктор локального об’єкта викликається при виході зі scope будь-яким шляхом: кінець блоку, early `return`, `break`, `goto`.[^cpp-draft-stmt-dcl] Якщо exceptions увімкнені, то й при stack unwinding, коли exception дійшов до handler.[^cpp-draft-except-ctor]

Правило: усе, що має «взяти і віддати», загортай в об’єкт із ctor/dtor.[^cppcg-r1-raii]

## Detailed explanation

Сама назва трохи вводить в оману: найважливіше в RAII не «захоплення», а те, що **звільнення прив’язане до lifetime об’єкта**. Якщо об’єкт існує, то його конструктор уже захопив ресурс; коли об’єкт знищується, деструктор ресурс віддає. «Взяти» і «віддати» перестають бути двома окремими викликами, які треба не забути, і стають інваріантом класу. Core Guidelines радять саме це для кожного ресурсу з парними acquire/release: файлу, mutex, пам’яті.[^cppcg-r1-raii]

Механізм спирається на гарантію мови. Коли керування залишає блок – природним кінцем, через `return`, `break` чи `goto` – усі automatic-змінні, що були активні в цьому блоці, знищуються у зворотному порядку конструювання.[^cpp-draft-stmt-dcl] Тому код очищення пишеться один раз, у деструкторі, а не повторюється перед кожним `return` на error-шляхах. Якщо конструктор завершився винятком, знищуються вже повністю ініціалізовані підоб’єкти (члени, бази),[^cpp-draft-except-ctor] тож кожен ресурс корисно тримати у власному члені-обгортці.

Exceptions у прошивках часто вимкнені (`-fno-exceptions`), але RAII від цього не втрачає сенсу: early `return` на помилках нікуди не зникають. Коли exceptions увімкнені, деструктори запускаються й при stack unwinding.[^cpp-draft-except-ctor] Проте якщо handler не знайдено, викликається `std::terminate`, і чи розкручується стек перед цим – implementation-defined.[^cpp-draft-except-handle] Деструктори automatic-об’єктів не виконуються і тоді, коли програма завершується через `std::abort` чи `std::exit`.[^cpp-draft-support-start-term]

Ілюстративний приклад (функції `gpio_claim` і `gpio_release` вигадані):

```cpp
class PinHandle {
    int pin_;
public:
    explicit PinHandle(int pin) : pin_(pin) { gpio_claim(pin_); }
    ~PinHandle() { gpio_release(pin_); }
    PinHandle(const PinHandle&) = delete;
    PinHandle& operator=(const PinHandle&) = delete;
};

int transfer(const std::uint8_t* d, int n) {
    PinHandle cs(5);
    if (n == 0) return -1;              // gpio_release runs here
    if (spi_send(d, n) != 0) return -2; // and here
    return 0;                           // and here
}
```

Усі три виходи з `transfer` проходять через деструктор `PinHandle`, хоча в тілі функції немає жодного явного `gpio_release`.

**Типові помилки:**

- Захоплювати ресурс в окремому `init()` замість конструктора: об’єкт може існувати без ресурсу, і інваріант «живий об’єкт – ресурс утримується» зникає.
- Сподіватися на деструктор там, де програма завершується через `std::abort` чи `std::exit`, або зависає: деструктор не виконається.
- Лишити клас-власник копійованим: дві копії звільнять той самий ресурс двічі (див. qid:emb-raii-0004).

## Sources

<!-- generated from frontmatter -->
