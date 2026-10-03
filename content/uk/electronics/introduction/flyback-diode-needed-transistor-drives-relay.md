---
id: emb-elintro-0216
title: "Навіщо потрібен flyback-діод при керуванні реле транзистором?"
description: "Навіщо потрібен flyback-діод при керуванні реле транзистором?"
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
    applicability: "Походження питання: лекція 20, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: aac-inductor-commutating
    title: "All About Circuits: Inductor commutating circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/inductor-commutating-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Пояснює індуктивний викид під час розмикання кола котушки та роботу паралельного commutating-діода; наведені приклади стосуються простого DC-кола."
  - source_id: ti-inductive-clamp
    title: "Texas Instruments: Designing for Loss of Ground and Loss of Battery on Texas Instruments High-Side Switches"
    url: https://www.ti.com/lit/pdf/slvaes9
    accessed: 2026-10-04
    kind: official
    version: "SLVAES9A, July 2020"
    applicability: "Обґрунтовує рециркуляцію струму через flyback-діод і компроміс між низьким clamp-рівнем та повільнішим спадом струму в колі з high-side switch."
---

## Short answer

Котушка реле є індуктивним навантаженням, тому її струм не може миттєво зникнути після вимикання транзистора: котушка створює напругу, що підтримує струм, і без обмеження вона може пошкодити ключ. Діод паралельно котушці дає струму шлях рециркуляції; у типовій схемі з низькобічним ключем його катод з’єднують із `+V`, а анод – зі стороною котушки біля транзистора.[^aac-inductor-commutating]

## Detailed explanation

Flyback-діод захищає ключ від перехідної напруги, що виникає при вимиканні котушки реле. Котушка зберігає енергію у магнітному полі, а зв’язок між напругою та швидкістю зміни струму описує співвідношення `v = L*di/dt`. Коли транзистор розриває коло, струм котушки прагне продовжитися в тому самому напрямку, тому полярність напруги на котушці змінюється. Без шляху для струму напруга може піднятися до рівня, небезпечного для транзистора; її величина залежить від схеми та паразитних параметрів, а не є сталою «сотнею вольт».[^aac-inductor-commutating]

Діод монтують безпосередньо паралельно котушці та орієнтують у зворотному напрямку відносно робочої напруги. Під час увімкнення він закритий і майже не впливає на струм котушки. Після вимкнення полярність на котушці змінюється, діод відкривається, і струм поступово спадає в локальному контурі «котушка – діод». Це обмежує напругу на ключі приблизно прямим падінням діода понад напругу живлення, але робить розмагнічування повільнішим; для реле це може збільшити час відпускання контактів.[^aac-inductor-commutating]

Для звичайного низькобічного NPN-ключа катод діода під’єднують до живленого кінця котушки (`+V`), анод – до кінця, що йде до колектора. Позначення «паралельно» важливе: діод не ставлять послідовно з котушкою. Також не слід вважати будь-який діод придатним автоматично: перевіряють допустимий прямий струм, імпульсні умови та зворотну напругу конкретного компонента. Швидший спад струму іноді потрібен для швидшого відпускання реле; тоді застосовують вищий clamp-рівень, наприклад правильно розраховану комбінацію діода й стабілітрона, з урахуванням граничної напруги транзистора.[^ti-inductive-clamp]

**Типова помилка:** залишити котушку без обмеження або переплутати полярність діода. У першому випадку вимикання створює великий викид, у другому діод проводить уже під час нормальної роботи й фактично закорочує живлення через котушку. Перед подачею живлення перевіряють, що в робочому режимі катод має вищий потенціал за анод, а параметри захисту узгоджені з котушкою та ключем.[^aac-inductor-commutating]

## Sources

<!-- generated from frontmatter -->
