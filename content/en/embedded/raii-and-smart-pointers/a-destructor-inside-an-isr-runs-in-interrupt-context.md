---
id: emb-raii-0018
title: "Trap: what makes an RAII destructor inside an ISR dangerous?"
description: "The destructor runs in the same context as the scope exit, that is inside the ISR."
track: embedded
section: raii-and-smart-pointers
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Question code

```c
void isr() {
  LockGuard lock(m); // dtor викличе release В ISR!
  // ...
}
```

## Short answer

<span class="warn">The destructor runs in the same context as the scope exit, that is inside the ISR (interrupt service routine).</span>

If the dtor performs a blocking operation (mutex release from an RTOS, allocation, UART TX), this is unacceptable in an interrupt: deadlock or jitter.

Defense: in ISR RAII, only register-level actions are allowed (interrupt enable/disable), no blocking teardown.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
