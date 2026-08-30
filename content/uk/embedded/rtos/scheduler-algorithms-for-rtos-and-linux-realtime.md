---
id: emb-rtos-0011
title: "Які scheduler algorithms важливі для RTOS і Linux real-time workloads?"
description: "RTOS часто використовує fixed-priority preemptive scheduling, а Linux real-time workloads спираються на SCHED_FIFO, SCHED_RR та PREEMPT_RT."
track: embedded
section: rtos
level: senior
type: concept
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
---

## Short answer

В RTOS типово важливий <span class="key">fixed-priority preemptive scheduling</span>, інколи round-robin для tasks одного priority.<br>Для Linux real-time важливі <code>SCHED_FIFO</code>, <code>SCHED_RR</code>, priority inheritance і PREEMPT_RT поведінка latency.<br><span class="warn">Алгоритм scheduler треба оцінювати разом з interrupt latency, locks і worst-case execution time.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
