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
  - source_id: iec-61508-1-2010
    title: "IEC 61508-1:2010: Functional safety of electrical/electronic/programmable electronic safety-related systems – Part 1: General requirements"
    url: https://webstore.iec.ch/en/publication/5515
  - source_id: nasa-hdbk-1002
    title: "NASA-HDBK-1002: Fault Management Handbook"
    url: https://ntrs.nasa.gov/api/citations/20120002598/downloads/20120002598.pdf
---

## Short answer

First identify the symptom, constraint and failure mode: timing, noise margin, resource limit, protocol mismatch or requirement gap. Firmware suits sequencing, filtering, diagnostics and policy; hardware – signal integrity, protection, analog limits and deterministic safety cutoff. **System architecture** is needed when the problem arises from a wrong distribution of responsibility between blocks or impossible requirements.[^dou-embedded-interview]

## Detailed explanation

TODO
