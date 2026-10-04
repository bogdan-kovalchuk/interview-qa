---
id: emb-elcirc-0031
title: "Чому резистивний подільник не може підвищувати напругу?"
description: "Чому резистивний подільник не може підвищувати напругу?"
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
    applicability: "Походження питання: лекція 30, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює розподіл напруги в послідовному колі; навантаження слід врахувати окремо."
---

## Short answer

Для двох резисторів між джерелом і спільним проводом `V_out = V_in*R_2/(R_1+R_2)`. За пасивних резисторів `R_1 ≥ 0`, тож вихід є часткою вхідної напруги, а не її підвищеним значенням. Щоб отримати вищу напругу, потрібен перетворювач енергії, наприклад boost-конвертер або трансформатор у відповідному колі.[^aac-direct-current]

## Detailed explanation

Резистивний подільник – це послідовне коло, у якому вихід знімають із частини загальної напруги. Через обидва резистори тече той самий струм, а спад на кожному пропорційний його опору; тому частка на `R_2` дорівнює `R_2/(R_1+R_2)`. Мережа розподіляє наявну напругу між елементами, але не створює додаткову енергію.[^aac-direct-current]

Межі видно з крайніх випадків. Якщо `R_1 = 0`, вихід ідеальної ненавантаженої схеми дорівнює входу; якщо `R_2 = 0`, вихід дорівнює нулю. Для додатних опорів між ними виходить значення між нулем і `V_in`. Це висновок для пасивного двохрезисторного подільника з ідеальним джерелом. Якщо точка `V_out` під’єднана до навантаження, воно змінює нижню гілку, тому розрахунок без навантаження вже не достатній.[^aac-direct-current]

Приклад розрахунку:

Для `V_in = 9 V`, `R_1 = 10 kΩ` і `R_2 = 20 kΩ` струм у ненавантаженому колі дорівнює `9 V/(30 kΩ) = 0.3 mA`, а вихід на `R_2` становить `6 V`. Він нижчий за джерело, бо на `R_1` припадає решта `3 V`.

**Типові помилки:**

- Плутати подільник із підвищувальним перетворювачем: більший опір нижнього плеча змінює частку, але не дає вихід вище джерела.
- Застосовувати формулу ненавантаженого подільника після під’єднання споживача: тоді слід врахувати його паралельно `R_2`.

## Sources

<!-- generated from frontmatter -->
