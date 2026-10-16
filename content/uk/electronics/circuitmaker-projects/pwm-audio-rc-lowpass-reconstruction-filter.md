---
id: emb-elcmproj-0062
title: "Навіщо між виводом ШІМ мікроконтролера та аудіопідсилювачем встановлюють фільтр низьких частот?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
---

## Short answer

Прямокутний сигнал ШІМ містить високочастотну несучу складову, яка викликає шуми та перегрів підсилювача. Пасивний фільтр RC із частотою зрізу <span class="formula">\(f_c = 1 / (2\pi R C)\)</span> згладжує імпульси, виділяючи звукову хвилю. На вхід підсилювача надходить відновлений аналоговий сигнал без паразитних високочастотних гармонік.[^udemy-electronics-course]

## Detailed explanation

TODO
