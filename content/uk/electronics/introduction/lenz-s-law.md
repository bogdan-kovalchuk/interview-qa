---
id: emb-elintro-0138
title: "Що таке закон Ленца?"
description: "Що таке закон Ленца?"
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
    applicability: "Пояснює знак мінус у законі Фарадея та те, що induced emf протидіє зміні струму/магнітного потоку."
---

## Short answer

Закон Ленца визначає напрям індукованої ЕРС: вона створює ефект, що протидіє зміні магнітного потоку, яка її спричинила. Для котушки це означає протидію зростанню струму або підтримку струму, що спадає, а не незмінний напрям індукованого струму.[^openstax-inductance-energy]

## Detailed explanation

Закон Ленца стверджує, що напрям індукованої ЕРС та пов’язаного з нею струму такий, щоб магнітне поле цього струму протидіяло зміні магнітного потоку, яка викликала індукцію. Це правило визначає напрям реакції системи, а не просто каже, що індукований струм «протилежний» до зовнішнього струму.[^openstax-inductance-energy]

У формулі Фарадея знак мінус кодує саме цю протидію. Якщо струм у котушці зростає, створений ним магнітний потік збільшується, і наведена ЕРС діє так, щоб стримати це зростання. Якщо струм спадає, ЕРС змінює полярність і намагається підтримати попередній струм. Напрям залежить від того, чи потік зростає або спадає, а також від того, як задано орієнтацію обмотки.[^openstax-inductance-energy]

Це також узгоджується із законом збереження енергії. Щоб збільшити струм і магнітне поле, джерело має виконати роботу проти наведеної ЕРС; при спаданні струму поле може віддавати накопичену енергію в коло. Тому індуктор не «забороняє» зміну струму, а створює напругу, величина якої пов’язана зі швидкістю цієї зміни.[^openstax-inductance-energy]

Приклад: коли вимикач розмикає коло з котушкою, струм прагне зменшитися. Полярність напруги на котушці стає такою, щоб підтримати цей струм; без обмежувального шляху напруга може зрости настільки, що виникне іскра на контактах. Захисний діод у відповідному DC-колі дає струму шлях для спадання.

**Типова помилка:** казати, що індукований струм завжди протилежний причині. Правильно спершу визначити напрям зміни потоку, а вже потім застосувати правило Ленца.

## Sources

<!-- generated from frontmatter -->
