---
id: emb-elee-0094
title: "Як спроєктувати RC-ФНЧ на 1 kHz з R = 1 kΩ і що робити після вибору стандартного номіналу?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-rc-low-pass-transfer
    title: "All About Circuits: Understanding Low-Pass Filter Transfer Functions"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-transfer-functions-for-low-pass-filters/
---

## Short answer

За `R = 1 kΩ` для зрізу `f_c = 1 kHz` потрібна ємність `C = 1/(2*pi*R*f_c) ≈ 159 nF`. Якщо вибрати стандартні `150 nF`, фактичний зріз становитиме `1/(2*pi*1 kΩ*150 nF) ≈ 1.06 kHz`; після вибору реальних номіналів частоту слід перерахувати, врахувавши допуски й навантаження.[^aac-rc-low-pass-transfer]

## Detailed explanation

Для простого пасивного RC-ФНЧ першого порядку частота зрізу визначається добутком опору й ємності: `f_c = 1/(2*pi*R*C)`. Якщо задані `R` та бажана `f_c`, ємність знаходять перестановкою формули: `C = 1/(2*pi*R*f_c)`. Вважаємо, що вихід знімається з конденсатора, джерело має малий вихідний опір, а навантаження не змінює подільник суттєво.[^aac-rc-low-pass-transfer]

**Приклад розрахунку:** для `R = 1 kΩ` і `f_c = 1 kHz` ідеальна ємність дорівнює приблизно `159 nF`. У серії стандартних компонентів може не бути саме такого значення; якщо обрати `150 nF`, повторний розрахунок дає близько `1.06 kHz`. Якщо обрати `160 nF`, результат буде близько `995 Hz`. Різниця від заданої частоти не є помилкою формули – це наслідок округлення номіналу.[^aac-rc-low-pass-transfer]

Після вибору деталей потрібно обчислити фактичну частоту ще раз за їхніми номіналами. Для точнішої оцінки враховують допуск резистора та конденсатора: комбінація крайніх значень дає діапазон можливих частот, а не одну гарантовану точку. Також слід перевірити опір джерела й вхідний опір наступного каскаду, адже вони змінюють ефективні `R` або навантаження конденсатора. За значного навантаження проста формула з одним `R` вже не описує точний зріз; коло аналізують як повний подільник або додають буфер.[^aac-rc-low-pass-transfer]

**Типові помилки:**
- Підставляти `1 kΩ` і `1 kHz` без перетворення одиниць та отримувати ємність у неправильному масштабі.
- Вважати розраховані `159 nF` доступним точним номіналом.
- Не враховувати завантаження фільтра наступним каскадом.

Практичний порядок такий: обрати доступні компоненти з потрібними допусками, повторно обчислити `f_c` і за потреби змоделювати або виміряти реальне коло.[^aac-rc-low-pass-transfer]
