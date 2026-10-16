---
id: emb-raii-0005
title: "Which pairs of HAL functions are worth wrapping in a scoped handle?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
  - source_id: cmsis-core-register
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
---

## Short answer

**Any acquire/release (init/deinit) pair where the release must happen on every exit path.**

A HAL is a hardware abstraction layer. Examples: interrupt disable/restore, SPI (serial peripheral interface) bus lock, CS (chip select) low -> CS high, GPIO (general-purpose input/output) claim, DMA (direct memory access) channel from a pool. If the resource outlives a single block, the handle should be a move-only owner rather than a local guard.

Rule: wrap paired acquire/release calls of a C API (application programming interface) in an RAII object.[^cppcg-r1-raii]

## Detailed explanation

TODO
