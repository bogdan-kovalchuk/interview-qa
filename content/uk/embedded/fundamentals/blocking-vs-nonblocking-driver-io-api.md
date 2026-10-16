---
id: emb-fund-0013
title: "Чим блокуючі операції відрізняються від неблокуючих у драйверах і I/O API?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Blocking call засинає або чекає, поки data/resource стане доступним, наприклад `read` з порожнього device queue. Non-blocking call одразу повертає `EAGAIN`/`EWOULDBLOCK`, якщо операцію не можна виконати. У драйверах це впливає на wait queues, poll/select/epoll support, timeout-и й те, чи можна викликати API з конкретного context.[^dou-embedded-interview]

## Detailed explanation

TODO
