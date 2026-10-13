---
id: emb-tmplcx-0009
title: "Що таке full specialization шаблону?"
description: "Повністю інша реалізація для конкретного типу."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
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
  - source_id: cpp-draft-temp-expl-spec
    title: "C++ working draft: Explicit specialization ([temp.expl.spec])"
    url: https://eel.is/c++draft/temp.expl.spec
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що template<> задає explicit specialization, яка для цього набору аргументів використовується замість загального визначення. Оголошення спеціалізації має бути досяжним з кожного використання, що викликало б неявну інстанціацію; інакше програма некоректна без діагностики."
  - source_id: cpp-draft-temp-spec-partial-general
    title: "C++ working draft: Partial specialization, general ([temp.spec.partial.general])"
    url: https://eel.is/c++draft/temp.spec.partial.general
    accessed: 2026-10-13
    kind: spec
    version: "C++ working draft"
    applicability: "Каже, що partial specialization є альтернативним визначенням шаблону, яке використовується замість primary template, коли аргументи збігаються з її патерном. Не описує вибір між кількома відповідними спеціалізаціями."
---

## Question code

```cpp
template<> class SpiDriver<STM32F4> {
  // register layout саме для STM32F4
};
```

## Short answer

**Повністю інша реалізація для конкретного типу.**

Full specialization – це `template<>`-визначення, яке для одного набору аргументів використовується замість primary template.[^cpp-draft-temp-expl-spec] Це дозволяє тримати платформо-залежний код в одному місці замість розкиданих `#ifdef` по всьому проєкту.

Правило: full specialization – для одного конкретного типу чи платформи, коли його реалізація справді відрізняється від загальної.

## Detailed explanation

Шаблон – це опис, за яким компілятор створює клас для кожного набору аргументів. Конструкція `template<>` задає для одного набору власне визначення, і воно використовується замість primary template.[^cpp-draft-temp-expl-spec] Тому спеціалізація – окремий клас: того, чого в ній немає, для цього типу не існує. У прикладі нижче `SpiDriver<Stm32f4>::send` не компілюється, бо `send` є лише в primary template.

Типовий випадок – платформа, де відрізняється сама послідовність дій, наприклад порядок запису в регістри, а не лише одна константа. Спеціалізація для одного типу не змінює інших: `SpiDriver<Stm32g0>` і далі використовує primary template. Водночас зміна загальної логіки не потрапляє в спеціалізацію автоматично, тож правки треба перевіряти в кожній. Якщо потрібна спільна поведінка для цілого сімейства типів, це partial specialization (`qid:emb-tmplcx-0010`): вона використовується замість primary template, коли аргументи збігаються з патерном.[^cpp-draft-temp-spec-partial-general]

```cpp
#include <cstdint>

struct Stm32f4 {};                      // platform tags, illustrative
struct Stm32g0 {};

template <typename Mcu>
struct SpiDriver {                      // primary template: generic code
    static void init() { /* generic sequence */ }
    static void send(std::uint8_t b) { (void)b; }
};

template <>                             // full specialization for one type
struct SpiDriver<Stm32f4> {
    static void init() { /* STM32F4-specific register sequence */ }
    // no send() here: the specialization is a separate definition
};

void use() {
    SpiDriver<Stm32g0>::send(0x55);     // primary template
    SpiDriver<Stm32f4>::init();         // specialization
    // SpiDriver<Stm32f4>::send(0x55);  // error: no member 'send'
}
```

**Типові помилки:**

- Очікувати, що спеціалізація успадкує члени primary template: `SpiDriver<Stm32f4>::send` не існує.
- Оголосити спеціалізацію після того, як для того самого типу вже була неявна інстанціація: оголошення має бути досяжним з кожного такого використання, інакше програма некоректна, і компілятор може не попередити.[^cpp-draft-temp-expl-spec]
- Писати окрему спеціалізацію для кожного MCU, коли відрізняється лише одна константа: тоді зручніше параметр шаблону або `constexpr`-значення в primary template.

## Sources

<!-- generated from frontmatter -->
