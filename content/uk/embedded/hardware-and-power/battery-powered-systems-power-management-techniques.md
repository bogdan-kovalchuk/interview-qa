---
id: emb-power-0001
title: "Які типові методи керування живленням використовуються в embedded-системах з батарейним живленням?"
track: embedded
section: hardware-and-power
sources:
  - source_id: arm-cortex-m-low-power
    title: "ARM: Cortex-M Low Power Design"
    url: https://developer.arm.com/documentation/102499/0100/
---

## Short answer

**Знижуйте середнє споживання через duty cycling: групуйте корисну роботу, прокидайтеся за потрібною подією або таймером і повертайтеся у доречний sleep state.** Вимикайте тактування невикористаної периферії, застосовуйте power gating, якщо його підтримує hardware, а частоту й напругу знижуйте лише в дозволених operating points.[^arm-cortex-m-low-power] Час роботи radio та sensor, quiescent current регуляторів і leakage можуть бути важливішими за час CPU. Найглибший sleep state не завжди найкращий: враховуйте енергію й latency пробудження, retention state, запуск clock і real-time deadlines.

## Detailed explanation

TODO
