---
id: emb-debug-0005
title: "What simple hardware and firmware methods remove noise/bounce on a digital sensor input?"
track: embedded
section: debugging-and-tracing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
---

## Short answer

Hardware: pull-up/pull-down of the correct value, RC filter, Schmitt trigger, shielding/grounding, series resistor, or opto/isolator where needed. Firmware: debounce timer, majority vote, state machine with stable time, interrupt masking over the debounce window. <span class="warn">Do not mask a wiring/grounding problem with a firmware filter if the noise can damage the input or cause a safety event.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
