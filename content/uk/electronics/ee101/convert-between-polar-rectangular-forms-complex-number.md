---
id: emb-elee-0056
title: "Як перейти між полярною і прямокутною формами комплексного числа?"
description: "Як перейти між полярною і прямокутною формами комплексного числа?"
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
    applicability: "Походження питання: лекція 41, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-complex-polar-rectangular
    title: "All About Circuits: Polar Form and Rectangular Form Notation for Complex Numbers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/polar-rectangular-notation
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Перетворення між прямокутною і полярною формами та використання j для уявної складової в електроніці."
---

## Short answer

Для `z = a + j*b` модуль дорівнює `M = sqrt(a² + b²)`, а кут слід знаходити як `φ = atan2(b, a)`, щоб правильно врахувати квадрант. У зворотному напрямку `a = M*cos(φ)` і `b = M*sin(φ)`, тому `z = M∠φ`. В електроніці уявну одиницю позначають `j`, щоб не плутати її зі струмом `i`.[^aac-complex-polar-rectangular]

## Detailed explanation

Комплексне число можна подати прямокутно як `z = a + j*b` або полярно як `z = M∠φ`. У прямокутній формі `a` є дійсною складовою, а `b` – коефіцієнтом при уявній одиниці; у полярній `M` задає довжину вектора, а `φ` – його кут відносно додатної дійсної осі. Обидва записи описують те саме число, але кожен зручніший для певних операцій.[^aac-complex-polar-rectangular]

Для переходу з полярної форми до прямокутної проєктують вектор на осі: `a = M*cos(φ)`, `b = M*sin(φ)`. У зворотному напрямку модуль отримують за теоремою Піфагора, а кут – за двоаргументною функцією `atan2(b, a)`. Звичайний `atan(b/a)` не розрізняє точки, що лежать у протилежних квадрантах, і не визначений при `a = 0`; `atan2` повертає правильний квадрант і працює на вертикальній осі, крім випадку нульового вектора, кут якого не визначений.[^aac-complex-polar-rectangular]

Приклад: для `z = -3 + j*4` модуль дорівнює `5`, а аргумент лежить у другому квадранті – приблизно `126.9°`. Якщо механічно обчислити `atan(4/-3)`, результат буде близько `-53.1°`, тобто напрямок помилково потрапить у четвертий квадрант. Використання `atan2(4, -3)` зберігає правильний напрямок. Кути можна подавати в градусах або радіанах, але режим калькулятора має відповідати обраним одиницям.[^aac-complex-polar-rectangular]

Прямокутний запис особливо зручний для додавання і віднімання: окремо обробляють дійсні та уявні складові. Полярний запис спрощує множення і ділення: множать або ділять модулі, а кути додають або віднімають. У AC-колах після арифметики треба зберігати однакову систему одиниць фаз і посилання на спільну опору.[^aac-complex-polar-rectangular]

**Типові помилки:**

- Використовувати `atan(b/a)` без перевірки квадранту.
- Плутати коефіцієнт `b` із самою уявною складовою `j*b`.
- Додавати полярні модулі й кути напряму замість переходу до прямокутної форми.[^aac-complex-polar-rectangular]

## Sources

<!-- generated from frontmatter -->
