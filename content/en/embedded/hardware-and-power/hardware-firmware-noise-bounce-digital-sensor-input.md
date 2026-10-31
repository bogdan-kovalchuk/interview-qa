---
id: emb-debug-0005
title: "What simple hardware and firmware methods remove noise/bounce on a digital sensor input?"
track: embedded
section: hardware-and-power
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
  - source_id: ganssle-debouncing
    title: "Jack Ganssle: A Guide to Debouncing, Part 1 (Wayback Machine copy)"
    url: https://web.archive.org/web/20261003021807/https://www.ganssle.com/debouncing.htm
  - source_id: ganssle-debouncing-part2
    title: "Jack Ganssle: A Guide to Debouncing, Part 2 (Wayback Machine copy)"
    url: https://web.archive.org/web/20260905204217/https://www.ganssle.com/debouncing-pt2.htm
---

## Short answer

Hardware: pull-up/pull-down of the correct value, RC filter, Schmitt trigger, shielding/grounding, series resistor, or opto/isolator where needed. Firmware: debounce timer, majority vote, state machine with stable time, interrupt masking over the debounce window. <span class="warn">Do not mask a wiring/grounding problem with a firmware filter if the noise can damage the input or cause a safety event.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
