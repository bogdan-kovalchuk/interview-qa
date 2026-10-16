---
id: emb-fund-0028
title: "How to assess whether a problem should be solved by firmware, hardware design, or system architecture?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

First identify the symptom, constraint and failure mode: timing, noise margin, resource limit, protocol mismatch or requirement gap. Firmware suits sequencing, filtering, diagnostics and policy; hardware – signal integrity, protection, analog limits and deterministic safety cutoff. **System architecture** is needed when the problem arises from a wrong distribution of responsibility between blocks or impossible requirements.[^dou-embedded-interview]

## Detailed explanation

TODO
