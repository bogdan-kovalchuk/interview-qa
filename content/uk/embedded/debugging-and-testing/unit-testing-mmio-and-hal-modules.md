---
id: emb-testemb-0006
title: "Як написати unit test для модуля, який працює з MMIO-регістрами або HAL-драйвером?"
track: embedded
section: debugging-and-testing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
---

## Short answer

Винеси доступ до регістрів/HAL за тонкий interface або fake register block, а бізнес-логіку тестуй на host. У тесті перевіряй, які bits записані, у якій послідовності, як обробляються flags, timeout і помилки. <span class="warn">Не тестуй реальний MMIO pointer на host напряму; заміни `volatile` register access контрольованим fake/shim шаром.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
