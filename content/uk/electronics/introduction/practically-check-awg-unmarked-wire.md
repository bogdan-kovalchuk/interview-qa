---
id: emb-elintro-0278
title: "Як практично перевірити AWG дроту без маркування?"
description: "Як практично перевірити AWG дроту без маркування?"
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
    applicability: "Походження питання: лекція 25, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: nist-awg-wire-diameter
    title: "NIST: Evaluation of Wire Detection in X-Ray Images"
    url: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=919567
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Наводить діаметри окремих розмірів AWG для порівняння з виміряним діаметром; таблиця NIST не є повним калібрувальним стандартом."
---

## Short answer

Знеструмте провід, зніміть ізоляцію з кінця та виміряйте діаметр металевої жили штангенциркулем або мікрометром. Порівняйте результат із таблицею AWG: 24 AWG – близько `0.51 mm`, а 30 AWG – близько `0.26 mm`.[^nist-awg-wire-diameter]

## Detailed explanation

Непозначений провід можна попередньо класифікувати за діаметром оголеного провідника та таблицею AWG. Ізоляція не входить у номінальний розмір жили, тому вимірювання зовнішнього діаметра кабелю дає завищений результат. Перед підготовкою проводу переконайтеся, що він не підключений до живлення, а відкритий кінець не торкається інших провідників.[^nist-awg-wire-diameter]

Обережно зніміть невелику ділянку ізоляції, не надрізаючи мідь, і виміряйте голу жилу штангенциркулем або мікрометром. Для AWG 24 орієнтир – приблизно `0.511 mm`, для AWG 30 – `0.255 mm`. Близькі значення допомагають звузити пошук, але результат залежить від точності інструмента, деформації проводу та того, чи це суцільна або багатодротяна жила.[^nist-awg-wire-diameter]

Якщо провід багатодротяний, не вимірюйте зовнішній контур пучка й не порівнюйте його напряму з таблицею для суцільного провідника. Для визначення перерізу можна виміряти окремі дротинки та врахувати їх кількість, або звірити маркування котушки, специфікацію виробника чи виміряний опір відомої довжини. Перший спосіб потребує уважного підрахунку; другий – точного вимірювання довжини та надійного контакту.[^nist-awg-wire-diameter]

**Типова помилка:** прийняти товсту ізоляцію за товсту мідну жилу або зробити висновок про допустимий струм лише з виміряного діаметра. AWG описує розмір провідника, а не його температурний режим у конкретній конструкції. Після визначення розміру окремо перевірте рейтинг струму та напруги для матеріалу, ізоляції й умов укладання. Якщо розмір критичний для безпеки або сумісності з клемою, використовуйте маркування чи документацію виробника, а не приблизне вимірювання.[^nist-awg-wire-diameter]

## Sources

<!-- generated from frontmatter -->
