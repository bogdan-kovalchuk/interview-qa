---
id: emb-macros-0020
title: "What does MISRA C Rule 20.7 require and why?"
track: embedded
section: inline-and-macros
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: misra-rule-20-7-reference
    title: "MathWorks Polyspace: MISRA C:2012 Rule 20.7"
    url: https://www.mathworks.com/help/bugfinder/ref/misrac2012rule20.7.html
---

## Short answer

**MISRA C Rule 20.7 requires expressions resulting from macro parameter expansion to be parenthesized** to avoid operator precedence errors.

For example, `#define ADD(a,b) a+b` should be rewritten as `#define ADD(a,b) ((a) + (b))`. Otherwise `ADD(1,2) * 3` expands to `1 + 2 * 3`, grouping the expression differently.[^misra-rule-20-7-reference]

Rule 20.7 addresses parentheses in the resulting expression; it is not a general recommendation to use macros instead of functions.[^misra-rule-20-7-reference]

## Detailed explanation

TODO
