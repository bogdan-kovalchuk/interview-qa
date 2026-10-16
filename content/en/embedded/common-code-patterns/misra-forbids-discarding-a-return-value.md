---
id: emb-patterns-0022
title: "What does MISRA C require when code does not use a function's return value?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: misra-c-2023-rule-17-7
    title: "MISRA C:2023 Addendum 2"
    url: https://misra.org.uk/app/uploads/2024/10/MISRA-C-2023-ADD2.pdf
---

## Short answer

**MISRA C Rule 17.7 requires using a non-void function's value or explicitly discarding it with a cast to `void`.** This does not mean every function that can fail must return an error code.[^misra-c-2023-rule-17-7]

The rule concerns use of the returned value, not one required error-handling pattern: status may be returned separately, in a result structure, or the contract may establish that failure is impossible. The project must define and check the appropriate response to meaningful outcomes.

An explicit `(void)call()` marks deliberate discarding, but does not replace risk analysis.[^misra-c-2023-rule-17-7]

## Detailed explanation

TODO
