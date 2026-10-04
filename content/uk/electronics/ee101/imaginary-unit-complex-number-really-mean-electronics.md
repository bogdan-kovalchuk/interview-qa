---
id: emb-elee-0067
title: "Що таке уявна одиниця j і що насправді означає комплексне число a + jb в електроніці?"
description: "Що таке уявна одиниця j і що насправді означає комплексне число a + jb в електроніці?"
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
    applicability: "Походження питання: лекція 43, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: AC-кола, реактивний опір, фазори, імпеданс, фільтри й трансформатори; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-complex-intro
    title: "All About Circuits: Introduction to Complex Numbers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-2/introduction-to-complex-numbers/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює комплексне подання амплітуди й фази AC; не стверджує, що уявна складова є окремою фізичною напругою."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
---

## Short answer

`j² = -1`. У комплексному фазорі дійсна й уявна складові є координатами, що кодують амплітуду та фазу синусоїдальної величини. Тому «уявна напруга» не є окремою фізичною напругою.[^aac-complex-intro]

## Detailed explanation

У електротехніці `j` позначає уявну одиницю, що задовольняє `j² = -1`; літеру `j` використовують, щоб не плутати її з поширеним позначенням струму `i`. У записі `a + jb` числа `a` та `b` задають координати комплексного числа: `a` – дійсну, `b` – уявну. Це математичне подання, а не твердження про два фізично незалежні види напруги.[^aac-complex-intro]

Для синусоїдального AC однієї частоти фазор зберігає дві потрібні характеристики – величину та фазу відносно опорного сигналу. Наприклад, `3 + j4` відповідає точці з координатами `3` і `4`; її модуль дорівнює `5`, а кут приблизно `53.13°`. Та сама величина в полярному записі – `5∠53.13°`. Обидва записи описують одну комплексну величину, лише в різних координатах.[^aac-complex-intro]

У часовій області фізична напруга залишається дійсною синусоїдою. Фазорний запис є компактним обчислювальним інструментом: після розв’язання комплексні координати інтерпретують як амплітуду та фазове співвідношення, а за потреби відновлюють часову форму. Значення `j` тут не є «уявною» частиною вимірювання мультиметра.[^aac-complex-intro]

**Типові помилки:**

- Вважати `j` фізичною змінною або уявляти вимірювану напругу як нереальну.
- Плутати `b` з модулем: у `a + jb` це координата; модуль знаходять з обох координат.
- Використовувати фазор без спільної частоти й опорного кута.[^aac-complex-intro]

## Sources

<!-- generated from frontmatter -->
