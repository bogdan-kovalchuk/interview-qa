---
id: emb-cppfound-0059
title: "Can pointers be compared with `<` and `>`, and when is this defined behavior?"
track: embedded
section: pointers-and-arrays
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Comparisons `==` and `!=` are always **defined** between any two pointers of the same type.

Comparisons `<`, `>`, `<=`, `>=` are **defined only** if both pointers point to the **same array** (or struct). Comparing pointers to different objects -> <span class="warn">undefined behavior per the standard</span>.

In practice: most platforms give a correct answer even for different objects, but do not rely on this in portable code.[^embeddedinterviewlab]

## Detailed explanation

TODO
