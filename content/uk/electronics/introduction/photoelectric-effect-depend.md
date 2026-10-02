---
id: emb-elintro-0069
title: "Що таке фотоелектричний ефект і від чого він залежить?"
description: "Що таке фотоелектричний ефект і від чого він залежить?"
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
    applicability: "Походження питання: лекція 8, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: openstax-photoelectric
    title: "OpenStax University Physics Volume 3: Photoelectric Effect"
    url: https://openstax.org/books/university-physics-volume-3/pages/6-2-photoelectric-effect
    accessed: 2026-10-04
    kind: book
    version: "University Physics Volume 3"
    applicability: "Порогова частота, робота виходу, енергія фотоелектронів та залежність фотоструму від інтенсивності для зовнішнього фотоефекту на металі."
---

## Short answer

Зовнішній фотоефект – це виліт електронів із поверхні матеріалу під дією світла. Для заданого матеріалу потрібна частота не нижча за порогову; інтенсивність вище порога переважно впливає на кількість емітованих електронів, а не на максимальну кінетичну енергію.[^openstax-photoelectric]

## Detailed explanation

Зовнішній фотоефект виникає, коли електрон поглинає фотон і отримує достатньо енергії, щоб залишити поверхню матеріалу. Енергія фотона пропорційна частоті світла: `E = h*f`, де `h` – стала Планка. Частина енергії витрачається на подолання роботи виходу матеріалу, а решта переходить у кінетичну енергію електрона.[^openstax-photoelectric]

Тому існує порогова частота, що залежить від матеріалу. Якщо світло має нижчу частоту, фотони не мають потрібної енергії, і збільшення інтенсивності не запускає зовнішню емісію. Еквівалентно можна говорити про порогову довжину хвилі: оскільки частота й довжина хвилі обернено пов’язані, коротша довжина хвилі означає більшу енергію фотона.[^openstax-photoelectric]

Коли частота вже перевищує поріг, інтенсивніше світло означає більше фотонів за одиницю часу. За інших однакових умов це може збільшити фотострум, тобто кількість електронів, що вилітають за час. Максимальна кінетична енергія фотоелектронів натомість зростає з частотою, а не просто з яскравістю.[^openstax-photoelectric]

**Типова помилка:** стверджувати, що достатньо дуже яскравого світла будь-якого кольору. Нижче порогової частоти окремий фотон не здатен вибити електрон, хоч би скільки таких фотонів падало на поверхню. Цей зовнішній фотоефект також не слід ототожнювати з внутрішнім фотоефектом у напівпровідниках, на якому працює багато фотодіодів і сонячних елементів.[^openstax-photoelectric]

## Sources

<!-- generated from frontmatter -->
