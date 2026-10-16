---
id: emb-patterns-0039
title: "Why do guard clauses speed up an audit of safety-critical code?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: holzmann-power-of-ten
    title: "The Power of Ten – Rules for Developing Safety Critical Code (G. J. Holzmann, NASA/JPL)"
    url: https://spinroot.com/gerard/pdf/P10.pdf
---

## Short answer

**Guard clauses move the input checks (null, range, state, permissions) into the first lines of the function, so the contract is visible at once and the main logic runs without nested `if`.**

A reviewer can more easily confirm that dangerous inputs are rejected before any side effect, and the JPL guidelines for safety-critical code require parameter validity to be checked inside each function.[^holzmann-power-of-ten] This does not prove correctness: a `NULL` check will not catch a bad non-null pointer, and a faster audit is a consequence of readability, not a guarantee.[^iso-c-n1570]

## Detailed explanation

TODO
