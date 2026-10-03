---
id: emb-elintro-0141
title: "Чому розрив кола з індуктором небезпечний?"
description: "Чому розрив кола з індуктором небезпечний?"
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
  - source_id: aac-inductor-voltage
    title: "All About Circuits, Inductor Voltage and Current Relationship"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує співвідношення напруги й струму ідеального індуктора, полярність за законом Ленца та викид напруги під час швидкого переривання струму; реальний пік залежить від паразитних параметрів і захисту."
---

## Short answer

Під час розмикання індуктор створює напругу, що протидіє швидкій зміні струму: `v = L*(di/dt)`. Її пік залежить від кола й захисту, тому значення «сотні вольт» не є універсальним; flyback-діод обмежує напругу, але сповільнює спад струму.[^aac-inductor-voltage]
## Detailed explanation

Під час розмикання кола індуктор створює напругу, яка намагається підтримати струм через обмотку. Струм в індукторі не може миттєво змінитися в ідеальній моделі: за співвідношенням `v = L*(di/dt)` швидке зменшення струму вимагає великої напруги з полярністю, що протидіє цьому зменшенню. Це не означає, що індуктор «виробляє» енергію з нічого: до розмикання енергія була запасена в його магнітному полі.[^aac-inductor-voltage]

Коли контакти вимикача розходяться, повітряний проміжок має дуже великий опір, але поле може пробитися іонізацією повітря. Тоді виникає дуга, через яку струм спадає повільніше, а енергія магнітного поля переходить у тепло та світло. Без дуги або іншого шляху розсіювання напруга зростає настільки, наскільки дозволяють паразитні ємності та ізоляція; реальна межа залежить від компонента й схеми, тому вона не є фіксованою величиною.[^aac-inductor-voltage]

Наприклад, у релейному колі вимкнення струму котушки може створити викид напруги, здатний пошкодити транзисторний ключ. Захисний діод, під’єднаний паралельно котушці у зворотному напрямку під час нормального живлення, дає струму шлях циркуляції після вимкнення; це обмежує напругу, хоча й уповільнює спад струму котушки. Для швидкого вимкнення застосовують інші обмежувачі, підібрані до допустимих напруг ключа та потрібного часу спаду.[^aac-inductor-voltage]

**Типова помилка:** вважати, що розімкнений вимикач гарантує нульовий струм і нульову напругу на котушці. Після розмикання струм спочатку продовжує текти через дугу, захисний елемент або паразитний шлях; план захисту має враховувати, куди саме піде запасена енергія.[^aac-inductor-voltage]

## Sources

<!-- generated from frontmatter -->
