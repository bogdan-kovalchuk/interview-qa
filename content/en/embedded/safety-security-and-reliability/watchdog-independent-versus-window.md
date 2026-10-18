---
id: emb-safety-0001
title: "What watchdog functions exist, and how does an independent watchdog differ from a window watchdog?"
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

A watchdog resets the system if firmware does not perform a refresh in time. **Independent watchdog** typically has a separate low-speed clock and works even during main clock problems. **Window watchdog** requires a refresh neither too early nor too late, so it catches both hangs and runaway loops.[^dou-embedded-interview]

## Detailed explanation

TODO
