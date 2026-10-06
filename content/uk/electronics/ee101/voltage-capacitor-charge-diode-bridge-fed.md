---
id: emb-elee-0129
title: "До якої напруги зарядиться конденсатор після діодного моста від джерела 6 В RMS?"
description: "До якої напруги зарядиться конденсатор після діодного моста від джерела 6 В RMS?"
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
    applicability: "Походження питання: лекція 55, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-06; курс не є доказом цих тверджень."
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
  - source_id: libretexts-fiore-rectification
    title: "Fiore: Semiconductor Devices, 3.2 Rectification (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Однопівперіодний випрямляч, двопівперіодний із середньою точкою та мостовий: які діоди проводять у кожному півперіоді, падіння на двох діодах моста, конденсатор згладжування й імпульси зарядного струму. Підручник використовує типові 0,7 В на діод; це не заміняє datasheet конкретного діода."
  - source_id: vishay-1n4001
    title: "Vishay: 1N4001 to 1N4007 general purpose plastic rectifier datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
    accessed: 2026-10-06
    kind: official
    version: "Revision 29-Apr-2020"
    applicability: "Максимальне V_F 1,1 В за 1 А (25 °C); I_R до 5 мкА за 25 °C і до 50 мкА за 125 °C за номінальної зворотної напруги; V_RRM від 50 до 1000 В залежно від типу. Стосується цієї серії випрямних діодів."
---

## Short answer

Для синусоїдального джерела `V_peak = sqrt(2)*6 ≈ 8.49 В`. Мінус два падіння по 0,7 В: `V_C,max ≈ V_peak - 2*V_F ≈ 7.09 В`.[^libretexts-fiore-rectification] Це оцінка для малого струму: за більшого струму `V_F` зростає (для 1N4001 до 1,1 В за 1 А), тож напруга буде нижчою.[^vishay-1n4001]

## Detailed explanation

6 В RMS – це діюче значення, а конденсатор заряджається до амплітуди. Для синусоїди `V_peak = sqrt(2)*V_RMS`, тож `V_peak = 1.41421*6 ≈ 8.485 В`. Саме ця амплітуда, а не 6 В, є верхньою межею напруги, до якої діодний міст міг би зарядити конденсатор, якби діоди були ідеальними.

У мості в кожен півперіод струм іде крізь два діоди послідовно, тому навантаження й конденсатор «бачать» вторинну напругу мінус два прямі падіння.[^libretexts-fiore-rectification] Конденсатор заряджається, доки його напруга не зрівняється з `V_peak - 2*V_F`; після піку діоди зміщуються у зворотному напрямку, і конденсатор лишається зарядженим. При `V_F = 0.7 В` маємо `V_C,max ≈ 8.485 - 2*0.7 = 7.085 ≈ 7.09 В`. За малого навантаження вихід «пливе» до піку вторинної напруги майже без пульсацій, а зі зростанням струму навантаження пульсації збільшуються, а номінальна вихідна напруга падає.[^libretexts-fiore-rectification]

Результат 7,09 В залежить від припущення про `V_F`. Напруга 0,7 В – наближення, а реальне падіння залежить від діода й струму (див. qid:emb-elee-0127). Заряджання відбувається короткими імпульсами струму біля піку: у симуляції підручника (однопівперіодний випрямляч, джерело 10 В, навантаження 100 Ω) для 1000 мкФ імпульс сягає приблизно 800 мА за тривалості близько 2,5 мс, значно вище середнього струму навантаження.[^libretexts-fiore-rectification] Для 1N4001 максимальне `V_F` за 1 А – 1,1 В,[^vishay-1n4001] тоді оцінка стає `8.485 - 2*1.1 ≈ 6.29 В` (це нижня оцінка за максимальними значеннями datasheet, а не типове число). Тобто реалістичний діапазон – приблизно від 6,3 до 7,1 В, і точну відповідь дає лише розрахунок або вимірювання для конкретних діодів і струму.

Конденсатор має бути розрахований на пік, а не на RMS: підручник у схожому прикладі бере 50 В для піку близько 34 В, тобто з великим запасом.[^libretexts-fiore-rectification] Для амплітуди 8,49 В стандартного номіналу на 6,3 В замало, потрібен більший номінал за напругою.

**Типові помилки:**

- Вважати, що конденсатор зарядиться до 6 В або до `V_peak` без падіння на діодах.
- Віднімати лише одне падіння `V_F`, а не два, хоча в мосту послідовно працюють два діоди.
- Використовувати множник `sqrt(2)` для несинусоїдальної напруги або вважати 7,09 В гарантованою напругою під навантаженням.

## Sources

<!-- generated from frontmatter -->
