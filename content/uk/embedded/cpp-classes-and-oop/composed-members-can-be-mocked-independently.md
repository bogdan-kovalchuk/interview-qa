---
id: emb-cppoop-0036
title: "Композиція чи успадкування: що легше тестувати і чому?"
description: "Композицію з ін’єкцією залежності: компонент-член можна підмінити mock’ом через template-параметр або інтерфейс."
track: embedded
section: cpp-classes-and-oop
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
  - source_id: cpp-core-guidelines-c120
    title: "C++ Core Guidelines: C.120 (class hierarchies)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c120-use-class-hierarchies-to-represent-concepts-with-inherent-hierarchical-structure-only
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Правило C.120: ієрархії класів – лише для понять із внутрішньою ієрархічною структурою; в обґрунтуванні названо «tight coupling of inheritance». Це рекомендація стилю; про тестування в правилі не йдеться."
  - source_id: cpp-core-guidelines-c129
    title: "C++ Core Guidelines: C.129 (implementation vs interface inheritance)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c129-when-designing-a-class-hierarchy-distinguish-between-implementation-inheritance-and-interface-inheritance
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Правило C.129: деталі реалізації в інтерфейсі роблять його крихким, а дані в базовому класі ускладнюють її реалізацію й можуть призводити до дублювання коду; розрізняй implementation inheritance та interface inheritance. Це рекомендація стилю; про тестування в правилі не йдеться."
  - source_id: gmock-for-dummies
    title: "GoogleTest: gMock for Dummies"
    url: https://google.github.io/googletest/gmock_for_dummies.html#a-case-for-mock-turtles
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Описує dependency injection через інтерфейс (клас із virtual-функціями) і mock-клас, що успадковує цей інтерфейс. Не стосується non-virtual залежностей і специфіки embedded."
  - source_id: gmock-cookbook-nonvirtual
    title: "GoogleTest: gMock Cookbook, Mocking Non-virtual Methods"
    url: https://google.github.io/googletest/gmock_cook_book.html#MockingNonVirtualMethods
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Каже, що для non-virtual класів mock – окремий тип без спільної бази, з тими самими сигнатурами методів, а вибір між справжнім класом і mock’ом робиться на етапі компіляції через template-параметр. Про вартість у embedded не йдеться."
---

## Short answer

**Композицію з ін’єкцією залежності: компонент-член можна підмінити mock’ом через template-параметр або інтерфейс.**

Успадкування реалізації тісно зв’язує класи,[^cpp-core-guidelines-c120] а дані в базі її ускладнюють,[^cpp-core-guidelines-c129] тож тест нащадка виконує код бази. Але композиція конкретного типу (`Uart uart_;`) сама mock не дозволяє, а mock, що успадковує чистий інтерфейс, – штатна підміна.[^gmock-for-dummies]

Правило: тестованість дає можливість підмінити залежність, а не композиція як така.

## Detailed explanation

Юніт-тесту потрібен seam – місце, де залежність можна замінити. Візьмемо клас `Led`, що перемикає пін через GPIO. Якщо `Led` тримає конкретний `Gpio gpio_;`, тест змусить виконати справжній код GPIO, а на host-машині це запис у регістри за фіксованою адресою, тобто збій. Композиція стає тестованою, коли залежність передають ззовні: через вказівник чи посилання на інтерфейс або через template-параметр.

gMock документує обидва шляхи. Перший – інтерфейс із virtual-функціями: mock успадковує цей інтерфейс, а код працює з вказівником на нього.[^gmock-for-dummies] Другий – для non-virtual класів: mock є окремим типом без спільної бази, але з тими самими сигнатурами методів, а вибір між справжнім класом і mock’ом робиться на етапі компіляції через template-параметр.[^gmock-cookbook-nonvirtual] В embedded другий варіант зазвичай дешевший: немає vptr і непрямого виклику, а підмінюваний тип відомий під час збірки. Інтерфейс простіший, якщо `virtual` у проєкті вже є, і потрібен, коли об’єкт підміняють у runtime.

Чому з успадкуванням реалізації складніше. Воно створює тісний зв’язок,[^cpp-core-guidelines-c120] а дані в базі ускладнюють її реалізацію й призводять до дублювання коду.[^cpp-core-guidelines-c129] Якщо база торкається регістрів (`volatile` за фіксованою адресою), будь-який тест нащадка виконає цей код, і на host-машині його не запустити без підміни самої бази. Типовий спосіб підміни тут – перевизначити virtual-функції бази в тестовому нащадку, тож `virtual` з’являється лише заради тесту.

Отже, питання «композиція чи успадкування» насправді звучить як «конкретна чи абстрактна залежність». Успадкування від чистого інтерфейсу без даних тестується так само легко, як композиція, – саме так будують mock у gMock.[^gmock-for-dummies] Різниця не в слові «композиція», а в тому, чи залежність абстрактна й передається ззовні. Ін’єкція має ціну: interface дає vptr і непрямий виклик, template – окрему інстанціацію для кожного типу. Про різницю has-a та is-a – `qid:emb-cppoop-0023`.

```cpp
// Ілюстративно: залежність передається ззовні як template-параметр.
template <typename Gpio>
class Led {
public:
    explicit Led(Gpio& gpio) : gpio_(gpio) {}
    void toggle() {
        on_ = !on_;
        gpio_.write(on_);
    }
private:
    Gpio& gpio_;
    bool on_ = false;
};

// У тесті (на host) замість справжнього GPIO – фейк, що запам’ятовує записи.
struct FakeGpio {
    bool last = false;
    int writes = 0;
    void write(bool v) { last = v; ++writes; }
};

// FakeGpio fake; Led<FakeGpio> led{fake}; led.toggle();
// далі перевіряємо: fake.last == true && fake.writes == 1
```

**Типові помилки:**

- Тримати конкретний тип як член (`Uart uart_;`) і вважати це «тестованою композицією»: seam немає.
- Мокати через успадкування від конкретного драйвера з регістровим кодом: тест тягне код і дані бази.[^cpp-core-guidelines-c129]
- Додавати `virtual` лише заради тестів у прошивці, де вистачило б template-параметра.

## Sources

<!-- generated from frontmatter -->
