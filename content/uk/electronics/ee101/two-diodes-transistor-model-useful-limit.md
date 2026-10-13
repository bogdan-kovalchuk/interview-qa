---
id: emb-elee-0192
title: "Для чого корисна модель транзистора «два діоди» і де її межа?"
description: "Для чого корисна модель транзистора «два діоди» і де її межа?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Походження питання: лекція 67, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-13; курс не є доказом цих тверджень."
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділи 4.2 і 4.2.1: проста модель з двох діодів передбачає результати омметра для переходів B–E і B–C, але не пояснює струми обох контурів при прямо-зворотному зсуві, бо база тонка й слабко легована. Не описує підсилення."
  - source_id: fiore-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Підручник, розділ 4.5: спрощена модель Еберса–Молла з ідеальним діодом B–E і керованим струмом між C і B; β залежить від приладу, температури, I_C і V_CE. Даних конкретного приладу не наводить."
---

## Short answer

Модель «два діоди» допомагає перевірити переходи B–E і B–C мультиметром у режимі діода.[^fiore-bjt-basics] Але два окремі діоди не замінюють транзистор: вони не відтворюють керованого струму колектора.[^fiore-ebers-moll] Порядок виводів B, C, E звіряють з даташитом конкретного приладу.

## Detailed explanation

Кожен перехід транзистора можна замінити діодом, і тоді омметр або режим діода мультиметра дає очікувані результати. Для NPN: якщо плюсовий щуп на базі, а мінусовий на емітері чи колекторі, опір малий; при зворотній полярності він великий. Між емітером і колектором опір великий у будь-якій полярності, бо один з переходів завжди зворотний.[^fiore-bjt-basics] Для NPN це дає швидку перевірку: від бази мають проходити струми в обидва інші виводи, а короткого або обриву не має бути.

Межа моделі видна в активному режимі. За прямого B–E і зворотного B–C два незалежні діоди дали б малий струм у другому контурі. Насправді обидва контури несуть майже однаковий значний струм, бо база тонка й слабко легована. Модель з двох діодів розрізає базу на два окремі шматки, і саме це її ламає.[^fiore-bjt-basics]

Для розрахунку зсуву використовують спрощену модель Еберса–Молла: ідеальний діод B–E і кероване струмом джерело струму між колектором і базою. Вона дає `I_C = β*I_B` у прямому активному режимі, але β залежить від приладу, струму, напруги `V_CE` і температури, тож точні значення беруть з даташиту або вимірюють.[^fiore-ebers-moll]

Тест діода показує, що база утворює перехід з кожним з двох інших виводів,[^fiore-bjt-basics] але не каже, який з них E, а який C. Тому порядок виводів береться з даташиту конкретного приладу. Тест діода годиться для пошуку бази й перевірки переходів, але не для оцінки підсилення.

**Типові помилки:**

- Вважати, що два діоди пояснюють підсилення або активний режим.
- Визначати E і C тестом діода: він показує лише переходи від бази.
- Вважати «нормальні» покази тесту підтвердженням потрібного β.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
