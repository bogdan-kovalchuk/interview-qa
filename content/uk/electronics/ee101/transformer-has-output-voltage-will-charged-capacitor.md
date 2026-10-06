---
id: emb-elee-0174
title: "Трансформатор має вихід «9 В AC». Яку напругу покаже заряджений конденсатор після моста?"
description: "Трансформатор має вихід «9 В AC». Яку напругу покаже заряджений конденсатор після моста?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 64, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Розділ 3.2.3: конденсатор після випрямляча заряджається до піка вторинної обмотки (за малого навантаження вихід «пливе» до піка), пульсації зростають зі струмом навантаження, а номінальний вихід падає; розділ 3.2.4: у мостовому випрямлячі навантаження бачить напругу вторинної обмотки мінус два прямі падіння на діодах, пік дорівнює RMS*sqrt(2) (24 В RMS дає 34 В), конденсатор вибирають на пікову напругу із запасом. Падіння на кремнієвому діоді ≈ 0,7 В – наближення."
  - source_id: kuphaldt-transformer-regulation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.6 Voltage Regulation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.06:_Voltage_Regulation
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Напруга вторинної обмотки зменшується зі зростанням струму навантаження; у SPICE-прикладі 9,990 В без навантаження і 9,348 В за повного навантаження; для силового трансформатора з резистивним навантаженням добрим вважають регулювання менше 3 %, індуктивне навантаження погіршує. Числа з прикладу не є параметрами реального трансформатора."
  - source_id: vishay-1n400x
    title: "Vishay: 1N4001–1N4007 datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
    accessed: 2026-10-06
    kind: official
    version: "29-Apr-2020"
    applicability: "Максимальне миттєве пряме падіння VF = 1,1 В за струму 1,0 А (TA = 25 °C) для серії 1N4001–1N4007; для інших діодів і струмів падіння інше."
---

## Short answer

Без навантаження приблизно 11,3 В, а не 9 В: 9 В – діюче значення, пік `9*sqrt(2) ≈ 12,73 В`, мінус два падіння на діодах моста, `2*0,7 В = 1,4 В`.[^fiore-rectification] Під навантаженням напруга матиме пульсації й просідання, а сама напруга вторинної обмотки трансформатора теж залежить від навантаження.[^fiore-rectification][^kuphaldt-transformer-regulation]

## Detailed explanation

Запис «9 В AC» – це діюче значення (RMS), а конденсатор після випрямляча заряджається до піка, а не до RMS. Для синусоїди пік у `sqrt(2)` разів більший за RMS: `9*1,414 ≈ 12,73 В`. У мостовому випрямлячі в кожен момент проводять два діоди, тож навантаження бачить напругу вторинної обмотки мінус два прямі падіння; за наближення `0,7 В` на діод це `12,73 − 1,4 ≈ 11,33 В`.[^fiore-rectification] Саме це число й має показати вольтметр постійного струму на конденсаторі без навантаження: за малого навантаження вихід «пливе» до піка вторинної обмотки.[^fiore-rectification]

Падіння `0,7 В` – лише наближення. У datasheet 1N4001–1N4007 максимальне миттєве пряме падіння за струму 1 А дорівнює 1,1 В.[^vishay-1n400x] Якщо припустити саме це значення на кожному з двох діодів, то `12,73 − 2*1,1 ≈ 10,5 В` – оцінка знизу для моста на таких діодах за струму 1 А; за менших струмів падіння менше, тож результат лежить між `10,5 В` і `11,3 В`.

Під навантаженням напруга на конденсаторі перестає бути сталою. Між піками діоди не проводять, конденсатор розряджається в навантаження, і це дає пульсації; їхня амплітуда зростає зі струмом навантаження, а середня напруга падає.[^fiore-rectification] Груба оцінка з визначення ємності: за струму `0,1 А`, `C = 1000 мкФ` і найгіршого проміжку без заряджання близько `10 мс` (півперіоду мережі 50 Hz) спад становить `0,1*0,01/0,001 ≈ 1 В`, тобто напруга коливається приблизно між `11,3 В` і `10,3 В`, якщо вторинна напруга незмінна.

Але й вторинна напруга не лишається сталою. У трансформатора напруга вторинної обмотки зменшується зі зростанням струму: у прикладі SPICE із джерела вона дорівнює 9,990 В без навантаження і 9,348 В за повного, тобто на холостому ході вона приблизно на `(9,990 − 9,348)/9,348 ≈ 6,9 %` вища.[^kuphaldt-transformer-regulation] Якщо припустити таку саму різницю для нашого трансформатора і вважати, що «9 В» стосується повного навантаження, то без навантаження вторинна дасть `9*1,069 ≈ 9,6 В RMS`, пік `≈ 13,6 В`, а на конденсаторі буде приблизно `13,6 − 1,4 ≈ 12,2 В`. Це лише ілюстрація: реальне регулювання залежить від трансформатора, а добрий силовий трансформатор із резистивним навантаженням має регулювання менше 3 %.[^kuphaldt-transformer-regulation] Так само змінюється результат і зі зміною напруги мережі.

**Типові помилки:**

- Вважати «9 В AC» постійною напругою або пікове значення плутати з RMS: конденсатор заряджається до піка `RMS*sqrt(2)`.[^fiore-rectification]
- Забути про два падіння на діодах моста: у мосту їх два, а не одне.[^fiore-rectification]
- Вибрати конденсатор на напругу, близьку до RMS: його вибирають на пікову напругу, з запасом, а за малого навантаження вихід досягає піка.[^fiore-rectification]
- Розраховувати на номінальні 9 В без урахування залежності напруги трансформатора від навантаження.[^kuphaldt-transformer-regulation]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
