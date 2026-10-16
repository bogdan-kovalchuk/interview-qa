---
id: emb-elinteg-0071
title: "Чому для роботи мікросхеми 7493 як повного 4-бітного лічильника необхідно з'єднувати вихід QA із входом CKB?"
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

Мікросхема 7493 внутрішньо розділена на два незалежні функціональні вузли: дільник частоти на 2 на першому тригері (вхід CKA, вихід QA) та 3-розрядний лічильник на 8 (вхід CKB, виходи QB–QD). Якщо не з'єднати QA з CKB ззовні корпусу, мікросхема працюватиме лише як два окремі незв'язані дільники. Зовнішня перемичка утворює повноцінний 4-розрядний лічильник від 0 до 15.[^udemy-electronics-course]

## Detailed explanation

TODO
