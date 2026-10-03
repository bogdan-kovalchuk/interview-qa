---
id: emb-elintro-0269
title: "Що означає bandwidth осцилографа?"
description: "Що означає bandwidth осцилографа?"
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
    applicability: "Визначення смуги як точки -3 dB для синусоїдального входу та наслідки недостатньої смуги для вимірювання амплітуди й фронтів."
---

## Short answer

Bandwidth задає частоту, на якій амплітуда синусоїдального сигналу на вході осцилографа вже зменшена до 70.7% від опорної, тобто до точки -3 dB.[^tek-oscilloscope-specs] Недостатня смуга спотворює амплітуду й швидкі фронти; потрібний запас визначається сигналом і потрібною точністю.[^tek-oscilloscope-specs]

## Detailed explanation

Bandwidth осцилографа – характеристика його аналогового тракту, яка описує, наскільки добре він передає сигнали різної частоти. Її стандартно задають частотою синусоїдального входу, на якій виміряна амплітуда падає до 70.7% від низькочастотного значення. Це точка -3 dB, а не жорстка межа, за якою осцилограф перестає показувати сигнал.[^tek-oscilloscope-specs]

Коли частота складової наближається до bandwidth приладу, її амплітуда відображається зі спадом. У складному сигналі, наприклад меандрі, фронти складаються з багатьох гармонік, тож обмежена смуга послаблює високочастотні складові: фронт виглядає повільнішим, а форма та пікова амплітуда можуть спотворитися. Для швидких цифрових переходів корисно також дивитися на rise time приладу й пробника; одного порівняння bandwidth із частотою повторення меандру недостатньо.[^tek-oscilloscope-specs]

Приклад: якщо вимірювана синусоїда має частоту, рівну номінальній bandwidth осцилографа, очікувана амплітуда на вході вже приблизно на 29.3% нижча за опорну, відповідно до визначення точки -3 dB. Якщо потрібно виміряти амплітуду в межах кількох відсотків, треба підібрати вищу смугу або перевірити специфікацію точності для своєї частоти; правило запасу на кшталт «у п’ять разів» є практичним орієнтиром, а не універсальною гарантією.[^tek-oscilloscope-specs]

**Типові помилки:**

- Трактувати bandwidth як частоту дискретизації: перша характеризує аналоговий тракт, друга – часовий крок вибірок.
- Вважати вимірювання точним аж до граничної частоти без похибки амплітуди.
- Оцінювати меандр лише за частотою повторення, ігноруючи швидкість його фронтів.

## Sources

<!-- generated from frontmatter -->
