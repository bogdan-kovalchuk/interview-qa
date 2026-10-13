---
id: emb-raii-0023
title: "Чому custom deleter варто робити stateless?"
description: "Stateless deleter type (лямбда без capture або empty functor) може не займати місця в unique_ptr завдяки empty base optimization."
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
  - source_id: cpp-draft-unique-ptr-single
    title: "C++ working draft: unique_ptr for single objects ([unique.ptr.single])"
    url: https://eel.is/c++draft/unique.ptr.single
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Визначає, що unique_ptr зберігає вказівник і deleter, а його деструктор викликає deleter лише для ненульового вказівника; copy-операції видалені, move дозволені. Розміру об’єкта не задає."
  - source_id: cpp-draft-intro-object
    title: "C++ working draft: Object model ([intro.object])"
    url: https://eel.is/c++draft/intro.object
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що нульовий розмір має base-підоб’єкт standard-layout класу без нестатичних даних, а в інших випадках обставини нульового розміру визначає реалізація. Конкретних значень sizeof не задає."
  - source_id: itanium-cxx-abi
    title: "Itanium C++ ABI"
    url: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Розкладка класів: порожня база спершу розміщується на зміщенні нуль, якщо це можливо. Це ABI, а не стандарт C++; вендорські тулчейни й інші платформи можуть відрізнятися."
---

## Short answer

**Stateless deleter type (лямбда без capture або empty functor) може не займати місця в `unique_ptr` завдяки empty base optimization.**

Лямбда з capture несе стан і має ненульовий розмір, тож збільшує `unique_ptr`.[^cpp-draft-intro-object] Function pointer deleter не має стану класу, але його значення треба зберігати поруч із вказівником, тому розмір зазвичай стає два вказівники.[^cpp-draft-unique-ptr-single]

Правило: deleter без runtime state -> `unique_ptr` може лишатися завбільшки з сирий вказівник; function pointer deleter простий, але не безрозмірний.[^itanium-cxx-abi]

## Detailed explanation

`unique_ptr` зберігає не лише вказівник, а й deleter. Стандарт описує конструювання так, що зберігаються і вказівник, і deleter, а деструктор викликає deleter лише для ненульового вказівника.[^cpp-draft-unique-ptr-single] Отже розмір `unique_ptr` складається з вказівника і deleter-а, якщо порожній deleter не розміщується як база без байтів. Стандарт дозволяє нульовий розмір для base-підоб’єкта standard-layout класу без нестатичних даних; в інших випадках обставини нульового розміру визначає реалізація.[^cpp-draft-intro-object]

Порожній deleter можна розмістити як порожню базу. На практиці (GCC, Clang) closure-тип лямбди без capture порожній і standard-layout, хоча стандарт дозволяє реалізації змінити його розмір і standard-layout-ність, тож перевіряй `sizeof`.[^cpp-draft-intro-object] Itanium C++ ABI спершу пробує розмістити порожню базу на зміщенні нуль, тому на таких платформах порожній deleter зазвичай не додає байтів.[^itanium-cxx-abi] Лямбда з capture має нестатичний член, тобто ненульовий розмір, і цей розмір додається до розміру `unique_ptr`.

```cpp
// Illustrative: SpiHandle, open_spi, spi_disable, spi_disable_on and Bus are driver types and functions.
void f(Bus& bus) {
    // Stateless: the closure has no data members, so it can be an empty base.
    auto close_spi = [](SpiHandle* h) { spi_disable(h); };
    std::unique_ptr<SpiHandle, decltype(close_spi)> spi(open_spi(), close_spi);

    // Capturing: the closure stores a reference, so it has nonzero size.
    auto close_spi_ctx = [&bus](SpiHandle* h) { spi_disable_on(bus, h); };
    std::unique_ptr<SpiHandle, decltype(close_spi_ctx)> spi2(open_spi(), close_spi_ctx);
}
```

На MCU зайві байти важливі тоді, коли таких обгорток багато, наприклад по одній на кожен периферійний хендл. Але розмір не переносимий: він залежить від STL, ABI і типу deleter-а, тож вимірюйте `sizeof` на цільовому тулчейні.

Stateless не означає безпечний. Якщо виклик deleter-а кидає виняток, це undefined behavior.[^cpp-draft-unique-ptr-single] Тому deleter не має кидати виняток. Якщо йому потрібен контекст, що передається через capture, він стає stateful і розмір зростає; тоді варто порівняти, чи вигода від контексту виправдовує байти.

**Типові помилки:**

- Захоплювати хендл або шину в лямбді-deleter і очікувати, що розмір `unique_ptr` лишиться як у сирого вказівника.
- Вважати розмір однаковим на всіх платформах: обставини нульового розміру визначає реалізація.[^cpp-draft-intro-object]
- Писати deleter, який може кинути виняток: тоді це undefined behavior.

## Sources

<!-- generated from frontmatter -->
