---
id: emb-fnptr-0021
title: "Why can a dispatch table be better than a large `switch`?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**It stores the opcode -> handler mapping separately from handler implementations** and can simplify adding commands.

In a protocol parser, the table can collect handler selection in one place while each function implements a separate command. This is a structural benefit, not a guarantee of smaller code or faster execution.

For a few branches, `switch` is often easier to read; a table fits when the mapping is data or the command set grows. Measure performance instead of inferring it from syntax.[^iso-c-n1570]

## Detailed explanation

TODO
