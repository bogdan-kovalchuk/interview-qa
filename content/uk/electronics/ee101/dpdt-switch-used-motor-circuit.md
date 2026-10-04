---
id: emb-elee-0009
title: "Навіщо в схемі з двигуном постійного струму використовують перемикач DPDT?"
description: "Навіщо в схемі з двигуном постійного струму використовують перемикач DPDT?"
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
  - source_id: mit-dc-motor-switching
    title: "MIT SeaPerch: Circuits using DPDT and SPDT switches to reverse the spin direction of DC motors"
    url: https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/5/2141/files/2025/05/SeaPerchII_SciTechNotes_5.pdf
    accessed: 2026-10-04
    kind: book
    version: "Science/Tech Note 5, revised 2025-04-30"
    applicability: "Показує схему DPDT з перехресно з’єднаними throw для зміни полярності на reversible DC motor у SeaPerch; не задає номінали чи придатність для інших двигунів і перемикачів."
  - source_id: aratas-switch-basics
    title: "ARATAS (formerly Omron): What is an Electrical Switch?"
    url: https://www.aratas.com/sg-en/products/basic-knowledge/switches/basics
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Основи контактних схем і вимога добирати перемикач відповідно до навантаження; конкретні рейтинг і компонування визначає документація моделі."
---

## Short answer

Двопозиційний DPDT можна з’єднати так, щоб у кожному положенні міняти місцями полярність на клемах реверсивного DC motor, змінюючи напрямок його обертання. Обидва полюси перемикаються разом, але результат залежить від перехресного підключення throw та придатності мотора до реверсу.[^mit-dc-motor-switching]

## Detailed explanation

DPDT означає Double Pole, Double Throw: це два перемикачі SPDT, механічно об’єднані одним приводом. У відповідній схемі контакти використовують для перестановки двох проводів живлення відносно двох клем мотора. Коли положення змінюється, полярність напруги на моторі змінюється на протилежну; у відповідного реверсивного DC motor це змінює напрямок обертання.[^mit-dc-motor-switching]

Для цього застосування обидві центральні клеми DPDT з’єднують із проводами мотора, а зовнішні throw з’єднують перехресно та підводять до джерела живлення. В одному положенні на мотор надходить звичайна полярність, у другому – протилежна. Сам DPDT не створює реверс автоматично: без правильного перехресного з’єднання він може просто вимикати або перемикати інші кола. Розташування COM і throw треба перевірити за схемою деталі або тестом continuity, бо воно не стандартизоване для всіх корпусів.[^mit-dc-motor-switching]

Напрямок обертання змінюється лише для типу мотора, який допускає зміну полярності на силових клемах. Наприклад, простий щітковий мотор з постійними магнітами зазвичай реверсує при зміні напряму струму в якорі; інші конструкції можуть вимагати перемикання окремої обмотки або спеціального драйвера. Тому твердження про «будь-який DC motor» було б надто широким. Також схема не задає швидкість і не гарантує гальмування.[^mit-dc-motor-switching]

Приклад: із джерелом 12 V у першому положенні клема M1 може бути під’єднана до +12 V, а M2 до 0 V; після перекидання M1 отримує 0 V, а M2 – +12 V. Отже, напруга `V_M1-M2` змінює знак. Це лише ілюстративна топологія: конкретна схема та номінали мають відповідати перемикачу й двигуну.[^mit-dc-motor-switching]

**Типові помилки:** вважати, що DPDT будь-якого розміру витримає струм запуску мотора або що його клеми мають типовий порядок. Вибирайте деталь із рейтингом, що відповідає навантаженню, і перевіряйте її pinout; допустимість комутації визначається документацією конкретного виробу.[^aratas-switch-basics]

## Sources

<!-- generated from frontmatter -->
