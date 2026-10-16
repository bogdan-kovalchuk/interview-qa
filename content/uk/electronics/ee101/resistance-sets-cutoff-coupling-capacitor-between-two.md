---
id: emb-elee-0207
title: "Який опір визначає зріз розділового конденсатора між двома каскадами?"
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
  - source_id: fiore-multi-stage-amplifiers
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.6 Multi-Stage Amplifiers"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.6:_Multi-Stage_Amplifiers
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
---

## Short answer

Частоту зрізу задає сума опорів, які бачить конденсатор з обох боків: вихідного опору першого каскаду і вхідного опору другого, а не лише `R_E`.[^fiore-multi-stage-amplifiers][^fiore-common-emitter-amplifier] Для RC-ланки `f_c = 1/(2*pi*R*C)`, а на f_c підсилення на 3 дБ нижче середньосмугового.[^fiore-ac-circuit-analysis]

## Detailed explanation

Розділовий конденсатор між каскадами разом з опорами, які він бачить з обох боків, утворює ФВЧ. Зліва видно вихідний опір першого каскаду. Для каскаду зі спільним емітером `Z_out ≈ R_C`, бо внутрішній опір колекторного джерела струму великий.[^fiore-common-emitter-amplifier] Справа видно вхідний опір другого каскаду, який для першого є навантаженням.[^fiore-multi-stage-amplifiers] Для змінного сигналу ці два опори стоять послідовно з конденсатором, тож `R = Z_out + Z_in` і `f_c = 1/(2*pi*R*C)`.[^fiore-ac-circuit-analysis]

Приклад: `R_C = 4,7 кОм` – колекторний резистор першого каскаду, вхідний опір другого каскаду `Z_in = 10 кОм` (він уже враховує його `R_B ∥ β(r_e + r_E)`), `C = 1 мкФ`. Тоді `R = 14,7 кОм`, а `f_c = 1/(2*pi*14700*1e-6)` ≈ 10,8 Гц. Якщо взяти замість цього лише `R_E = 470 Ом` другого каскаду, виходить `1/(2*pi*470*1e-6)` ≈ 339 Гц, тобто приблизно в тридцять разів більше. Але `R_E` не стоїть послідовно з `C`: він входить лише опосередковано, через `Z_in` другого каскаду, тож оцінка за самим `R_E` хибна.

На частоті зрізу підсилення на 3 дБ менше за середньосмугове, а нижче зрізу воно спадає приблизно на 6 дБ на октаву.[^fiore-ac-circuit-analysis] Тому формули середньої смуги, наприклад `A_v = -r_C/(r_e + r_E)`, правильні лише значно вище `f_c`, де втрати на конденсаторі малі.[^fiore-common-emitter-amplifier]

**Типові помилки:**

- Оцінювати зріз лише за `R_E`, коли він не стоїть у ланці конденсатора.
- Не враховувати вихідний опір попереднього каскаду з боку конденсатора.
- Забувати, що `f_c` залежить від обох величин, `C` і повного `R` ланки, а не лише від одного з них.
