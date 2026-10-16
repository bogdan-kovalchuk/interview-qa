---
id: emb-raii-0002
title: "Why is RAII critical specifically in embedded?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
  - source_id: linux-man-exit
    title: "Linux man-pages: _exit(2)"
    url: https://man7.org/linux/man-pages/man2/_exit.2.html
  - source_id: cmsis-core-register
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
  - source_id: cpp-draft-stmt-dcl
    title: "C++ working draft: Declaration statement ([stmt.dcl])"
    url: https://eel.is/c++draft/stmt.dcl
  - source_id: cpp-draft-support-start-term
    title: "C++ working draft: Start and termination ([support.start.term])"
    url: https://eel.is/c++draft/support.start.term
  - source_id: cppcg-r1-raii
    title: "C++ Core Guidelines: R.1 – Manage resources automatically using resource handles and RAII"
    url: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r1-manage-resources-automatically-using-resource-handles-and-raii-resource-acquisition-is-initialization
---

## Short answer

**No OS safety net and no garbage collector – a forgotten resource can stay occupied until reset.**

A mutex that a thread did not release is not freed automatically in CMSIS-RTOS2: only a robust mutex is released for you, and only when its owner terminates.[^cmsis-rtos2-mutex] On Linux the kernel closes a process's open file descriptors when it terminates,[^linux-man-exit] while firmware on an MCU is usually a single program with no such cleanup.

Rule: RAII returns the resource on every scope exit, so forgetting the release becomes harder.[^cppcg-r1-raii]

## Detailed explanation

TODO
