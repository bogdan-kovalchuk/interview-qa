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
  - source_id: ti-slpa005-ringing
    title: "TI SLPA005: Reducing Ringing Through PCB Layout Techniques"
    url: https://www.ti.com/lit/an/slpa005/slpa005.pdf
  - source_id: ti-scba004-slow-inputs
    title: "TI SCBA004: Implications of Slow or Floating CMOS Inputs"
    url: https://www.ti.com/lit/an/scba004/scba004.pdf
  - source_id: ti-scea046-schmitt
    title: "TI SCEA046: Understanding Schmitt Triggers"
    url: https://www.ti.com/lit/an/scea046/scea046.pdf
  - source_id: ti-sdya006-metastability
    title: "TI SDYA006: Metastable Response in 5-V Logic Circuits"
    url: https://www.ti.com/lit/an/sdya006/sdya006.pdf
---

## Short answer

**Bounce** is usually repetitive and tied to a mechanical edge; EMI may correlate with motor/PWM/radio events. A ground issue shows up as a reference shift, ringing between ground points, or a change with different probe grounding. A sampling problem appears when the analog signal is normal but the firmware catches alias/metastability due to a wrong threshold, debounce, or sample rate.[^dou-embedded-interview]

## Detailed explanation

TODO
