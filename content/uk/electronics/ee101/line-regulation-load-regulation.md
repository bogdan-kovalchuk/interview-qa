---
id: emb-elee-0141
title: "Що таке line regulation і load regulation?"
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

Line regulation показує, наскільки змінюється вихідна напруга при зміні вхідної за сталого навантаження: `ΔV_out/ΔV_in`. Load regulation – наскільки вона змінюється при зміні струму навантаження за сталої вхідної напруги: `ΔV_out/ΔI_out`.[^ti-slva079] Обидва параметри усталені, тож не описують перехідні процеси, а менше значення за модулем означає кращу стабілізацію.[^ti-slva079]

## Detailed explanation

Будь-який стабілізатор має тримати вихід сталим, хоча зовні змінюється кілька речей. Дві головні – вхідна напруга й струм навантаження, і кожній відповідає свій параметр. Line regulation – реакція виходу на зміну входу за сталого навантаження, `ΔV_out/ΔV_in`. Load regulation – реакція на зміну струму за сталої вхідної напруги, `ΔV_out/ΔI_out`.[^ti-slva079] За означенням перший параметр безрозмірний (наприклад, мВ/В), а другий має розмірність опору (мВ/мА = Ом): це статичний вихідний опір стабілізатора.

Ці параметри усталені: вони описують нове стале значення виходу, а не те, як воно встановлюється. Швидкість і викиди після стрибка входу чи струму – окрема характеристика (transient response).[^ti-slva079] У лінійного стабілізатора обидва числа залежать від коефіцієнта підсилення розімкненої петлі: що він більший, то кращі line і load regulation.[^ti-slva079] Скінченне підсилення петлі – одна з причин, чому ці параметри не нульові.

**Приклад: простий стабілітронний стабілізатор.** Стабілітрон має скінченний динамічний опір `r_Z = ΔV_Z/ΔI_Z`.[^nexperia-an90031] Приймемо модель `V_out = V_Z + r_Z*I_Z` і `I_Z = (V_in - V_out)/R - I_load`. Тоді для малих змін `ΔV_out/ΔV_in = r_Z/(R + r_Z)` і `ΔV_out/ΔI_load = -(R*r_Z)/(R + r_Z)`. Для BZX84-C5V1 максимум `r_Z` при 5 мА – 60 Ом,[^nexperia-bzx84] а `R = 390 Ом`. Звідси line regulation `≤ 60/450 ≈ 0.13`, тобто 1 В зміни входу дає до 133 мВ зміни виходу. Load regulation за модулем `≤ 60*390/450 = 52 Ом`: зміна струму навантаження на 1 мА дає до 52 мВ. Це оцінка зверху для робочої точки біля 5 мА. Якби стабілітрон працював біля 1 мА, де максимум `r_Z` дорівнює 480 Ом,[^nexperia-bzx84] то `ΔV_out/ΔV_in` зросло б до `480/870 ≈ 0.55`, а load regulation – до `480*390/870 ≈ 215 Ом`.

**Умови.** Обидва параметри мають сенс, лише поки стабілізатор у режимі стабілізації. Якщо навантаження забирає майже весь струм резистора, стабілітрон перестає проводити, регуляція зникає, а резистор із навантаженням працюють як дільник напруги (див. qid:emb-elee-0143).[^fiore-rectification] Значення з datasheet прив’язані до конкретних діапазонів входу й струму, тож їх не можна переносити на інші умови.

**Типові помилки:**

- Плутати line і load regulation: перша стосується зміни входу, друга – зміни струму навантаження.
- Порівнювати load regulation без урахування діапазону `ΔI_out`, за якого його задано.
- Вважати їх описом перехідних процесів, а не усталеного значення.
- Очікувати такої стабілізації поза режимом: зі стабілітроном без струму або при просіданні входу нижче допустимого.
