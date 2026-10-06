---
id: emb-elee-0170
title: "Чому для деяких LDO важливий ESR вихідного конденсатора?"
description: "Чому для деяких LDO важливий ESR вихідного конденсатора?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Походження питання: лекція 63, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: ti-slva115
    title: "Texas Instruments SLVA115A: ESR, Stability, and the LDO Regulator"
    url: https://www.ti.com/lit/an/slva115/slva115.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA115A, February 2020"
    applicability: "LDO з PMOS або PNP pass element: три полюси розімкненої петлі (домінантний, load pole, pass-device pole), нуль від ESR вихідного конденсатора `f_Z = 1/(2*pi*ESR*C_out)`, умова на ESR знизу й зверху, переваги вимірювання перехідної характеристики, приклад із осциляціями для 2,2 мкФ кераміки й стабільним режимом із додатковим 1 Ω, нові LDO для кераміки. Записка про LDO зазначених типів; числовий приклад у записці дає для 0,1 Ω і 2,2 мкФ значення 72,3 кГц, яке не збігається з формулою (за нею вийшло б близько 723 кГц), тому тут числа не беруться."
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Конкретний LDO: мінімальна ємність 47 мкФ і ESR від 100 мОм до 10 Ω, примітка, що ESR включає зовнішній послідовний опір і опір доріжки до C_O, та висновок, що вищий ESR дає більше просідання на початку стрибка навантаження. Значення стосуються лише TPS752-Q1 і TPS754xx."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Розділ 10: стабільна область compensation series resistance `CSR = R_ESR + R_add` залежить від струму навантаження (tunnel of death), додатковий резистор можна ввести, якщо ESR замалий; діапазон 0,2–9 Ω наведено як приклад. Записка про LDO; межі є прикладом, а не універсальними."
---

## Short answer

У LDO з PMOS або PNP pass element ESR вихідного конденсатора створює нуль, який компенсує полюси петлі зворотного зв’язку, тому datasheet задає допустимий діапазон ESR і мінімальну ємність.[^ti-slva115][^ti-tps752q1-datasheet] Надто малий ESR (як у кераміки) може залишити петлю без компенсації, надто великий – порушити її на високих частотах; в обох випадках є ризик нестабільності. Високий ESR також збільшує просідання напруги під час стрибка струму.[^ti-tps752q1-datasheet]

## Detailed explanation

LDO – це замкнена система зі зворотним зв’язком: error amplifier порівнює вихід з опорною напругою й керує pass element, а вихідний конденсатор разом із навантаженням входить у цю петлю. У LDO з PMOS або PNP pass element в розімкненій петлі є три важливі полюси: домінантний (в error amplifier), полюс навантаження (його задають вихідний конденсатор і навантаження, тому він зсувається зі струмом) та полюс pass element (паразитна ємність цього елемента). Три полюси за високого підсилення без компенсації не дають достатнього phase margin, а найпростіше джерело компенсації – нуль, який створює ESR конденсатора, що LDO однаково потребує.[^ti-slva115]

Частота цього нуля `f_Z = 1/(2*pi*ESR*C_out)`. ESR має бути достатньо великим, щоб нуль опустився й нахил АЧХ у точці перетину 0 dB став –20 dB/dec замість –40 dB/dec, і достатньо малим, щоб підсилення впало нижче 0 dB ще до полюса pass element.[^ti-slva115] Для `C_out = 2,2 мкФ` і `ESR = 1 Ω` маємо `f_Z ≈ 72 kHz`, а для керамічного конденсатора з `ESR = 10 мОм` – `f_Z ≈ 7,2 MHz`, тобто у 100 разів вище. Де саме лежить частота перетину конкретної петлі, залежить від мікросхеми, тож у другому випадку нуль, імовірно, надто високо, щоб змінити нахил АЧХ у точці перетину.

Тому в datasheet подається не лише мінімальна ємність, а й допустимий ESR. Для TPS752-Q1 це щонайменше 47 мкФ і ESR від 100 мОм до 10 Ω, причому ESR там означає повний послідовний опір, разом із зовнішнім резистором і опором доріжки до конденсатора.[^ti-tps752q1-datasheet] У SLVA079 цю суму названо compensation series resistance, `CSR = R_ESR + R_add`, а її стабільну область показують залежно від струму навантаження (tunnel of death); якщо ESR замалий, додають послідовний резистор.[^ti-slva079] У SLVA115 для TPS76050 із керамікою 2,2 мкФ після стрибка струму видно багаторазові осциляції, а з додатковим 1 Ω перехідна характеристика стабільна; ESR у таких графіках береться мінімальний, бо він змінюється з частотою.[^ti-slva115]

Є й зворотний бік. У момент стрибка струму навантаження LDO ще не встигає відреагувати, і струм віддає конденсатор, тож на його ESR падає `V_ESR = I*ESR`, і чим вищий ESR, тим більше початкове просідання.[^ti-tps752q1-datasheet] Для стрибка 0,5 A це 0,5 В за `ESR = 1 Ω` і лише 5 мВ за `ESR = 10 мОм`. Нові LDO проєктують так, щоб вони були стабільні з керамікою без додаткового ESR, і для них умова на ESR зазвичай не лімітує вибір, але це перевіряють у datasheet конкретної мікросхеми, а не припускають.[^ti-slva115]

**Типові помилки:**

- Замінювати танталовий чи електролітичний конденсатор керамічним тієї самої ємності для LDO старішого типу, не перевіривши вимоги до ESR.[^ti-slva115]
- Вважати, що чим менший ESR, тим краще: у таких LDO ESR має й нижню межу.[^ti-tps752q1-datasheet]
- Не враховувати, що ESR у datasheet включає опір доріжки та додаткові резистори, і перевіряти стабільність лише за номіналом конденсатора.[^ti-tps752q1-datasheet]
- Приймати стабільність без вимірювання перехідної характеристики: багаторазові осциляції після стрибка струму вказують на брак phase margin.[^ti-slva115]

## Sources

<!-- generated from frontmatter -->
