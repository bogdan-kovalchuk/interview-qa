---
id: emb-elinteg-0028
title: "Чому серіалізація та десеріалізація є критичними операціями в цифрових інтерфейсах передачі даних?"
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

Паралельні шини вимагають окремого фізичного провідника для кожного розряду даних, що збільшує габарити кабелю та схильність до перекосу сигналів. Послідовні інтерфейси (UART, SPI, USB) передають біти по черзі по одній лінії зв'язку. Регістри зсуву перетворюють внутрішні паралельні шини мікропроцесора на послідовний потік на боці передавача та відновлюють байти на приймачі.[^udemy-electronics-course]

## Detailed explanation

TODO
