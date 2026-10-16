---
id: emb-fnptr-0022
title: "Why should a function pointer table be `static const`?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-cortex-m-startup
    title: "Arm: Decoding the startup file for Arm Cortex-M4"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4
---

## Short answer

**At file scope, `static const` gives the table internal linkage and prevents modifying its elements through that object; placement in Flash depends on the toolchain and linker script.**

If the linker script maps a read-only section to Flash, this can save RAM. The table also cannot be accidentally overwritten through this access path.[^arm-cortex-m-startup]

Example: `static const cmd_handler_t handlers[] = { cmd_ping, cmd_reset };`. Check the linker map to confirm the actual section and address.[^arm-cortex-m-startup]

## Detailed explanation

TODO
