---
id: emb-elintro-0120
title: "Розрахуйте резистор для червоного `LED`: V = 5 V, V_f = 1.9 V, I = 15 mA?"
description: "Розрахуйте послідовний резистор для червоного LED за V = 5 V, V_f = 1.9 V та I = 15 mA."
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
    applicability: "Походження питання: лекція 12, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-led-resistor
    title: 'All About Circuits: Special-purpose Diodes'
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
    accessed: '2026-10-04'
    kind: book
    version: null
    applicability: 'Підтримує розрахунок послідовного резистора за різницею напруги та струмом, а також перевірку потужності; задане V_f є навчальним припущенням, не універсальною характеристикою червоного LED.'
---

## Short answer

За ідеального джерела `5 V` і заданого падіння `V_f = 1.9 V`, розрахунок дає `R = (5 - 1.9)/0.015 ≈ 207 Ω`; найближчий більший стандартний номінал `220 Ω` задає приблизно `14.1 mA`.[^aac-led-resistor] Реальне `V_f` змінюється між екземплярами та зі струмом і температурою, тому це розрахунок для заданих припущень, а не точний гарантований струм.

## Detailed explanation

Послідовний резистор для `LED` добирають за різницею між напругою джерела й прямим падінням на діоді, поділеною на бажаний струм; за заданими умовами `5 V`, `1.9 V` і `15 mA` ідеальний результат становить приблизно `207 Ω`.[^aac-led-resistor]

У послідовному колі через резистор і `LED` тече той самий струм. За законом Кірхгофа сума падінь напруг дорівнює напрузі джерела, тому резистор має прийняти залишок після прямого падіння на діоді. Закон Ома дає `R = (V_supply - V_f)/I`. Значення `V_f` залежить від типу діода, струму та температури; значення `1.9 V` у цій задачі є заданим припущенням для обчислення, а не універсальним параметром кожного червоного `LED`.[^aac-led-resistor]

Підставивши числа, отримуємо `3.1 V` на резисторі. Ділення на `0.015 A` дає приблизно `206.7 Ω`, тож для навчального прикладу можна вибрати стандартні `220 Ω`. За тих самих ідеальних `5 V` і `1.9 V` струм буде близько `14.1 mA`, а потужність резистора – близько `44 mW`. Це нижче за типовий номінал резистора `0.125 W`, однак реальний проєкт має враховувати температуру та derating конкретного резистора.[^aac-led-resistor]

```text
V_R = 5 - 1.9 = 3.1 V
R_ideal = 3.1 / 0.015 = 206.7 Ω
I_at_220Ω = 3.1 / 220 = 0.0141 A ≈ 14.1 mA
P_at_220Ω = 3.1 * 0.0141 ≈ 0.044 W
```

**Типові помилки:**

- Ділити повну напругу `5 V` на струм і забути падіння на `LED`. Тоді резистор вийде завеликим для заданого струму.
- Підставляти `15` замість `0.015` у формулу з омахами. Струм потрібно виразити в амперах.
- Вважати `220 Ω` гарантією рівно `15 mA`. Реальний струм залежить від допуску резистора, напруги живлення та розкиду `V_f`; розрахунок перевіряють на граничних значеннях datasheet.[^aac-led-resistor]

## Sources

<!-- generated from frontmatter -->
