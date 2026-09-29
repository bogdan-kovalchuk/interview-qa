---
id: emb-eldig-0007
title: "Як працює прийом bubble pushing під час графічного перетворення схем?"
description: "Як працює прийом bubble pushing під час графічного перетворення схем?"
track: electronics
section: digital-logic
level: junior
type: concept
tags: []
status: published
updated: 2026-09-27
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання й відповіді: створено на основі стенограми лекції 82 курсу на Udemy."
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: цифрова логіка, булева алгебра, логічні вентилі, часові діаграми та цифрові мікросхеми TTL/CMOS."
---

## Short answer

Проштовхування кружечка інверсії крізь вентиль змінює операцію AND на OR (або навпаки) і розміщує кружечки на всіх виводах іншого боку. Щоб зберегти логічну функцію кола, спершу додають подвійну інверсію <span class="formula">\(\overline{\overline{Z}} = Z\)</span>. Один кружечок проштовхують крізь вентиль, а інший залишають на лінії.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
