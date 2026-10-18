---
id: emb-debug-0005
title: "Які прості hardware і firmware методи прибирають noise/bounce на цифровому вході сенсора?"
track: embedded
section: hardware-and-power
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
---

## Short answer

Hardware: pull-up/pull-down правильного номіналу, RC filter, Schmitt trigger, shielding/grounding, series resistor або opto/isolator за потреби. Firmware: debounce timer, majority vote, state machine з stable time, interrupt masking на debounce window. <span class="warn">Не маскуй firmware-фільтром проблему wiring/grounding, якщо noise може пошкодити input або викликати safety event.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
