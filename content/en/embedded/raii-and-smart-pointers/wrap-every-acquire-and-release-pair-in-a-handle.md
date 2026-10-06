---
id: emb-raii-0005
title: "Which pairs of HAL functions are worth wrapping in a scoped handle?"
description: "Any acquire/release or init/deinit pair from a HAL, such as interrupt disable/restore, SPI bus lock, chip select, GPIO claim, or DMA channel, is a candidate for a scoped RAII handle."
track: embedded
section: raii-and-smart-pointers
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: wrap a resource with paired acquire/release in an object that acquires in the constructor and releases in the destructor; its examples are files, mutexes and memory, not hardware peripherals."
  - source_id: cmsis-core-register
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Describes __disable_irq and __enable_irq (set and clear PRIMASK; privileged mode only), __get_PRIMASK and __set_PRIMASK (read and write PRIMASK); PRIMASK, when set, blocks all exceptions with configurable priority. The page marks __get_PRIMASK as available only for Armv8-M, so availability on a specific core must be checked in that core's documentation."
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Describes the CMSIS-RTOS2 mutex API: osMutexAcquire and osMutexRelease; these calls are not available from an ISR. A specific RTOS implementation can behave differently outside the specification."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 2: on every transfer of control within a function (including a return from it), automatic block variables active at the source point and not at the destination point are destroyed in reverse order of construction. Does not cover program termination through exit or abort and does not describe exceptions."
---

## Short answer

**Any acquire/release (init/deinit) pair where the release must happen on every exit path.**

A HAL is a hardware abstraction layer. Examples: interrupt disable/restore, SPI (serial peripheral interface) bus lock, CS (chip select) low -> CS high, GPIO (general-purpose input/output) claim, DMA (direct memory access) channel from a pool. If the resource outlives a single block, the handle should be a move-only owner rather than a local guard.

Rule: wrap paired acquire/release calls of a C API (application programming interface) in an RAII object.[^cppcg-r1-raii]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
