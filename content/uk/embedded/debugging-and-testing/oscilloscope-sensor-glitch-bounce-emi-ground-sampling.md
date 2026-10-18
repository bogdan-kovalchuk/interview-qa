---
id: emb-debug-0004
title: "На осцилографі видно заваду на переході сенсора 0-1. Як відрізнити bounce, EMI, ground issue і sampling problem?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
---

## Short answer

**Bounce** зазвичай повторюваний і прив'язаний до механічного edge; EMI може корелювати з motor/PWM/radio events. Ground issue видно як зсув reference, ringing між ground points або зміна при іншому probe grounding. Sampling problem проявляється, коли analog сигнал нормальний, але firmware ловить alias/metastability через неправильний threshold, debounce або sample rate.[^dou-embedded-interview]

## Detailed explanation

TODO
