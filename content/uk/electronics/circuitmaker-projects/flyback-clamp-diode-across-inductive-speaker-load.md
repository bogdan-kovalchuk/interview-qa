---
id: emb-elcmproj-0042
title: "Чому паралельно до котушки динаміка в однотактному підсилювачі обов’язково вмикають діод?"
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

Котушка динаміка володіє індуктивністю, яка при різкому закриванні транзистора створює зворотний викид напруги: <span class="formula">\(v_L = L\,(di/dt)\)</span>. Високовольтний індуктивний сплеск перевищує допустиму межу <span class="formula">\(V_{CEO}\)</span> транзистора й пробиває перехід. Зворотний діод безпечно закорочує струм котушки на себе, захищаючи кристал.[^udemy-electronics-course]

## Detailed explanation

TODO
