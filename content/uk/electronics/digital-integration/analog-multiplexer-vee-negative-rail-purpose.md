---
id: emb-elinteg-0020
title: "Навіщо в аналоговому мультиплексорі 74HC4051 передбачено окремий вивід живлення VEE?"
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

Вивід VEE є негативною шиною живлення внутрішніх аналогових ключів і дозволяє комутувати двополярні аналогові сигнали (наприклад, аудіо). Напруга аналогового сигналу може змінюватися в діапазоні від VEE до VCC, тоді як цифрове керування здійснюється відносно GND. Якщо комутуються лише однополярні позитивні напруги, вивід VEE з'єднують із землею GND.[^udemy-electronics-course]

## Detailed explanation

TODO
