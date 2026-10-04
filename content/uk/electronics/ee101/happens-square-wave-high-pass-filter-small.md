---
id: emb-elee-0111
title: "Що відбувається з прямокутним сигналом після RC-ФВЧ з малою сталою часу?"
description: "Що відбувається з прямокутним сигналом після RC-ФВЧ з малою сталою часу?"
track: electronics
section: ee101
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
    applicability: "Походження питання: лекція 51, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Частотна поведінка capacitive high-pass; разом із моделлю RC transient response пояснює реакцію на фронти прямокутного сигналу."
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor Transient Response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Експоненційне заряджання та стала часу RC для ідеальної моделі; реальні втрати та паразитні параметри тут не розглянуто."
---

## Short answer

Якщо `τ = R*C` мала порівняно з півперіодом, вихід RC-ФВЧ утворює короткі імпульси біля фронтів: додатний після зростання та від’ємний після спадання входу. Між фронтами експоненційна складова спадає майже до нуля; схема не випрямляє сигнал.[^aac-high-pass-filters] [^aac-capacitor-transient]

## Detailed explanation

RC-ФВЧ реагує на зміни входу, а не підтримує на виході його постійний рівень. На фронті прямокутного сигналу напруга конденсатора не може миттєво змінитися, тому початково значна частина стрибка з’являється на резисторі. Далі конденсатор заряджається через опір кола, і вихід експоненційно наближається до нуля. На спадному фронті знак імпульсу змінюється. Для базового кола стала часу `τ = R*C`, а частота зрізу `f_c = 1/(2π*R*C)`.[^aac-high-pass-filters] [^aac-capacitor-transient]

Вислів «мала стала часу» має сенс лише відносно тривалості рівнів сигналу. Якщо період дорівнює `T`, а прямокутник має 50-відсотковий duty cycle, кожен рівень триває `T/2`. Коли `τ` набагато менша за `T/2`, попередній перехідний процес майже встигає згаснути до наступного фронту. Якщо ж `τ` порівнянна з тривалістю рівня, імпульси перекриваються, і вихід не повертається близько до нуля до наступного переходу.[^aac-capacitor-transient]

Приклад: нехай `τ = 1 ms`, а рівень сигналу триває `5 ms`. Після одного часу `τ` експоненційна складова зменшується приблизно до 37 відсотків початкової, а після п’яти `τ` залишається менш як один відсоток. Тому такий вибір дає короткий викид і майже нульовий вихід перед наступним фронтом. Амплітуда першого викиду залежить від амплітуди стрибка, початкового заряду конденсатора та подільника напруги джерелом і навантаженням.[^aac-capacitor-transient]

**Типова помилка:** називати ці викиди випрямленою прямокутною хвилею або вважати, що ФВЧ завжди дає однакові вузькі імпульси. Полярність відповідає напрямку фронту, а форма між фронтами залежить від `τ`, періоду, duty cycle та навантаження. Для точного прогнозу треба врахувати весь опір, який бачить конденсатор, а не лише позначення одного резистора.[^aac-high-pass-filters] [^aac-capacitor-transient]

## Sources

<!-- generated from frontmatter -->
