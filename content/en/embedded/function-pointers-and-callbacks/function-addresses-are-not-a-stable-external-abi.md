---
id: emb-fnptr-0055
title: "Trap: why should function pointer addresses not be serialised or stored in a Flash config?"
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

<span class="warn">A function pointer value is not a portable, stable identifier.</span>

After a rebuild, link-time optimisation, linker script change or firmware update an address may change. On an MCU with bootloader and application layout it may depend on the slot. A stale value may be invalid or designate different code; C does not define a long-term external storage format for function pointers.[^c11-function-pointers]

Defence: serialise a symbolic ID or opcode, not a function address, and after boot select the handler through the current dispatch table.[^c11-function-pointers]

## Detailed explanation

TODO
