---
id: emb-elee-0005
title: "Що означають SPST, SPDT, DPST і DPDT та скільки контактів має кожен?"
description: "Що означають SPST, SPDT, DPST і DPDT та скільки контактів має кожен?"
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
    applicability: "Походження питання: лекція 33, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aratas-switch-basics
    title: "ARATAS (formerly Omron): What is an Electrical Switch?"
    url: https://www.aratas.com/sg-en/products/basic-knowledge/switches/basics
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Визначення pole і throw та контактні конфігурації SPST, SPDT, DPST і DPDT; фізичні виводи конкретного корпусу можуть містити додаткові контакти."
---

## Short answer

**SPST** має один полюс і один шлях контакту, а **SPDT** – один полюс із двома виходами. DPST і DPDT керують відповідно двома однопозиційними та двома перемикальними колами одночасно; типові контактні схеми мають 2, 3, 4 і 6 клем відповідно.[^aratas-switch-basics]

## Detailed explanation

Позначення описує електричну контактну схему. Pole – це число незалежних кіл, якими перемикач керує однією дією; throw – число контактних шляхів, до яких може перейти кожен полюс. Тому SPST означає один полюс і один шлях: контакт або замикає коло, або розмикає його. У SPDT один спільний контакт перекидається між двома іншими контактами, тож для базової моделі потрібно три клеми.[^aratas-switch-basics]

Літера D означає два полюси, пов’язані одним приводом. DPST одночасно замикає або розмикає два кола, а DPDT одночасно перемикає обидва полюси між парами виходів. Саме тому поширена умовна кількість клем становить 2, 3, 4 та 6. Це не універсальний підрахунок усіх металевих виводів корпуса: підсвічування, додаткові полюси, подвійні контакти або окрема клема індикатора можуть збільшити їхню кількість.[^aratas-switch-basics]

Практичний наслідок позначення полягає у функції, а не в геометрії корпуса. SPDT можна використати для перемикання одного проводу між двома лініями; DPDT – як два синхронні SPDT, наприклад для одночасної зміни обох проводів навантаження. Позначення саме по собі не задає, які клеми розташовані поруч, де COM на корпусі, чи є центральне положення OFF і який струм безпечно комутувати. Для реального компонента звіряються зі схемою контактів і номіналами виробника.[^aratas-switch-basics]

Приклад: якщо потрібно перемикати один провід між двома сигналами, шукайте SPDT і визначте COM та обидва виходи за схемою. Якщо потрібно одночасно перемикати два проводи, потрібен DPDT, але струмовий рейтинг кожного полюса все одно має відповідати навантаженню.

**Типова помилка:** рахувати всі виводи корпуса за буквами й вважати, що клем завжди рівно стільки, скільки має базова схема. SPST/SPDT/DPST/DPDT називають конфігурацію контактів, а не точне компонування виводів чи допустиму потужність.[^aratas-switch-basics]

## Sources

<!-- generated from frontmatter -->
