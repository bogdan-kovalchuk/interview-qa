---
id: emb-fnptr-0022
title: "Why should a function pointer table be `static const`?"
description: "At file scope, static const gives internal linkage and makes the elements nonmodifiable; the linker script determines placement."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: arm-cortex-m-startup
    title: "Arm: Decoding the startup file for Arm Cortex-M4"
    url: "https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/decoding-the-startup-file-for-arm-cortex-m4"
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Cortex-M4 example showing read-only section placement is controlled by linker options; this does not universally guarantee that every const object resides in Flash."
---

## Short answer

**At file scope, `static const` gives the table internal linkage and prevents modifying its elements through that object; placement in Flash depends on the toolchain and linker script.**

If the linker script maps a read-only section to Flash, this can save RAM. The table also cannot be accidentally overwritten through this access path.[^arm-cortex-m-startup]

Example: `static const cmd_handler_t handlers[] = { cmd_ping, cmd_reset };`. Check the linker map to confirm the actual section and address.[^arm-cortex-m-startup]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
