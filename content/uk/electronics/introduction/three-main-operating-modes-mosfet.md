---
id: emb-elintro-0241
title: "Які три основні режими роботи MOSFET?"
description: "Які три основні режими роботи MOSFET?"
track: electronics
section: introduction
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
    applicability: "Походження питання: лекція 22, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: toshiba-mosfet-drive
    title: "Toshiba: MOSFET Gate Drive Circuit, Application Note"
    url: https://toshiba.semicon-storage.com/info/TPH4R50ANH1_application_note_en_20180726_AKX00068.pdf?did=59460&prodName=TPH4R50ANH1
    accessed: 2026-10-04
    kind: official
    version: "AKX00068-1, 2018-07-26"
    applicability: "Режими роботи MOSFET, умови відкривання, залежність R_DS(on) від V_GS і температури та втрати перемикання."
---

## Short answer

У enhancement-mode MOSFET розрізняють `cutoff`, `linear/triode` та `saturation`: нижче порогового `V_GS` канал майже не проводить, у `linear` він має малий опір і придатний для ключа, а в `saturation` струм слабше залежить від `V_DS`, що корисно для підсилення. Поріг не є межею нульового струму, а умови режиму залежать від полярності й типу транзистора.[^toshiba-mosfet-drive]

## Detailed explanation

Режими роботи enhancement-mode MOSFET описують, як напруга між затвором і витоком та напруга між стоком і витоком визначають струм каналу. Назви `cutoff`, `linear` і `saturation` стосуються різних ділянок вихідних характеристик, а не трьох окремих типів транзистора.[^toshiba-mosfet-drive]

У `cutoff` напруга `V_GS` недостатня для формування провідного каналу. Для реального компонента це означає малий струм витоку, а не математично нульовий струм; значення `V_th` у datasheet вимірюють за заданих умов і воно не обіцяє малого опору каналу при великих навантаженнях. Щоб MOSFET став добрим ключем, його затвор треба керувати напругою, за якої datasheet задає `R_DS(on)`.[^toshiba-mosfet-drive]

У `linear` або `triode` канал сформований, а `V_DS` мале порівняно з надлишком керування затвором. У цій області канал поводиться приблизно як керований резистор, тому саме тут працює повністю ввімкнений силовий ключ. Назва `linear` описує ділянку характеристик; вона не означає, що компонент завжди працює як лінійний підсилювач.[^toshiba-mosfet-drive]

У `saturation` канал біля стоку переживає pinch-off, і зі зростанням `V_DS` струм у простій моделі змінюється слабше, ніж у лінійній області. Це корисна область для підсилення, але вона не є бажаним «повністю ввімкненим» режимом силового ключа: за того самого струму напруга на транзисторі та розсіювана потужність можуть бути значними.[^toshiba-mosfet-drive]

Приклад: у типовому низькобічному ключі достатнє `V_GS` переводить MOSFET у `linear` область із малим падінням напруги; при вимкненому керуванні він переходить у `cutoff`. Перевіряйте потрібну напругу затвора за умовами, для яких виробник гарантує опір, і не робіть висновок про струм за одним лише `V_th`.[^toshiba-mosfet-drive]

**Типова помилка:** називати режим `saturation` станом «насиченого, повністю відкритого ключа». Для MOSFET це назва області pinch-off; потрібний для ключа малий опір має область `linear/triode`.[^toshiba-mosfet-drive]

## Sources

<!-- generated from frontmatter -->
