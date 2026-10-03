---
id: emb-elintro-0230
title: "Що таке `stall current` мотора і чому він важливий?"
description: "Що таке `stall current` мотора і чому він важливий?"
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
    applicability: "Походження питання: лекція 21, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: pololu-motor-stall
    title: "Pololu Jrk G2 Motor Controller User’s Guide: Choosing the motor, power supply, and Jrk"
    url: https://www.pololu.com/docs/0J73/4.1
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Визначення stall current, залежність від прикладеної напруги та короткочасний пусковий струм DC-мотора; не підтверджує конкретні параметри навчального макета."
---

## Short answer

`Stall current` – це струм DC-мотора під напругою, коли вал нерухомий. Він зазвичай набагато більший за струм вільного ходу, тому ключ, джерело живлення й проводи потрібно оцінювати з урахуванням такого пускового струму.[^pololu-motor-stall]

## Detailed explanation

`Stall current` описує струм щіткового DC-мотора, коли на нього подано задану напругу, але вал не обертається. Під час обертання мотор створює проти-ЕРС, яка зменшує струм; при нерухомому роторі цього ефекту немає. Тому струм визначається переважно напругою живлення та опором обмотки і досягає великого значення, пов’язаного з максимальним моментом і нульовою швидкістю.[^pololu-motor-stall]

У паспорті stall current зазвичай вказують для номінальної напруги конкретного мотора. Це не одна універсальна характеристика для всіх моторів і не обов’язково безпечний тривалий режим: обмотка нагрівається, а щітки й механіка зазнають навантаження. Під час звичайного запуску з нерухомого стану мотор короткочасно бере струм, близький до stall current, а після прискорення струм зазвичай знижується. Якщо вал механічно заблокований, великий струм може тривати й спричинити перегрів.[^pololu-motor-stall]

Приклад: якщо в документації мотора наведено stall current `0.8 A` за `6 V`, драйвер слід оцінювати щонайменше щодо такого стартового навантаження за цієї напруги, з урахуванням тривалості імпульсу, охолодження та обмежень виробника. Для іншої напруги значення буде іншим; наближення пропорційного масштабування за напругою працює лише за відповідних припущень про опір та температуру обмотки. Перевіряють також, чи може джерело витримати запуск без просідання напруги.[^pololu-motor-stall]

Типова помилка – підбирати транзистор або драйвер лише за робочим струмом мотора після розгону. Пусковий струм може перевищити цей показник у багато разів, а під час реверсу мотор може створити ще більший короткий струм. Також потрібен шлях для індуктивного струму при вимиканні, наприклад відповідний діод у простій схемі ключа. Отже, stall current допомагає визначити пікові вимоги до силового кола, але не скасовує перевірку теплового режиму й захисту.[^pololu-motor-stall]

## Sources

<!-- generated from frontmatter -->
