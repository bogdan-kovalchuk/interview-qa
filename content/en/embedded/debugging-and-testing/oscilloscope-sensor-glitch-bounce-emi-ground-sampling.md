---
id: emb-debug-0004
title: "Oscilloscope shows a glitch on a sensor 0-1 transition. How to distinguish bounce, EMI, ground issue, and sampling problem?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
---

## Short answer

**Bounce** is usually repetitive and tied to a mechanical edge; EMI may correlate with motor/PWM/radio events. A ground issue shows up as a reference shift, ringing between ground points, or a change with different probe grounding. A sampling problem appears when the analog signal is normal but the firmware catches alias/metastability due to a wrong threshold, debounce, or sample rate.[^dou-embedded-interview]

## Detailed explanation

TODO
