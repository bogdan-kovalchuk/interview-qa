---
id: emb-elintro-0003
title: Яка функція резистора у колі?
description: Яка функція резистора у колі?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання;
    конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела
    живлення; конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: aac-resistors
  title: 'All About Circuits: Resistors'
  url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
  accessed: 2026-10-04
  kind: book
  version: null
  applicability: Resistance, voltage/current relationship and dissipation.
---

## Short answer

Резистор пов’язує напругу та струм через опір: для ідеального ohmic resistor `V = I*R`. Він обмежує струм, утворює voltage divider та розсіює електричну енергію як тепло в межах допустимої потужності. [^aac-resistors]

## Detailed explanation

Опір не задає фіксованого падіння напруги: падіння залежить від струму. І навпаки, за сталої прикладеної напруги більший опір дає менший струм. Резистор не споживає заряд; він перетворює електричну енергію на тепло. Для ідеальної резистивної моделі використовують `P = V*I = I²*R = V²/R`. [^aac-resistors]

У розрахунковому прикладі 5 V на 1 kΩ дають `I = 5/1000 = 5 mA` та `P = 25 mW`. Йдеться про напругу саме на резисторі, а не автоматично про всю напругу живлення, якщо послідовно є інші компоненти.

Для LED з припущеним forward drop 2 V від живлення 5 V послідовний резистор 220 Ω дає приблизно `(5-2)/220 = 13.6 mA`; його розсіювання – близько 41 mW. Це розрахунок моделі, а не універсальна схема LED: перевірте фактичну forward voltage, допустимий струм LED, tolerance і rated power резистора. Реальний опір також може змінюватися з температурою.

## Sources

<!-- generated from frontmatter -->
