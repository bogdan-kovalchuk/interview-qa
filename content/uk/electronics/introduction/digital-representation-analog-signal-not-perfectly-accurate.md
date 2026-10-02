---
id: emb-elintro-0019
title: Чому цифрове представлення аналогового сигналу не є ідеально точним?
description: Чому цифрове представлення аналогового сигналу не є ідеально точним?
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

Скінченне sampled representation може втрачати інформацію через quantization, недостатній sampling, noise та converter errors. Більше bits зменшують ideal amplitude step, а достатні sampling і filtering запобігають aliasing за відповідних припущень про сигнал. Error не обов’язково ненульова для кожного sample. [^adi-adc] [^adi-quantization]

## Detailed explanation

За сталого input span uniform N-bit step приблизно дорівнює `span/2^N`. Для span 3.3 V розрахунковий step зменшується з близько 12.89 mV при 8 bits до 0.806 mV при 12 bits. Це краща resolution, а не автоматично краща accuracy: реальні noise та systematic errors можуть домінувати. Ideal half-step quantization bound потребує відповідної quantizer model без clipping. [^adi-quantization]

Sampling створює окреме обмеження. Різні time-varying signals можуть дати однакові samples, якщо їхні spectra не обмежені; це aliasing. Тому anti-alias filtering і sample rate, відповідний signal bandwidth, є частиною acquisition, а не заміною більшої кількості amplitude bits. [^adi-adc]

Sampling сам по собі не обов’язково втрачає інформацію за всіх теоретичних умов: ideally band-limited signal із достатньо швидким ideal sampling можна відновити зі samples. Практичні finite records, finite precision та недосконалі converters не виконують усіх цих ideal conditions. Відрізняйте цю теорему від actual ADC measurement і не стверджуйте, що кожен sample мусить мати quantization error.

## Sources

<!-- generated from frontmatter -->
