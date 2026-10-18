---
id: emb-rtos-0011
title: "Які scheduler algorithms важливі для RTOS і Linux real-time workloads?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
---

## Short answer

В RTOS типово важливий **fixed-priority preemptive scheduling**, інколи round-robin для tasks одного priority. Для Linux real-time важливі `SCHED_FIFO`, `SCHED_RR`, пріоритетне успадкування (priority inheritance) і PREEMPT_RT поведінка latency. <span class="warn">Алгоритм scheduler треба оцінювати разом з interrupt latency, locks і worst-case execution time.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
