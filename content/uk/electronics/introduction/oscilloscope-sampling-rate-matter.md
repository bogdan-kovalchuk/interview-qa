---
id: emb-elintro-0270
title: "Чому важлива sampling rate осцилографа?"
description: "Чому важлива sampling rate осцилографа?"
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
    applicability: "Походження питання: лекція 24, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: tek-oscilloscope-specs
    title: "Tektronix: Evaluating Oscilloscope Bandwidth, Sample Rate, and Key Specifications"
    url: https://www.tek.com/en/documents/primer/evaluating-oscilloscopes
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Частота дискретизації, aliasing, обмеження правила Найквіста для скінченного запису та практична потреба в запасі вибірок."
---

## Short answer

Sampling rate – це кількість вибірок сигналу, які осцилограф бере за секунду; вона визначає часову деталізацію запису.[^tek-oscilloscope-specs] Замала частота дискретизації може призвести до aliasing або пропуску коротких подій, тому правило Найквіста «удвічі вище за найвищу частоту» не є достатнім практичним запасом для довільних імпульсів і glitch.[^tek-oscilloscope-specs]

## Detailed explanation

Sampling rate осцилографа – кількість виміряних значень сигналу за секунду, зазвичай у S/s або GS/s. Між вибірками прилад не має безпосереднього вимірювання сигналу, тому вища частота дискретизації за інших рівних умов дає більше часових точок і зменшує ризик пропустити коротку подію.[^tek-oscilloscope-specs]

Для ідеального безперервного сигналу з обмеженим спектром теорема Найквіста вимагає частоту дискретизації вищу за подвоєну найвищу частоту складової, щоб уникнути aliasing. Але реальний осцилограф має скінченний запис, а короткий glitch не є безперервною періодичною подією: вибірка може просто не потрапити в його короткий інтервал. Тому для відтворення форми хвилі на практиці потрібен запас, що залежить від типу сигналу, алгоритму інтерполяції та задачі вимірювання.[^tek-oscilloscope-specs]

Приклад: період сигналу 1 µs відповідає частоті 1 MHz. На 2 MS/s припадає в середньому лише дві вибірки на період – цього недостатньо, щоб надійно побачити форму, фронти чи короткий провал. За 100 MS/s інтервал між вибірками становить 10 ns, що дає близько 100 точок за період. Навіть тоді фронт коротший за цей інтервал може бути недостатньо деталізований, а максимальна доступна частота також залежить від аналогової bandwidth та довжини запису.[^tek-oscilloscope-specs]

**Типові помилки:**

- Застосовувати правило «дві вибірки за період» як гарантію точного відтворення будь-якої хвилі.
- Плутати sampling rate із bandwidth: достатня кількість вибірок не компенсує обмежений аналоговий тракт.
- Ігнорувати довжину запису: за фіксованої пам’яті підвищення частоти дискретизації скорочує часовий інтервал, який можна захопити.[^tek-oscilloscope-specs]

## Sources

<!-- generated from frontmatter -->
