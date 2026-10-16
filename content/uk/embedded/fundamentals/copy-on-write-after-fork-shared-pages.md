---
id: emb-fund-0016
title: "Що таке copy-on-write і де воно проявляється в Linux fork або memory mapping?"
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

**Copy-on-write** дозволяє кільком mappings спільно читати одні physical pages, доки хтось не спробує записати. Після `fork` parent і child спочатку ділять pages, а при write kernel створює приватну копію сторінки. Це економить RAM і пришвидшує fork, але перший write може мати page fault latency.[^dou-embedded-interview]

## Detailed explanation

TODO
