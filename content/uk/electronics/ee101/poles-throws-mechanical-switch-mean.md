---
id: emb-elee-0004
title: "Що означають полюси (poles) і напрямки (throws) механічного перемикача?"
description: "Що означають полюси (poles) і напрямки (throws) механічного перемикача?"
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
    applicability: "Походження питання: лекція 33, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: te-switch-poles-throws
    title: "TE Connectivity: Understanding Switch Pole and Switch Throw"
    url: https://www.te.com/en/products/switches/intersection/global-switch-attributes.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Визначення poles і throws та базові конфігурації SPST, SPDT, DPST і DPDT; для конкретного перемикача також потрібна його схема контактів."
---

## Short answer

Полюс описує окреме коло або спільний контакт перемикача, а напрямок (throw) – кількість контактів, між якими цей полюс перемикає з’єднання. Наприклад, SPDT має один полюс і два вибрані вихідні контакти; позначення не задає саме по собі моментну поведінку чи схему контактів конкретної деталі.[^te-switch-poles-throws]

## Detailed explanation

Полюси й напрямки – це два параметри контактної конфігурації перемикача. Полюс (pole) відповідає кількості окремих кіл або спільних контактів, якими керує механізм. Напрямок (throw) означає, до скількох контактних шляхів може перемкнутися кожен полюс. Ця нотація допомагає зрозуміти базову топологію, але не описує всі електричні характеристики деталі.[^te-switch-poles-throws]

У SPST один полюс комутує один шлях: типовий приклад – просте вмикання або розмикання кола. У SPDT один спільний контакт переходить між двома іншими контактами, тож ним можна вибрати один із двох шляхів. У DPDT є два полюси, кожен із двома напрямками; одна дія перемикача керує обома полюсами одночасно. Тому «два полюси» не означає два незалежні органи керування: їх може з’єднувати спільний механічний привод.[^te-switch-poles-throws]

**Приклад читання позначення:**

Якщо на схемі вказано `SPDT`, визначте common контакт і два альтернативні контакти, а потім за символом з’ясуйте, який контакт замкнений у кожному положенні. Сам напис `SPDT` не встановлює, чи є третє центральне положення, чи перемикач momentary або latching, а також чи є перехід break-before-make чи make-before-break. Ці властивості потрібно перевірити за схемою контактів і datasheet конкретного виробу.[^te-switch-poles-throws]

Не плутайте кількість механічних положень руків’я з кількістю poles: це різні властивості. Так само pole не завжди означає окреме незалежно кероване навантаження; у багатополюсному перемикачі контакти часто перемикаються разом. Для підключення реального перемикача орієнтуйтеся на його розводку контактів, а не лише на загальне скорочення.[^te-switch-poles-throws]

## Sources

<!-- generated from frontmatter -->
