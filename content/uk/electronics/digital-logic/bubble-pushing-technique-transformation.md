---
id: emb-eldig-0007
title: "Як працює прийом bubble pushing під час графічного перетворення схем?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
---

## Short answer

Проштовхування кружечка інверсії крізь вентиль змінює операцію AND на OR (або навпаки) і розміщує кружечки на всіх виводах іншого боку. Щоб зберегти логічну функцію кола, спершу додають подвійну інверсію <span class="formula">\(\overline{\overline{Z}} = Z\)</span>. Один кружечок проштовхують крізь вентиль, а інший залишають на лінії.[^udemy-electronics-course]

## Detailed explanation

TODO
