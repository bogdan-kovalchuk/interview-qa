---
id: emb-elintro-0092
title: "Коли P &gt; 0, а коли P &lt; 0 у елементі кола?"
description: "Коли P &gt; 0, а коли P &lt; 0 у елементі кола?"
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
    applicability: "Походження питання: лекція 10, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-polarity-voltage-drops
    title: "All About Circuits: Polarity of voltage drops"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/polarity-voltage-drops/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює вибір полярності падіння напруги відносно напрямку струму та підтримує пасивну знакову домовленість."
---

## Short answer

За пасивною знаковою домовленістю `P = V*I` додатна потужність означає, що елемент поглинає енергію: опорний струм входить у позначений додатним вивід напруги. Від’ємна потужність означає, що елемент віддає енергію в коло; знак визначається вибраними напрямками та полярністю, а не типом компонента.[^aac-polarity-voltage-drops]

## Detailed explanation

Знак потужності описує напрямок передавання енергії за обраною системою відліку. У пасивній знаковій домовленості спочатку задають полярність напруги на двовивідному елементі, а напрямок опорного струму вважають додатним, коли він входить у вивід, позначений «+». Тоді добуток `P = V*I` є додатним, коли елемент поглинає потужність, і від’ємним, коли він її віддає.[^aac-polarity-voltage-drops]

Домовленість не вимагає вгадати фактичний напрямок до розрахунку. Якщо обраний напрямок струму виявився протилежним реальному, розв’язок дасть від’ємне значення струму. Аналогічно, знак добутку напруги й струму покаже потік потужності. Важливо лишити початкові опорні напрями незмінними в усьому розрахунку, а наприкінці інтерпретувати знаки послідовно.[^aac-direct-current] [^aac-polarity-voltage-drops]

Наприклад, резистор із додатним `V` та струмом, що входить у його додатний вивід, має `P > 0` і перетворює електричну енергію на тепло. Для батареї, яка живить коло, якщо напругу визначено від її додатного виводу до від’ємного, струм зазвичай виходить із додатного виводу; за пасивною домовленістю це дає `P < 0`, тобто батарея віддає енергію. Під час заряджання напрямок струму через батарею зміниться, і вона матиме додатну потужність, бо поглинатиме енергію.[^aac-direct-current]

**Типові помилки:**
- Називати будь-який елемент-джерело від’ємним за означенням. Джерело може поглинати потужність у режимі заряджання або гальмування.
- Вважати, що напрямок звичайного струму сам по собі задає знак потужності, не уточнивши опорну полярність напруги на виводах елемента.[^aac-polarity-voltage-drops]

## Sources

<!-- generated from frontmatter -->
