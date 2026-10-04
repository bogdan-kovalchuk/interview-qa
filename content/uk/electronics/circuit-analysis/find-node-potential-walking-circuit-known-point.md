---
id: emb-elcirc-0022
title: "Як знайти потенціал вузла, рухаючись по схемі від відомої точки?"
description: "Як знайти потенціал вузла, рухаючись по схемі від відомої точки?"
track: electronics
section: circuit-analysis
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
    applicability: "Походження питання: лекція 29, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-kvl
    title: "All About Circuits: Kirchhoff’s Voltage Law (KVL)"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/kirchhoffs-voltage-law-kvl/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує алгебраїчне додавання підйомів і спадів напруги вздовж замкненого шляху; умовні напрями обходу довільні за послідовного обліку знаків."
  - source_id: aac-voltage-polarity
    title: "All About Circuits: Polarity of voltage drops"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/polarity-voltage-drops/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Підтримує визначення полярності спаду на резисторі відносно напряму conventional current; не визначає полярність довільного активного компонента."
---

## Short answer

Почніть від вузла з відомим потенціалом і послідовно додавайте алгебраїчні зміни напруги вздовж шляху. Для резистора зі струмом, що входить у позначений «+» вивід, перехід від «+» до «−» є спадом, а у зворотному напрямі – підйомом; для джерела використовуйте його позначену полярність.[^aac-kvl][^aac-voltage-polarity]

## Detailed explanation

Потенціал вузла – це напруга цього вузла відносно вибраного опорного вузла. У багатьох схемах опорним вузлом є GND, якому за домовленістю призначають `0 V`; це не означає, що земля має абсолютний нульовий потенціал, а лише задає початок відліку. Потенціал іншого вузла можна знайти, пройшовши від відомої точки до нього та підсумувавши зміни напруги на елементах уздовж шляху.[^aac-kvl]

Знак кожної зміни залежить від напряму обходу та полярності елемента. На резисторі за пасивною домовленістю струм входить у вивід із вищим потенціалом; отже, рух у напрямку струму означає спад напруги, а рух проти нього – підйом. Для джерела напруги дивіться на символи «+» і «−»: перехід від мінуса до плюса додає напругу, а від плюса до мінуса віднімає її.[^aac-voltage-polarity]

Наприклад, якщо від `GND = 0 V` пройти через джерело від «−» до «+» величиною `5 V`, а потім через резистор у напрямі спаду `2 V`, отримаємо вузол на `3 V`. Якщо пройти замкненим шляхом назад до початкової точки, алгебраїчна сума змін повинна дорівнювати нулю – це дає спосіб перевірити знаки.[^aac-kvl]

**Типові помилки:**

- Додавати всі модулі напруг без знаків, через що підйом сплутується зі спадом.
- Вважати, що потенціал вузла має сенс без зазначення опорної точки.
- Приписувати спад резистора за напрямом обходу, не перевіривши напрям струму або задану полярність.

Якщо невідомі струми чи елементи утворюють складну мережу, простого обходу може бути недостатньо: тоді спершу розв’яжіть рівняння для струмів і напруг, а потім використайте їх для перевірки потенціалу вузла.[^aac-kvl]

## Sources

<!-- generated from frontmatter -->
