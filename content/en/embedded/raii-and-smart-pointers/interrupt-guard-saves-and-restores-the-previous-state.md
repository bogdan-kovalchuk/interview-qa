---
id: emb-raii-0006
title: "What does an interrupt-disable RAII guard look like and why is it safe in an ISR?"
track: embedded
section: raii-and-smart-pointers
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: cmsis-core-register-access
    title: "CMSIS-Core (Cortex-M): Core Register Access"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__Core__Register__gr.html
  - source_id: tm4c123-datasheet
    title: "Tiva TM4C123GH6PM Microcontroller Data Sheet (SPMS376E)"
    url: https://www.ti.com/lit/ds/symlink/tm4c123gh6pm.pdf
  - source_id: cpp-draft-stmt-jump
    title: "C++ working draft: Jump statements ([stmt.jump])"
    url: https://eel.is/c++draft/stmt.jump
  - source_id: gcc-extended-asm
    title: "GCC: Extended Asm"
    url: https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html
---

## Short answer

**The ctor saves the current interrupt state and disables interrupts; the dtor restores the saved state instead of enabling interrupts unconditionally.** On Cortex-M this is a read of PRIMASK plus `cpsid i`, with no blocking and no heap,[^cmsis-core-register-access] and PRIMASK is accessible in privileged mode, so in an ISR (Handler mode) the guard works.[^tm4c123-datasheet] Restoring the saved value allows nested sections; while PRIMASK = 1, all exceptions with configurable priority are masked, so keep the section short.[^tm4c123-datasheet]

## Detailed explanation

TODO
