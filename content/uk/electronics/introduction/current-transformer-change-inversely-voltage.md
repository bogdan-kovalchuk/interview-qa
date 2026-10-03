---
id: emb-elintro-0158
title: "Чому у трансформаторі струм змінюється обернено до напруги?"
description: "Чому у трансформаторі струм змінюється обернено до напруги?"
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
    applicability: "Походження питання: лекція 15, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: electronics-tutorials-transformer-basics
    title: "Electronics Tutorials: Transformer Basics and Transformer Principles"
    url: https://www.electronics-tutorials.ws/transformer/transformer-basics.html
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Ідеальний баланс потужності та обернене співвідношення напруги й струму; реальний трансформатор має втрати."
---

## Short answer

В ідеальному трансформаторі вхідна й вихідна потужності рівні: `V1*I1 = V2*I2`. Тому збільшення напруги у 10 разів відповідає приблизно десятикратному зменшенню струму для тієї самої переданої потужності; у реальному трансформаторі вихідна потужність трохи менша через втрати.[^electronics-tutorials-transformer-basics]

## Detailed explanation

В ідеальному трансформаторі вища напруга на одній обмотці відповідає меншому струму в ній, якщо трансформатор передає ту саму потужність. Причина – збереження потужності в ідеальній моделі: `P1 = P2`, а для активного навантаження миттєву або середню потужність описують добутком напруги та струму.[^electronics-tutorials-transformer-basics]

Оскільки напруга пропорційна числу витків, струми обмоток мають обернене співвідношення: для ідеального трансформатора `V2/V1 = N2/N1`, а `I2/I1 = N1/N2`. Це не означає, що енергія виникає безкоштовно: трансформатор змінює співвідношення напруги й струму, а не створює потужність.[^electronics-tutorials-transformer-basics]

Наприклад, якщо ідеальний трансформатор підвищує напругу з `12 V` до `120 V`, то за вхідного струму `1 A` вихідний струм становить приблизно `0.1 A`, якщо знехтувати втратами й фазовими ефектами навантаження. Перевірка: `12 V*1 A = 120 V*0.1 A = 12 W`. Це приклад для ідеальної моделі; реальний вихідний струм буде нижчим через втрати в осерді й обмотках.[^electronics-tutorials-transformer-basics]

У реальному AC-колі важливо розрізняти повну потужність у VA та активну потужність у W: коефіцієнт потужності навантаження впливає на їхнє співвідношення. Крім того, номінал трансформатора обмежує допустиму VA-потужність і струм; одного бажаного коефіцієнта трансформації недостатньо для вибору компонента.[^electronics-tutorials-transformer-basics]

**Типова помилка:** робити висновок, що при підвищенні напруги трансформатор збільшує доступну потужність. У найкращому разі потужність передається майже без втрат, а в реальному пристрої вихідна потужність дещо менша за вхідну.[^electronics-tutorials-transformer-basics]

## Sources

<!-- generated from frontmatter -->
