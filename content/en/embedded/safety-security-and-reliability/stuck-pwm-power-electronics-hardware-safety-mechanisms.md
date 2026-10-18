---
id: emb-safety-0003
title: "Why can a stuck PWM in power electronics be dangerous for hardware and what safety mechanisms should be built in?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
---

## Short answer

A stuck PWM can leave a MOSFET or IGBT in a dangerous duty or open both legs simultaneously, leading to shoot-through, overheating, or load destruction. Required measures: hardware shutdown, dead-time, current and temperature limits, watchdog, timer fault inputs, and safe default state of pins. <span class="warn">Safety must not rely only on the main loop; the critical shutdown mechanism must work even during a firmware hang.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
