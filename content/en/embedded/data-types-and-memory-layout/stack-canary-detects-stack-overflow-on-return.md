---
id: emb-dtypes-0044
title: "What is a stack canary, and how does it guard against stack overflow?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-stack-protector
    title: "GCC instrumentation options: stack protection"
    url: https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html
---

## Short answer

A stack canary is a guard value that the compiler places in some function frames and checks before returning; its exact placement depends on the ABI and implementation.[^gcc-stack-protector]

If the check detects a change, the runtime takes a failure path; this indicates damage to a protected frame but does not prove that stack overflow was the cause.[^gcc-stack-protector]

GCC can enable protection with `-fstack-protector-strong`; bare-metal requires a compatible runtime and failure handler.[^gcc-stack-protector]

## Detailed explanation

TODO
