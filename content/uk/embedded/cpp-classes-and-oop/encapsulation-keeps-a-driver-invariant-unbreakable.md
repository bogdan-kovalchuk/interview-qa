---
id: emb-cppoop-0033
title: "Що таке encapsulation і яку гарантію він дає в драйвері?"
description: "Приховування внутрішнього стану за публічним інтерфейсом, щоб invariant класу підтримували лише його власні операції."
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
  - source_id: cpp-draft-class-access-general
    title: "C++ working draft: Member access control, general ([class.access.general])"
    url: https://eel.is/c++draft/class.access.general
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що private-член можна назвати лише в членах і friends класу, що контроль доступу стосується можливості назвати член, і що конструкція, яка використовує недоступний член, ill-formed. Це правило мови про імена, а не захист пам’яті чи апаратури; про вартість у runtime нічого не каже."
  - source_id: cpp-core-guidelines-c2
    title: "C++ Core Guidelines: C.2 (class or struct, invariant)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c2-use-class-if-the-class-has-an-invariant-use-struct-if-the-data-members-can-vary-independently
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Правило C.2 і примітка до нього: invariant – логічна умова над членами об’єкта, яку має встановити constructor, щоб public-функції могли на неї покладатися; якщо члени змінюються незалежно, invariant неможливий. Це конвенція стилю, а не вимога мови."
  - source_id: cpp-core-guidelines-c9
    title: "C++ Core Guidelines: C.9 (minimize exposure of members)"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#c9-minimize-exposure-of-members
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Правило C.9: щоб забезпечити зв’язок (invariant) між членами, їх роблять private і підтримують цей зв’язок через constructors і member-функції; приховування зменшує шанс ненавмисного доступу. Це рекомендація стилю, а не вимога мови; про runtime-вартість не йдеться."
  - source_id: gcc-optimize-options
    title: "GCC 16.1.0: Optimize Options"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Optimize-Options.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Документує, що без оптимізації GCC не розгортає функції inline (-fno-inline за замовчуванням), що -finline-small-functions вмикається на -O2, -O3 і -Os, і що -flto дозволяє інлайнити між об’єктними файлами; конкретні рішення евристик залежать від коду."
---

## Short answer

**Приховування внутрішнього стану за публічним інтерфейсом**, щоб invariant класу підтримували лише його власні операції.

Драйвер тримає регістри й буфери `private` і відкриває лише валідовані операції; код поза класом не може назвати такі члени, тож не обійде перевірки.[^cpp-draft-class-access-general] Це правило мови, а не захист пам’яті: `friend`, приведення типів чи прямий запис за адресою його обходять.

Правило: це compile-time перевірка, тому в runtime вона зазвичай нічого не додає; ціну мають лише перевірки, які ти пишеш сам.

## Detailed explanation

Encapsulation – це об’єднання даних з операціями над ними й приховування представлення, щоб лише ці операції могли змінювати стан. Сенс він має тоді, коли в класу є invariant: логічна умова над членами, яку встановлює constructor і яку зберігає кожна public-функція.[^cpp-core-guidelines-c2] Якщо члени можуть змінюватися незалежно один від одного, invariant немає, і `struct` з public-даними чесніший. Щоб умова між членами справді трималася, члени роблять `private`, а її підтримують constructor і member-функції.[^cpp-core-guidelines-c9]

У драйвері UART кільцевий буфер має invariant `head_ < N` і `count_ <= N`. Якби ці поля були public, будь-який код (інший модуль, ISR) міг би записати `head_ = 99`, і наступний `pop()` прочитав би `data_[99]` за межами масиву (а зіпсований `count_` змусив би `pop()` віддавати байти, яких `push()` не клав). Коли поля `private`, змінити їх можуть лише `push()` і `pop()`, а перевірка меж лежить в одному місці. Гарантія мови вузька: `private`-член можна назвати лише в членах і `friend`-ах класу, а конструкція, що звертається до недоступного члена, ill-formed, тобто компілятор її відхиляє.[^cpp-draft-class-access-general] Порушення стає помилкою компіляції, а не плаваючим багом на стенді.

Проте це контроль імен, а не захист пам’яті. `friend`, приведення вказівника на об’єкт, `memcpy` поверх нього чи запис за адресою регістра access control не зупиняє. Метод сам не стає безпечним для переривань: якщо `push()` викликають і з ISR, і з main-циклу, потрібен окремий захист (critical section чи lock-free дизайн). Тож encapsulation гарантує лише, що код поза класом не змінить стан повз його операції, поки дотримується правил мови.

Специфікатори доступу перевіряє компілятор, у машинному коді їх немає, тому самі по собі вони не мають додавати ні даних, ні інструкцій. Ціну мають лише перевірки, які ти пишеш в операціях, і виклики, які компілятор не інлайнить (без оптимізації GCC не інлайнить функції, а між translation units це можливо лише з LTO;[^gcc-optimize-options] див. `qid:emb-cppoop-0001`). Конкретний приклад для GPIO-регістра – `qid:emb-cppoop-0004`.

```cpp
#include <cstddef>
#include <cstdint>

// Ілюстративно: invariant (head_ < N, count_ <= N) підтримують лише методи.
template <std::size_t N>
class RxBuffer {
public:
    bool push(std::uint8_t byte) {
        if (count_ == N) { return false; }      // межі перевіряються в одному місці
        data_[(head_ + count_) % N] = byte;
        ++count_;
        return true;
    }
    bool pop(std::uint8_t& out) {
        if (count_ == 0) { return false; }
        out = data_[head_];
        head_ = (head_ + 1) % N;
        --count_;
        return true;
    }
private:
    std::uint8_t data_[N]{};
    std::size_t head_ = 0;
    std::size_t count_ = 0;
};
```

**Типові помилки:**

- Робити `private` поле з public getter і setter на кожне: формально це encapsulation, але invariant між полями знову нічим не захищений.
- Вважати `private` захистом від ISR, DMA чи коду, що пише за адресою: це лише правило мови, синхронізацію воно не дає.
- Додавати `virtual` до інтерфейсу драйвера «для чистоти»: encapsulation цього не вимагає, а `virtual` додає vptr і непрямий виклик.
- Очікувати, що getter завжди «безкоштовний»: на `-O0` або між translation units без LTO компілятор його не інлайнить, і лишається звичайний call.[^gcc-optimize-options]

## Sources

<!-- generated from frontmatter -->
