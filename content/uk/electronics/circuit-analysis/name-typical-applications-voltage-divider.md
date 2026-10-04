---
id: emb-elcirc-0036
title: "Назвіть типові застосування подільника напруги."
description: "Назвіть типові застосування подільника напруги."
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
  - source_id: adi-voltage-divider
    title: "Analog Devices: Voltage Divider"
    url: https://www.analog.com/en/resources/glossary/voltage-divider.html
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Підтримує застосування подільника та пояснює, що навантаження впливає на вихідну напругу; не задає точних номіналів для конкретного пристрою."
  - source_id: ti-voltage-divider-adc
    title: "Texas Instruments: Interfacing 5V Sensors and Signals to 3.3V Input SAR ADCs"
    url: https://www.ti.com/lit/an/sprad89/sprad89.pdf
    accessed: 2026-10-04
    kind: official
    version: "SPRAD89, March 2023"
    applicability: "Підтримує масштабування сигналу для ADC та застереження щодо source impedance, settling і навантаження ADC; приклад стосується SAR ADC."
---

## Short answer

Подільник напруги зменшує рівень сигналу для входу ADC і дає змогу вимірювати напругу батареї, якщо його вихід відповідає допустимому діапазону входу. Потенціометр використовують як регульований подільник для задання рівня сигналу; сам пасивний подільник не є стабільним джерелом живлення.[^adi-voltage-divider] Для ADC треба врахувати його вхідне навантаження, опір джерела та час усталення, а не лише ідеальне співвідношення резисторів.[^ti-voltage-divider-adc]

## Detailed explanation

Подільник напруги використовує послідовні опори, щоб отримати на середній точці частину вхідної напруги; типове застосування – масштабувати сигнал до діапазону вимірювача або входу ADC.[^adi-voltage-divider]

Для двох резисторів `R1` і `R2`, де вихід знімають з `R2`, ідеальна напруга дорівнює `Vout = Vin*R2/(R1 + R2)`. Це випливає з того, що через послідовні резистори тече той самий струм, а частка напруги на кожному дорівнює його частці в сумарному опорі. Наприклад, за `Vin = 5 V`, `R1 = 10 kΩ` і `R2 = 20 kΩ` середня точка має `3.33 V` без підключеного навантаження.[^adi-voltage-divider]

На практиці середня точка має ненульовий вихідний опір. Підключене навантаження опиняється паралельно `R2`, зменшує еквівалентний нижній опір і зазвичай знижує вихідну напругу. Через це подільник зручний для вимірювання або створення сигналу з малим струмом, але сам по собі не підходить для живлення навантаження, що споживає помітний струм.[^adi-voltage-divider]

Для батареї чи сенсора подільник може привести напругу до меж ADC, але коефіцієнт слід вибрати так, щоб максимальний вхідний рівень не перевищував дозволеної межі з урахуванням допусків і перехідних процесів. Вхід SAR ADC має конденсатор вибірки та потребує часу на заряд; завеликий вихідний опір може спричинити похибку усталення. Рекомендації залежать від конкретного ADC, частоти вибірки та схеми драйвера, тому перевіряють datasheet, а за потреби додають конденсатор або buffer amplifier.[^ti-voltage-divider-adc]

**Типова помилка:** вважати розраховану без навантаження напругу гарантованою після підключення ADC чи іншого кола. Спершу врахуйте навантаження паралельно нижньому резистору, а потім перевірте час усталення та безпечні межі входу.[^adi-voltage-divider] [^ti-voltage-divider-adc]

## Sources

<!-- generated from frontmatter -->
