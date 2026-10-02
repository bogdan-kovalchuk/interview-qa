---
id: emb-elintro-0079
title: "Що означає \"120 В у розетці США\"? Це `RMS` чи пік?"
description: "Що означає \"120 В у розетці США\"? Це `RMS` чи пік?"
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
    applicability: "Походження питання: лекція 9, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-ac-magnitude
    title: "All About Circuits: Measurements of AC Magnitude"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-1/measurements-ac-magnitude
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює RMS і межі показів вимірювачів; покази залежать від типу приладу та форми сигналу."
---

## Short answer

120 V у мережі США – номінальне значення `RMS`, а не пік. Для чистої синусоїди пік становить приблизно `120*√2 = 170 V`, а peak-to-peak – приблизно `340 V`. Показ AC-мультиметра залежить від його конструкції та форми сигналу; не кожен прилад вимірює true RMS.[^aac-ac-magnitude]

## Detailed explanation

Позначення `120 V` для побутової мережі США означає номінальну діючу (RMS) напругу. Воно не описує миттєву напругу в кожну мить і не є піковим значенням; для синусоїди піки більші за RMS приблизно у `√2` раза.[^aac-ac-magnitude]

RMS пов’язує змінний сигнал із його середньою потужністю на резистивному навантаженні. Тому номінальні напруги мережі зазвичай подають як RMS. Миттєва напруга синусоїди змінюється між позитивним і негативним піками, а не залишається на рівні `120 V`.[^aac-ac-magnitude]

Для ідеальної синусоїди амплітуда дорівнює `V_peak = V_rms*√2`. Отже, при `120 V RMS` пік приблизно `169.7 V`, тобто близько `±170 V`; повний розмах `V_pp = 2*V_peak` – приблизно `339.4 V`. Це розрахунок для чистої синусоїди, а не твердження про фактичне миттєве значення кожної розетки за будь-яких умов.[^aac-ac-magnitude]

Режим `AC` мультиметра не гарантує true RMS: прості прилади можуть бути відкалібровані для синусоїди, а їхня точність погіршується на спотворених хвилях. Для вимірювання несинусоїдального сигналу потрібен прилад із true-RMS функцією та достатньою смугою/crest factor. Також слід перевіряти межі напруги й безпечну категорію приладу перед роботою з мережею.[^aac-ac-magnitude]

**Типова помилка:** трактувати `120 V` як пік або автоматично очікувати, що будь-який AC-вимірювач покаже справжній RMS. Відокремлюйте номінальне RMS від піку, а властивості вимірювання звіряйте з документацією конкретного приладу.[^aac-ac-magnitude]

## Sources

<!-- generated from frontmatter -->
