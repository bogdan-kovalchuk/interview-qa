---
id: emb-fnptr-0045
title: "Trap: why is a function pointer state machine harder to analyse?"
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

<span class="warn">Indirect calls hide control flow from the reader, the debugger and some static analysers.</span>

Instead of an explicit `switch`, you see only `handlers[state](...)`. If the table is initialised at runtime or modified, it is harder to determine which functions can be called. This can complicate review; a project's rules may separately restrict such calls.

Defence: make tables `static const`, name handlers explicitly, check state bounds and document the transition table.[^iso-c-n1570]

## Detailed explanation

TODO
