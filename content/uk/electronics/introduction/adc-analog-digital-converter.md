---
id: emb-elintro-0018
title: Що робить `ADC` (analog-to-digital converter)?
description: Що робить `ADC` (analog-to-digital converter)?
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
  applicability: 'Historical question provenance: lecture 4 of the Udemy course. Original flashcards remain in imports.
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
- source_id: adi-adc
  title: 'Analog Devices: Analog-to-digital conversion, chapter 20'
  url: https://wiki.analog.com/university/courses/electronics/text/chapter-20
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Sampling and finite-bit quantization, ADC/DAC distinction.
- source_id: adi-quantization
  title: 'Analog Devices MT-001: Quantization error and ADC SNR'
  url: https://www.analog.com/media/en/training-seminars/tutorials/MT-001.pdf
  accessed: 2026-10-04
  kind: official
  version: MT-001
  applicability: Ideal quantization error within half a step; real converter errors are additional.
---

## Short answer

Analog-to-digital converter перетворює analog input на numeric codes. У sampled-data system sampling визначає моменти часу, а quantization відносить амплітуди до скінченного набору codes; N-bit output має до `2^N` codes. Потрібно вказувати resolution, input range і sampling behavior. [^adi-adc]

## Detailed explanation

Sampling і quantization відповідають на різні питання: коли спостерігають сигнал і яке numeric value подає це спостереження? Збільшення sample rate саме по собі не додає amplitude codes. Збільшення bit depth саме по собі не дозволяє захоплювати швидші зміни. ADC architectures реалізують операції по-різному, тому спрощена модель є functional description. [^adi-adc]

Для ідеального uniform 8-bit converter із span 0–3.3 V корисна step model – `LSB = 3.3/256 ≈ 12.89 mV`. Ideal nearest-level quantizer має error в межах половини step для inputs усередині unclipped range, без крайових conventions. Точні transitions і full-scale definitions потрібно брати з converter datasheet. [^adi-quantization]

Реальна accuracy також включає reference error, offset, gain error, nonlinearity і noise. Sample може точно збігтися з representable level: quantization не означає ненульову error для кожного input. DAC виконує протилежне перетворення на analog output, зазвичай із відповідним reconstruction filtering.

## Sources

<!-- generated from frontmatter -->
