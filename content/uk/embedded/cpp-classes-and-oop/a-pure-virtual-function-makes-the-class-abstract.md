---
id: emb-cppoop-0016
title: "Що таке pure virtual функція і abstract клас?"
description: "= 0 робить функцію pure virtual; клас з нею стає abstract і його не можна інстанціювати."
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
  - source_id: cpp-draft-class-abstract
    title: "C++ working draft: Abstract classes ([class.abstract])"
    url: https://eel.is/c++draft/class.abstract
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає pure virtual функцію (pure-specifier) і abstract клас (є pure virtual функція, final overrider якої pure), забороняє об’єкти abstract класу крім підоб’єктів похідних, допускає визначення pure virtual функції для виклику через qualified-id і оголошує UB для virtual-виклику pure функції з constructor-а чи destructor-а того ж об’єкта. Про vptr чи vtable не йдеться."
  - source_id: cpp-draft-class-dtor
    title: "C++ working draft: Destructors ([class.dtor])"
    url: https://eel.is/c++draft/class.dtor
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Пункт 11: деструктор може бути virtual і з pure-specifier; якщо деструктор virtual і в програмі створюються об’єкти цього чи похідного класу, його має бути визначено. Не стосується інтерфейсів без деструктора."
  - source_id: cpp-core-guidelines
    title: "C++ Core Guidelines: C.121 (interface as pure abstract class)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c121-if-a-base-class-is-used-as-an-interface-make-it-a-pure-abstract-class
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Правило C.121: інтерфейс нормально складається лише з public pure virtual функцій і default/порожнього virtual destructor. Це рекомендація стилю, а не вимога мови; про HAL чи embedded не йдеться."
---

## Question code

```cpp
class Sensor {
public:
  virtual int16_t read() = 0;
  virtual ~Sensor() = default;
};
```

## Short answer

**`= 0` робить функцію pure virtual; клас, у якого final overrider хоча б однієї функції pure, є abstract, і об’єкти такого класу можна створювати лише як підоб’єкти похідних.**[^cpp-draft-class-abstract]

Abstract клас задає інтерфейс (контракт) для похідних: похідний клас, що не реалізував усі pure virtual функції, теж лишається abstract.

Правило: abstract base – це C++-спосіб описати інтерфейс драйвера/HAL (hardware abstraction layer); Core Guidelines радять складати такий інтерфейс із pure virtual функцій і virtual destructor.[^cpp-core-guidelines]

## Detailed explanation

Pure virtual функція – це virtual-функція, оголошена в класі з pure-specifier `= 0`. Клас є abstract, якщо в нього є хоча б одна pure virtual функція, final overrider якої pure.[^cpp-draft-class-abstract] Об’єкт такого класу створити не можна, хіба що як підоб’єкт похідного класу; водночас вказівники й посилання на abstract клас цілком допустимі, і саме так його використовують: функція приймає `Sensor&` і не знає, який саме драйвер за нею стоїть.

Звідси випливає механізм «контракту». Похідний клас стає конкретним, лише коли перевизначає всі pure virtual функції; якщо хоч одну пропустив, він сам лишається abstract, і помилка з’явиться в місці створення об’єкта, а не в місці оголошення.[^cpp-draft-class-abstract]

```cpp
// Illustrative
int16_t adc_read_raw();

class Adc : public Sensor {
public:
  int16_t read() override { return adc_read_raw(); }
};

void report(Sensor& s) { (void)s.read(); }  // працює з будь-яким драйвером

// Sensor s;   // помилка: Sensor є abstract
Adc adc;       // добре: read() реалізовано
```

Є кілька тонкощів. Pure virtual функція все одно може мати визначення поза класом, але воно потрібне лише тоді, коли її викликають із qualified-id (`Sensor::read()`).[^cpp-draft-class-abstract] Pure virtual destructor дозволений, проте його тіло обов’язкове: стандарт вимагає визначити virtual destructor, якщо в програмі створюються об’єкти цього чи похідного класу.[^cpp-draft-class-dtor] А virtual-виклик pure функції з constructor-а чи destructor-а для об’єкта, що конструюється чи знищується, – undefined behavior,[^cpp-draft-class-abstract] тому в базовому конструкторі не викликай `read()` напряму чи через допоміжну функцію.

Для embedded абстракція має ціну, як і будь-який polymorphic клас: кожен конкретний похідний об’єкт містить vptr, а його клас – vtable. Core Guidelines радять тримати інтерфейс «чистим» (лише pure virtual функції й virtual destructor, без даних), бо клас без даних стабільніший (менш крихкий).[^cpp-core-guidelines] Коли конкретний тип відомий на етапі компіляції, іноді обирають шаблони замість virtual-інтерфейсу, але це вже компроміс, а не наслідок `= 0`.

**Типові помилки:**

- Вважати, що abstract клас не можна використовувати взагалі: заборонені лише об’єкти, а вказівники й посилання – основний спосіб роботи з інтерфейсом.
- Пропустити одну pure virtual функцію в похідному класі й дивуватися, що його теж не можна створити.
- Викликати pure virtual функцію з конструктора чи деструктора базового класу: це undefined behavior.

## Sources

<!-- generated from frontmatter -->
