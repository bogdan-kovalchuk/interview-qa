---
id: emb-tmplcx-0020
title: "Як шаблони дають type-safe фізичні одиниці?"
description: "Одиниця закодована в тип – змішати несумісні величини не можна (compile error)."
track: embedded
section: templates-and-constexpr
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання і відповіді; відповідь незалежно не перевірена."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C++; freestanding і вендорські тулчейни можуть відрізнятися."
---

## Short answer

```cpp
template<typename Unit, typename Rep = int32_t>
struct Quantity { Rep value; };
using Millivolt = Quantity<MillivoltTag>;
using Milliamp  = Quantity<MilliampTag>;
```

**Одиниця закодована в тип – змішати несумісні величини не можна (compile error).**

`set_led_current(read_battery())` не скомпілюється (Millivolt ≠ Milliamp). При цьому `Quantity` має розмір як `int32_t`: tag-типи існують лише на етапі компіляції й повністю оптимізуються.

Правило: type-safe одиниці дають compile-time перевірку без додаткових runtime-полів; згадай крах Mars Climate Orbiter (фунт-секунди vs ньютон-секунди).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
