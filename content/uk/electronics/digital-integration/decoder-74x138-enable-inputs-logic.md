---
id: emb-elinteg-0004
title: "Навіщо дешифратор 74x138 має три входи дозволу різної полярності?"
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

Мікросхема 74x138 має два активні низькі входи <span class="formula">\(\overline{E_1}\)</span>, <span class="formula">\(\overline{E_2}\)</span> та один активний високий вхід <span class="formula">\(E_3\)</span>. Дешифрація відбувається лише тоді, коли одночасно подано <span class="formula">\(\overline{E_1}=0\)</span>, <span class="formula">\(\overline{E_2}=0\)</span> і <span class="formula">\(E_3=1\)</span>. Різна полярність дозволів уможливлює легке каскадування дешифраторів або дешифрацію адрес пам'яті без використання зовнішніх логічних вентилів.[^udemy-electronics-course]

## Detailed explanation

TODO
