---
id: emb-eldig-0009
title: "Чому затримки t_PLH і t_PHL вентиля бувають різними і як це впливає на вибір логіки?"
description: "Чому затримки t_PLH і t_PHL вентиля бувають різними і як це впливає на вибір логіки?"
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

Переходи з низького рівня у високий (t_PLH) та з високого в низький (t_PHL) визначаються різними внутрішніми транзисторами й паразитними ємностями. У серії 74LS вентиль 74LS32 (OR) зазвичай має меншу затримку поширення, ніж 74LS08 (AND). Якщо критичний шлях схеми не вкладається в часовий бюджет, перетворення логіки на швидші вентилі прискорює обчислення.[^udemy-electronics-course]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
