---
id: emb-structs-0041
title: "Trap: how can padding become an information leak?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">Sending or writing raw struct bytes can expose data the program did not intend to transmit through padding.</span>

For example, `send(fd, &msg, sizeof msg)` may include padding bytes between fields. These bytes are not initialized by individual field assignments and may contain fragments of previous variables.

Mitigation: zero-initialize the struct before populating it, serialize fields explicitly, and do not export raw struct layout as a security boundary.[^iso-c-n1570]

## Detailed explanation

TODO
