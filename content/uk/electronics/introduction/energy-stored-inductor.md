---
id: emb-elintro-0137
title: "Де зберігається енергія в індукторі?"
description: "Де зберігається енергія в індукторі?"
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
    applicability: "Походження питання: лекція 14, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: openstax-inductance-energy
    title: "OpenStax College Physics 2e: 23.9 Inductance"
    url: https://openstax.org/books/college-physics-2e/pages/23-9-inductance
    accessed: 2026-10-04
    kind: book
    version: "College Physics 2e"
    applicability: "Енергія індуктора зберігається в магнітному полі; для лінійного індуктора наведено `E = L*I²/2`."
---

## Short answer

Енергія індуктора зберігається в магнітному полі, створеному струмом у його обмотці. Для лінійного індуктора `E = L*I²/2`, де `L` – індуктивність, а `I` – миттєвий струм.[^openstax-inductance-energy]

## Detailed explanation

Індуктор зберігає енергію у своєму магнітному полі, яке виникає навколо обмотки, коли нею тече струм. Для лінійного індуктора енергія дорівнює `E = L*I²/2`: вона залежить від індуктивності `L` та квадрата струму `I`.[^openstax-inductance-energy]

Залежність від квадрата струму важлива: якщо струм подвоїти за незмінної індуктивності, запасена енергія зросте вчетверо. Наприклад, для ідеалізованої котушки `L = 10 mH` зі струмом `I = 2 A` маємо `E = 0.01*2²/2 = 0.02 J`. У реальному компоненті допустимий струм обмежується нагріванням обмотки та, для осердя, насиченням; за насичення індуктивність може змінитися, тож проста лінійна модель стає менш точною.[^openstax-inductance-energy]

Ця енергія не є «енергією струму» як окремої речовини: струм підтримує магнітне поле, а поле є місцем накопичення енергії. Коли струм зменшується, поле слабшає, і енергія передається назад у коло або розсіюється в його опорах. Через це розмикання котушки без шляху для струму може спричинити значну напругу, що протидіє швидкому спаданню струму.[^openstax-inductance-energy]

**Типова помилка:** плутати місце накопичення енергії з міддю обмотки. Обмотка створює поле і проводить струм, але в ідеальній моделі запас енергії описує саме магнітне поле.

## Sources

<!-- generated from frontmatter -->
