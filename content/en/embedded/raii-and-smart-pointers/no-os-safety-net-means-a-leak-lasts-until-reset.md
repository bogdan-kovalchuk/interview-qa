---
id: emb-raii-0002
title: "Why is RAII critical specifically in embedded?"
description: "Without an OS or garbage collector, a forgotten resource on an MCU can stay occupied until reset, so RAII prevents fatal leaks rather than merely adding convenience."
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
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Describes the CMSIS-RTOS2 mutex API: osMutexAcquire and osMutexRelease (return codes, including osErrorResource when releasing a mutex that was not acquired or is not owned; not callable from an ISR), and the osMutexRecursive and osMutexRobust attributes. A specific RTOS implementation can behave differently outside the specification."
  - source_id: linux-man-exit
    title: "Linux man-pages: _exit(2)"
    url: https://man7.org/linux/man-pages/man2/_exit.2.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "States that _exit() terminates the process and closes all its open file descriptors. Concerns Linux processes; says nothing about bare-metal MCUs or non-file resources."
  - source_id: cmsis-core-register
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Describes __disable_irq, __enable_irq, __get_PRIMASK and __set_PRIMASK: PRIMASK, when set, blocks all exceptions with configurable priority; __disable_irq and __enable_irq run only in privileged mode. The page marks __get_PRIMASK as available only for Armv8-M, so availability on a specific core must be checked in that core's documentation."
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "Paragraph 2: on every transfer of control within a function (including a return from it), automatic block variables active at the source point and not at the destination point are destroyed in reverse order of construction. Does not cover program termination through exit or abort and does not describe exceptions."
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
    accessed: 2026-10-06
    kind: spec
    version: "C++ working draft"
    applicability: "States that std::abort terminates the program without running destructors and that std::exit does not destroy automatic objects; freestanding implementations may not provide these functions."
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Guideline: wrap a resource with paired acquire/release in an object that acquires in the constructor and releases in the destructor; its examples are files, mutexes and memory, not hardware peripherals."
---

## Short answer

**No OS safety net and no garbage collector – a forgotten resource can stay occupied until reset.**

A mutex that a thread did not release is not freed automatically in CMSIS-RTOS2: only a robust mutex is released for you, and only when its owner terminates.[^cmsis-rtos2-mutex] On Linux the kernel closes a process's open file descriptors when it terminates,[^linux-man-exit] while firmware on an MCU is usually a single program with no such cleanup.

Rule: RAII returns the resource on every scope exit, so forgetting the release becomes harder.[^cppcg-r1-raii]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
