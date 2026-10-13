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
updated: 2026-10-13
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-13; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
    accessed: 2026-10-13
    kind: spec
    version: "working draft"
    applicability: "Paragraph 2, note 1: on exit from a scope in any way, including return, automatic objects are destroyed in reverse order of construction, so a guard's destructor runs inside the ISR before it returns. Does not say which actions a destructor may take in an ISR."
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "States that CMSIS-RTOS2 mutex functions cannot be called from interrupt service routines: osMutexRelease returns osErrorISR, and osMutexAcquire also cannot be called from an ISR. Does not describe other RTOSes or destructor behavior."
---

## Question code

```c
void isr() {
  LockGuard lock(m); // dtor викличе release В ISR!
  // ...
}
```

## Short answer

<span class="warn">The destructor runs in the same context as the scope exit, that is inside the ISR (interrupt service routine).</span>[^cpp-draft-stmt-jump]

If the dtor calls an RTOS API that is not allowed in an ISR, such as releasing a mutex, this is invalid in an ISR: CMSIS-RTOS2 forbids `osMutexRelease` from an ISR and returns `osErrorISR`.[^cmsis-rtos2-mutex] The safer option is a guard whose destructor restores the interrupt state without blocking actions.

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
