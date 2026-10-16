---
id: emb-fnptr-0057
title: "Trap: why can an indirect call through a function pointer be a problem in safety-critical firmware?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: c11-function-pointers
    title: "ISO/IEC 9899:2011 Committee Draft N1570, 6.3.2.3"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">It moves the control-flow decision into data.</span>

If a function pointer is corrupted by memory corruption, an out-of-bounds access or a stack bug, an indirect call may target a function other than the expected one. The impact depends on the architecture, memory and system protections.[^c11-function-pointers]

Defence: keep immutable tables in read-only memory, validate indices and input values, and use MPU or stack protection when the platform supports them.[^c11-function-pointers]

## Detailed explanation

TODO
