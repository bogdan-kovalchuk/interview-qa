---
id: emb-elintro-0002
title: Яка ключова різниця між аналоговим і цифровим сигналом?
description: Яка ключова різниця між аналоговим і цифровим сигналом?
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
- source_id: ti-pam4
  title: 'TI SNAA325A: PAM-4 signaling'
  url: https://www.ti.com/lit/an/snaa325a/snaa325a.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: 'Section 1.2: four discrete signaling levels encode two bits per symbol.'
---

## Short answer

Analog signal подає інформацію через величину, що може змінюватися неперервно; digital signal використовує дискретний набір символів. Binary logic зазвичай має LOW і HIGH, але digital signaling може мати більше двох рівнів: PAM-4 використовує чотири рівні та передає два біти на символ. [^ti-pam4]

## Detailed explanation

Відмінність стосується способу подання й інтерпретації інформації. Analog voltage може кодувати виміряну температуру в неперервному діапазоні. Digital receiver відносить прийняту форму сигналу до одного зі скінченного набору символів. Сама електрична напруга під час переходів усе одно змінюється неперервно; фізично дискретною величиною вона не стає.

У binary signaling два розпізнавані стани кодують 0 та 1. PAM-4 спростовує правило, ніби кожен digital signal має тільки два рівні напруги: чотири рівні символів кодують два біти на символ. Отже, digital – ширше поняття, ніж binary. [^ti-pam4]

Сигнал також може бути дискретним у часі, не будучи двійковим за амплітудою. Sampling визначає моменти спостереження; quantization – значення амплітуди, які можна подати. У поясненні ADC ці дві операції потрібно розрізняти. Цифрове подання дозволяє обробляти символи, але саме по собі не гарантує нечутливості до електричного шуму.

## Sources

<!-- generated from frontmatter -->
