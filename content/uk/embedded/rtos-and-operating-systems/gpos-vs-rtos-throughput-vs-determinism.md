---
id: emb-rtos-0005
title: "Яка різниця між ОС загального призначення та ОС реального часу?"
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

**GPOS** (Linux, Windows): оптимізована на throughput, fairness і зручність для багатьох процесів; latency може бути непередбачуваною без спеціальної real-time конфігурації.[^dou-embedded-interview]

**RTOS** (FreeRTOS, Zephyr, VxWorks): оптимізована на **детермінованість** – bounded latency і прогнозований worst-case response за правильно спроєктованих пріоритетів, ISR і critical sections. У preemptive RTOS ready task з вищим пріоритетом витісняє нижчий.

Ключова метрика – **jitter** (розкид часу відгуку). Приклади задач RTOS: керування двигуном, ABS, медичні прилади.

## Detailed explanation

TODO
