---
id: emb-elintro-0274
title: "Чому перед живленням нової схеми корисно виставити current limit?"
description: "Чому перед живленням нової схеми корисно виставити current limit?"
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 24, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: keysight-current-limit
    title: "Keysight: Protect Your Device Against High Power"
    url: https://www.keysight.com/blogs/en/tech/bench/2022/03/02/protect-your-device-against-high-power
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Пояснює перехід джерела у constant-current після досягнення current limit; межі захисту залежать від моделі."

---

## Short answer

Якщо є помилка монтажу або коротке замикання, блок живлення перейде в `CC` і обмежить струм. Це часто рятує компоненти, доріжки, дроти й сам блок живлення.[^keysight-current-limit]

## Detailed explanation

Current limit корисно встановити перед першим увімкненням нової схеми, оскільки він обмежує струм, який лабораторне джерело віддає навантаженню. У режимі constant-voltage джерело підтримує задану напругу, доки струм не досягне межі; тоді воно може перейти в режим constant-current, утримувати струм на межі й зменшувати вихідну напругу.[^keysight-current-limit]

Якщо монтаж містить коротке замикання або компонент встановлено неправильно, обмеження може зменшити струм і розсіювану потужність у частині несправних кіл. Воно не гарантує, що компонент не пошкодиться: навіть обмежений струм може бути завеликим для тонкої доріжки чи мікросхеми, а реакція джерела має скінченний час. Межу вибирають за очікуваним споживанням і допустимим струмом найслабшої частини схеми, а не навмання.[^keysight-current-limit]

Current limit не тотожний захисту від перенапруги або аварійному відключенню за струмом. У багатьох джерелах досягнення межі переводить вихід у CC, але окрема функція overcurrent protection може вимкнути вихід; поведінка залежить від моделі й налаштувань.[^keysight-current-limit]

Приклад: якщо плата має споживати близько 100 mA, для першого ввімкнення задають межу трохи вище очікуваного пускового струму, але нижче небезпечного рівня для плати. Якщо джерело відразу показує CC і напруга падає, живлення вимикають і шукають замикання замість того, щоб навмання підвищувати межу.

**Типові помилки:**

- Вважати current limit миттєвим запобіжником або повним захистом плати.
- Встановити межу нижче нормального пускового струму.
- Не перевірити вихідну напругу й полярність.

## Sources

<!-- generated from frontmatter -->
