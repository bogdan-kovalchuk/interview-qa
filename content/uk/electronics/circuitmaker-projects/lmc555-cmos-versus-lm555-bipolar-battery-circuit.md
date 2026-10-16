---
id: emb-elcmproj-0011
title: "Чому для батарейних пристроїв обирають КМОН-таймер LMC555 замість класичного біполярного LM555?"
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

КМОН-таймер LMC555 зберігає працездатність за низької напруги від <span class="formula">\(1{,}5\ \text{В}\)</span> і споживає частки міліампера струму. Він позбавлений наскрізних струмових викидів під час перемикання внутрішніх транзисторів вихідного каскаду. Це захищає шину живлення від високочастотних шумів і продовжує ресурс батарейного живлення.[^udemy-electronics-course]

## Detailed explanation

TODO
