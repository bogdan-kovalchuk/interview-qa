---
id: emb-fnptr-0018
title: "What is a dispatch table of function pointers?"
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

**A dispatch table** is an array of function pointers where an index or opcode selects the function to call.

For example, a command parser can have `cmd_handler_t table[256]`, where `table[opcode](ctx, frame)` handles the command. This eliminates a large `switch`, but requires bounds checking and a default handler.

Embedded use cases: CLI commands, protocol opcodes, state machine actions, test command handlers.[^embeddedinterviewlab] [^iso-c-n1570]

## Detailed explanation

TODO
