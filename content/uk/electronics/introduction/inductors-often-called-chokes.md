---
id: emb-elintro-0148
title: "Чому індуктори часто називають choke?"
description: "Чому індуктори часто називають choke?"
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
    applicability: "Походження питання: лекція 14, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-inductor-choke
    title: "All About Circuits: Magnetic Fields and Inductance"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/magnetic-fields-and-inductance/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Походження назви choke та типове використання індуктора для послаблення високочастотних AC-сигналів; термін історичний і не обмежує тип компонента."
---

## Short answer

Назва choke (дросель) пов’язана з використанням індуктора для послаблення небажаних високочастотних AC-сигналів. Це назва за застосуванням, а не окремий фізичний тип компонента; реакція конкретного індуктора залежить від частоти та його реальних паразитних параметрів.[^aac-inductor-choke]

## Detailed explanation

Індуктор створює напругу, що протидіє зміні струму, який проходить через обмотку. У фільтрі ця властивість допомагає зменшувати пульсації або перешкоди змінного струму, тому індуктор, призначений для такого застосування, називають choke, або дроселем. Назва описує функцію в колі, а не спеціальну конструкцію: дросель усе одно є індуктором.[^aac-inductor-choke]

Для ідеального індуктора модуль індуктивного опору синусоїдальному сигналу зростає з частотою: `X_L = 2π*f*L`. Це пояснює, чому послідовний індуктор може краще протидіяти високочастотній складовій, ніж зміні струму з низькою частотою. У фільтрі живлення дросель може зменшувати AC-пульсацію, водночас пропускаючи корисний DC-струм після перехідного процесу. Він не «проводить лише DC»: змінна складова також проходить, але її поведінка визначається повним імпедансом схеми.[^aac-inductor-choke]

**Приклад:** у вихідному фільтрі випрямляча послідовний дросель протидіє пульсації струму, а конденсатор шунтує частину AC-пульсації на землю. Результат залежить від номіналів, частоти пульсацій і навантаження, тому одна котушка не гарантує потрібного ослаблення в будь-якому колі. Реальні обмотки мають опір, а паразитна ємність може спричиняти резонанс; на достатньо високих частотах проста модель ідеальної індуктивності вже непридатна.[^aac-inductor-choke]

У сучасній технічній мові частіше вживають загальне слово «індуктор», а «choke» лишається поширеною назвою компонента, коли йдеться про фільтрацію або придушення певних сигналів. Під час вибору важливо дивитися на призначення й характеристики конкретного компонента, а не робити висновок лише з назви.[^aac-inductor-choke]

## Sources

<!-- generated from frontmatter -->
