---
id: emb-elintro-0124
title: "Як температура впливає на пряму напругу LED?"
description: "Як температура впливає на пряму напругу LED?"
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
    applicability: "Походження питання: лекція 12, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: kingbright-wp154a4
    title: "Kingbright WP154A4SEJ3VBDZGC/CA datasheet"
    url: https://www.kingbrightusa.com/images/catalog/SPEC/WP154A4SEJ3VBDZGC-CA.pdf
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Datasheet LED Kingbright WP154A4SEJ3VBDZGC/CA: V_R = 5 V, температурний коефіцієнт V_F −2.0 mV/°C (Hyper Red) за I_F = 20 mA."
---

## Short answer

Із нагріванням `V_f` багатьох LED зменшується; для червоного Kingbright WP154A4SEJ3VBDZGC/CA вказано коефіцієнт −2.0 mV/°C за `I_F = 20 mA`.[^kingbright-wp154a4] У колі з джерелом напруги та резистором це може збільшити струм, тоді як constant-current driver підтримує заданий струм у межах робочого діапазону.[^kingbright-wp154a4]

## Detailed explanation

Пряма напруга `V_f` залежить від температури переходу, і для багатьох LED вона зменшується при нагріванні. Знак і величина коефіцієнта залежать від типу компонента та робочого струму, тому числове значення слід брати з datasheet, а не переносити з одного LED на всі інші.[^aac-semiconductors]

У простому колі з джерелом напруги й послідовним резистором струм приблизно задається різницею напруг живлення та `V_f`, поділеною на опір. Якщо `V_f` падає, на резисторі лишається більша напруга, і струм зростає. Це може створювати позитивний зворотний зв’язок через нагрівання, але його сила залежить від резистора, тепловідведення та режиму; thermal runaway не є неминучим у кожному колі.[^aac-semiconductors]

Для конкретного прикладу datasheet Kingbright WP154A4SEJ3VBDZGC/CA наводить коефіцієнт `−2.0 mV/°C` для червоного варіанта при `I_F = 20 mA`. Зміна температури переходу на 10 °C відповідає приблизно `−20 mV` зміни `V_f` за умов datasheet; це не можна без перевірки застосовувати до інших кольорів, струмів чи деталей.[^kingbright-wp154a4]

Регульований за струмом драйвер компенсує зміну `V_f`, поки має достатній запас вихідної напруги. Він не скасовує зниження допустимого струму при високій температурі: потрібне теплове проєктування та дотримання обмежень виробника.[^aac-semiconductors]

## Sources

<!-- generated from frontmatter -->
