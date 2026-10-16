---
id: emb-fnptr-0044
title: "What is a state machine built on function pointers?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: cppreference-pointer
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
---

## Short answer

**It is a table of state handlers or transition handlers** where the current state selects the function to handle an event.

For example: `state = handlers[state](ctx, event);`. This makes each state a separate function and removes a large nested `switch`. For embedded protocol stacks this is often more readable and testable per state handler.

Rule: the state enum must be bounds-checked before indexing into the handler table.[^cppreference-pointer]

## Detailed explanation

TODO
