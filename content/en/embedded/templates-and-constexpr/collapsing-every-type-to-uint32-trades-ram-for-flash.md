---
id: emb-tmplcx-0030
title: "Trap: why is collapsing all types to `uint32_t` to reduce bloat a trade-off?"
track: embedded
section: templates-and-constexpr
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
---

## Short answer

<span class="warn">Fewer instantiations (less Flash), but `uint32_t` wastes RAM on small values.</span>

If a buffer could have been `uint8_t` and you made it `uint32_t` for a single instantiation, you save ROM but quadruple the RAM buffer.

Mitigation: balance the number of instantiations (Flash) against the type width (RAM) for the specific MCU.[^embeddedinterviewlab]

## Detailed explanation

TODO
