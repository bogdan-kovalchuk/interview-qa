---
id: emb-elintro-0237
title: "Чому через затвор MOSFET майже не тече постійний струм?"
description: "Чому через затвор MOSFET майже не тече постійний струм?"
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
    applicability: "Походження питання: лекція 22, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
---

## Short answer

Затвор MOSFET відділений від каналу ізоляційним шаром і утворює ємнісну структуру. У сталому режимі тече лише малий струм витоку, а помітний струм потрібен під час заряджання або розряджання gate capacitance.[^aac-semiconductors]

## Detailed explanation

Затвор MOSFET відділений від напівпровідникового каналу ізоляційним шаром, тому в першому наближенні його можна уявити як одну пластину конденсатора, а канал і підкладку – як іншу. Стала напруга створює електричне поле, яке змінює кількість носіїв заряду біля поверхні напівпровідника та керує провідністю каналу. Для ідеального конденсатора після встановлення напруги постійний струм не потрібен.[^aac-semiconductors]

Реальний MOSFET не ідеальний: datasheet задає gate leakage, а також ємності та gate charge. Під час увімкнення драйвер подає заряд, щоб підняти напругу gate; під час вимкнення він відводить заряд. Отже, струм має короткочасний характер, а його величина залежить від швидкості фронту, імпедансу драйвера та нелінійних ємностей транзистора.[^aac-semiconductors]

Наприклад, якщо керувати затвором повільно й дочекатися усталеного стану, вихід GPIO не віддає значний постійний струм у gate. Але швидкі перемикання повторюють процес заряджання багато разів, тому середній струм драйвера зростає разом із частотою та потрібним зарядом. Це також пояснює, чому силовому MOSFET може знадобитися окремий gate driver.[^aac-semiconductors]

**Типові помилки:**
- Казати, що gate зовсім не споживає струм: існують leakage та перехідний струм.
- Плутати відсутність сталого струму з відсутністю споживання енергії під час перемикання.
- Вважати gate ідеальним конденсатором на всіх напругах і частотах.

## Sources

<!-- generated from frontmatter -->
