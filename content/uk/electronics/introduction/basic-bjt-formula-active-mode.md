---
id: emb-elintro-0198
title: "Основна формула `BJT` в активному режимі?"
description: "Основна формула `BJT` в активному режимі?"
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
    applicability: "Походження питання: лекція 19, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Для `BJT` у прямому активному режимі наближено `I_C = β*I_B`, де `β` – коефіцієнт передачі струму для конкретного робочого режиму. Це не універсальна стала: β змінюється між екземплярами та залежить від струму, напруги й температури. У насиченні навантаження обмежує струм, тож формула вже не задає фактичний `I_C`.[^aac-semiconductors]

## Detailed explanation

У прямому активному режимі базо-емітерний перехід відкритий, а колекторно-базовий – закритий. У цій області для спрощеного аналізу використовують співвідношення `I_C = β*I_B`, де β (також `h_FE` у DC-контексті) є відношенням струму колектора до струму бази.[^aac-semiconductors]

Фізично тонка база дає змогу більшості носіїв, інжектованих емітером, дістатися колектора; менша частина рекомбінує в базі й утворює базовий струм. Модель β зручна для оцінки, але це не точна пропорційність для всіх умов. Значення β беруть з datasheet для відповідних струму колектора та напруги; гарантовані межі можуть бути широкими, а параметр змінюється з температурою.[^aac-semiconductors]

Коли транзистор насичений, зовнішнє коло не здатне забезпечити струм, який вимагала б оцінка β*I_B. Тоді обидва переходи провідні, а струм визначають живлення та навантаження. Саме тому для перемикання транзистора зазвичай задають достатній запас базового струму, а не покладаються на типове β з одного рядка таблиці.[^aac-semiconductors]

Приклад: якщо для розрахунку прийняти β = 100 і `I_B = 20 µA`, модель дає `I_C = 2 mA`. Це лише оцінка для активного режиму; реальний транзистор може мати інше β, а навантаження може обмежити струм нижче 2 mA.[^aac-semiconductors]

**Типові помилки:** трактувати β як гарантовану константу; застосовувати формулу в насиченні або відсічці; плутати DC `h_FE` із малосигнальним коефіцієнтом підсилення.[^aac-semiconductors]

## Sources

<!-- generated from frontmatter -->
