---
id: emb-safety-0001
title: "Які функції watchdog бувають і чим independent watchdog відрізняється від window watchdog?"
track: embedded
section: safety-security-and-reliability
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010 ? Functional safety: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
---

## Short answer

Watchdog скидає систему, якщо firmware не виконує refresh у правильний час. **Independent watchdog** зазвичай має окремий low-speed clock і працює навіть при проблемах main clock. **Window watchdog** вимагає refresh не надто рано й не надто пізно, тому ловить як зависання, так і runaway loop.[^dou-embedded-interview]

## Detailed explanation

TODO
