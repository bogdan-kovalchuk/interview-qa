---
id: emb-raii-0018
title: "Trap: what makes an RAII destructor inside an ISR dangerous?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements, general ([stmt.jump.general])"
    url: https://eel.is/c++draft/stmt.jump.general
  - source_id: cmsis-rtos2-mutex
    title: "CMSIS-RTOS2: Mutex Management"
    url: https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__MutexMgmt.html
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
