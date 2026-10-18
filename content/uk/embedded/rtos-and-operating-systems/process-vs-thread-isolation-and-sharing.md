---
id: emb-fund-0006
title: "Чим відрізняється процес від потоку?"
track: embedded
section: rtos-and-operating-systems
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**Процес** – окрема запущена програма зі своїм адресним простором, ресурсами ОС, таблицею файлових дескрипторів і мінімум одним потоком.[^dou-embedded-interview] Процеси ізольовані: помилка в одному процесі зазвичай не псує пам'ять іншого.

**Потік (thread)** – одиниця виконання всередині процесу. Потоки одного процесу мають спільну пам'ять, heap, globals і файлові дескриптори, але кожен має власний stack, регістри та instruction pointer.

Наслідок: процеси безпечніше ізольовані, але дорожчі для створення й IPC; потоки легші та швидше обмінюються даними, але потребують синхронізації (`mutex`, `semaphore`, `atomic`) через ризик race condition.

## Detailed explanation

TODO
