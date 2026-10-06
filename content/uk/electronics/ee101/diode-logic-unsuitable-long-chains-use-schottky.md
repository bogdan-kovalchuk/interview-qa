---
id: emb-elee-0149
title: "Чому діодна логіка непридатна для довгих ланцюжків і навіщо в ній діоди Шотткі?"
description: "Чому діодна логіка непридатна для довгих ланцюжків і навіщо в ній діоди Шотткі?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 59, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: nexperia-diode-handbook
    title: "Nexperia: Diode Application Handbook (Design Engineer’s Guide), 2022"
    url: https://assets.nexperia.com/documents/brochure/Nexperia_document_book_DiodeApplicationHandbook_2022.pdf
    accessed: 2026-10-06
    kind: official
    version: "2022"
    applicability: "Розділ 7.4 (Switching diode): прості повільні діодні функції OR і AND з резистором (рис. 114–117): діоди розв’язують входи, за низького входу на резисторі лежить V_F, за всіх високих входів вихід високий; розділ 2: діод Шотткі має низьке пряме падіння, але є компроміс між V_F, струмом витоку й зворотною напругою. Загальні відомості, а не параметри конкретного діода."
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
    accessed: 2026-10-06
    kind: book
    version: "last updated 1996-07-16"
    applicability: "Лекційний матеріал курсу 1996 року зі спрощеною моделлю діода; додаткове джерело: діодні AND і OR з резистором, падіння на діоді «приблизно 0,7 В», накопичення падінь при каскадуванні (п’ять AND по 0,7 В дають 3,5 В), неможливість інвертора лише з діодів і резисторів. Не містить параметрів конкретних приладів."
  - source_id: vishay-bat54
    title: "Vishay: BAT54, BAT54A, BAT54C, BAT54S small signal Schottky diodes (datasheet)"
    url: https://www.vishay.com/docs/86410/bat54_bat54a_bat54c_bat54s.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 1.1, 21-Feb-2024"
    applicability: "Максимальне V_F за 25 °C: 240 мВ за 0,1 мА, 320 мВ за 1 мА, 400 мВ за 10 мА, 800 мВ за 100 мА; струм витоку до 2 мкА за V_R = 25 В; V_BR не менше 30 В. Значення стосуються цієї серії малосигнальних діодів Шотткі, а не всіх діодів Шотткі."
  - source_id: ti-hc00
    title: "TI: SN74HC00, SN54HC00 quadruple 2-input NAND gates (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-06
    kind: official
    version: "SCLS181H"
    applicability: "Розділ 6.3 Recommended Operating Conditions: V_IL(max) = 1,35 В і V_IH(min) = 3,15 В за V_CC = 4,5 В; рядка для V_CC = 5 В у таблиці немає. Значення стосуються цієї родини HC, інші родини логіки мають інші пороги."
---

## Short answer

Діодна логіка пасивна: вона не відновлює рівні й не підсилює сигнал, тому падіння `V_F` накопичуються від каскаду до каскаду.[^utah-cs6710-diode-logic] Діод Шотткі має менше `V_F`, тож логічний нуль зростає повільніше, але накопичення це не усуває, а менше `V_F` дається компромісом зі струмом витоку.[^nexperia-diode-handbook] Сумісність слід перевіряти за порогами наступного каскаду.[^ti-hc00]

## Detailed explanation

У діодному AND вихід низького рівня дорівнює низькому входу плюс `V_F`. Якщо цей вихід подати на вхід наступного такого вентиля, той додасть ще одне `V_F`, і так далі: після `n` каскадів логічний нуль піднімається приблизно до `n*V_F` (за сталого `V_F` й нульового входу). Handout наводить приклад: п’ять послідовних AND по 0,7 В дають на виході 3,5 В, що далеко від будь-якого розпізнаваного логічного нуля.[^utah-cs6710-diode-logic] У діодного OR аналогічно на кожному каскаді втрачається `V_F` високого рівня (див. `qid:emb-elee-0147`).

Виправити це самими діодами й резисторами не вдасться: у схемі немає активного елемента, який повернув би сигнал до напруги живлення чи землі. За handout, підвищення напруги живлення лише зсуває діапазони рівнів і збільшує потужність, не знімаючи обмеження на кількість каскадів; інвертор із самих діодів і резисторів побудувати неможливо, а ці проблеми розв’язують транзистори.[^utah-cs6710-diode-logic]

**Приклад (ідеалізований).** Візьмемо як наступний каскад SN74HC00 за `V_CC = 4.5 V`: `V_IL(max) = 1.35 V`.[^ti-hc00] Для кремнієвих діодів `V_F = 0.7 V` ланцюжок із двох AND уже дає `2*0.7 = 1.4 V > 1.35 V`, тобто нуль не гарантовано розпізнається. Для Шотткі з `V_F = 0.3 V` чотири каскади дають `4*0.3 = 1.2 V < 1.35 V`, а п’ятий – `1.5 V > 1.35 V`. Отже, Шотткі подовжує допустимий ланцюжок, але не робить його необмеженим. Це спрощена оцінка: реальне `V_F` залежить від струму (для BAT54 максимум зростає від 0,24 В за 0,1 мА до 0,8 В за 100 мА).[^vishay-bat54]

Діод Шотткі обирають через менше пряме падіння,[^nexperia-diode-handbook] яке зменшує втрату на кожному каскаді й збільшує запас до порога. Проте менше `V_F` пов’язане компромісом зі струмом витоку, тож параметри слід звіряти з datasheet.[^nexperia-diode-handbook]

**Типові помилки:**

- Вважати, що Шотткі робить діодну логіку придатною для довгих ланцюжків: вона лише збільшує допустиму довжину.
- Брати для всіх діодів `V_F = 0.7 V` і не враховувати залежність від струму та типу діода.[^vishay-bat54]
- Перевіряти лише логічний нуль у AND-ланцюжках і забувати про втрату високого рівня в OR-ланцюжках.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
