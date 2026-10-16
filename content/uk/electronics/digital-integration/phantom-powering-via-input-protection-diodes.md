---
id: emb-elinteg-0032
title: "Що таке паразитна заживка (phantom powering) через вхідні діоди захисту і чим вона небезпечна?"
track: electronics
section: digital-integration
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Входи цифрових мікросхем містять внутрішні ESD-діоди захисту, підключені катодами до шини VCC. Якщо подати активний сигнал на вхід незаживленої мікросхеми, струм потече через діод у шину живлення, частково живлячи схему. Це утримує тригери в напівробочому стані, блокує штатне початкове скидання при ввімкненні та може пошкодити вхідний захист.[^udemy-electronics-course]

## Detailed explanation

TODO
