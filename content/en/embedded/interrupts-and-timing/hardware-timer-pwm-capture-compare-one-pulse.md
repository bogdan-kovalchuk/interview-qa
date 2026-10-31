---
id: emb-irq-0011
title: "How do hardware timers work in PWM, input capture, output compare, and one-pulse modes?"
track: embedded
section: interrupts-and-timing
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
  - source_id: stm32f4-hal-tim
    title: "STMicroelectronics STM32F4 HAL: stm32f4xx_hal_tim.c (TIM driver)"
    url: https://github.com/STMicroelectronics/stm32f4xx-hal-driver/blob/master/Src/stm32f4xx_hal_tim.c
  - source_id: stm32f4-hal-tim-h
    title: "STMicroelectronics STM32F4 HAL: stm32f4xx_hal_tim.h (TIM definitions)"
    url: https://github.com/STMicroelectronics/stm32f4xx-hal-driver/blob/master/Inc/stm32f4xx_hal_tim.h
---

## Short answer

In **PWM** mode, the timer counts the period and compares the counter against a duty value to drive an output pin. **Input capture** latches the counter on an external edge to measure signal timing, while **output compare** generates an event or toggles a pin on match. **One-pulse** mode generates a single pulse of a defined duration after a trigger.[^dou-embedded-interview]

## Detailed explanation

TODO
