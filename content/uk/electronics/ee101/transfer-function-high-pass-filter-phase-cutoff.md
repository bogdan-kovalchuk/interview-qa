---
id: emb-elee-0109
title: "Яка передавальна функція RC-ФВЧ і фаза на частоті зрізу?"
description: "Яка передавальна функція RC-ФВЧ і фаза на частоті зрізу?"
track: electronics
section: ee101
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
    applicability: "Походження питання: лекція 51, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-high-pass-transfer-function
    title: "All About Circuits: Understanding the First-Order High-Pass Filter Transfer Function"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-the-first-order-high-pass-filter-transfer-function/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: Передавальна функція, модуль і фазовий зсув ідеального ФВЧ першого порядку; знак фази залежить від домовленості про фазори.
---

## Short answer

Для ідеального RC-ФВЧ `H(jω) = jωRC/(1 + jωRC)`, а на частоті зрізу `f_c = 1/(2*pi*R*C)` вихід випереджає вхід на 45°.[^aac-high-pass-transfer-function] Це справедливо для навантаження, закладеного в ефективний R.

## Detailed explanation

Передавальна функція – це відношення комплексних фазорів вихідної та вхідної напруг для усталеного синусоїдального сигналу. Для ідеального RC-ФВЧ із виходом на R вона дорівнює `H(jω) = jωRC/(1 + jωRC)`, де `ω = 2*pi*f`.[^aac-high-pass-transfer-function]

Модуль показує, яка частка амплітуди входу з’являється на виході: `|H| = (f/f_c)/sqrt(1 + (f/f_c)^2)`. За частоти значно нижчої за зріз він малий, а за частоти значно вищої прямує до одиниці. Частота зрізу дорівнює `f_c = 1/(2*pi*R*C)` для ненавантаженої схеми або для R, що вже враховує ефективне навантаження.[^aac-high-pass-transfer-function]

Фаза виходу відносно входу становить `φ = 90° - arctan(f/f_c)`: на низьких частотах вона прямує до +90°, на високих – до 0°. На частоті зрізу `f = f_c` арктангенс дорівнює 45°, отже вихід випереджає вхід на 45°. У тому самому пункті амплітуда становить `1/sqrt(2)`, тобто приблизно 0.707 від максимальної, або −3 dB.[^aac-high-pass-transfer-function]

**Приклад:** якщо `R = 1 kΩ` і `C = 100 nF`, то `f_c` приблизно дорівнює `1.59 kHz`. На цій частоті синусоїдальний вихід має приблизно 70.7% амплітуди високочастотної смуги та випереджає вхід на 45° за стандартної домовленості про фазори.

**Типові помилки:**
- Приписувати ФВЧ відставання фази на 45°: знак протилежний до ФНЧ за тієї самої домовленості.
- Плутати `ω` у радіанах за секунду з `f` у герцах; між ними є множник `2*pi`.
- Застосовувати ідеальну формулу без урахування навантаження виходу.

Це частотна передавальна функція лінійного кола в усталеному режимі. Вона не описує запуск, нелінійність компонентів або паразитні параметри макета; виміряний результат може відхилятися, якщо ці ефекти істотні.

## Sources

<!-- generated from frontmatter -->
