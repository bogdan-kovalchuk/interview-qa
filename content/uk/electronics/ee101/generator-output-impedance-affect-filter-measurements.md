---
id: emb-elee-0105
title: "Чому вихідний опір генератора впливає на вимірювання RC-фільтра?"
description: "Чому вихідний опір генератора впливає на вимірювання RC-фільтра?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Походження питання: лекція 50, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
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
  - source_id: keysight-generator-load-termination
    title: "Keysight: Output Load Termination"
    url: https://helpfiles.keysight.com/Standalone_BenchVueSoftware_PW_HelpFiles/PWFGApp/Content/Configure%20Waveforms/Waveform%20Configuration/Output%20Load%20Termination.htm
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: Більшість описаних генераторів має послідовний вихідний опір 50 Ом; фактичний рівень залежить від імпедансу навантаження та налаштування приладу.
---

## Short answer

Вихідний опір генератора утворює подільник із вхідним імпедансом фільтра; у багатьох генераторах він становить 50 Ω, але це треба перевірити для конкретного приладу.[^keysight-generator-load-termination] Тому сигнал для передавальної характеристики слід вимірювати безпосередньо на вході фільтра, а не вважати задану амплітуду на дисплеї напругою на цьому вузлі.

## Detailed explanation

Вихідний опір генератора – це послідовний опір у еквівалентній схемі джерела, тому він разом з імпедансом під’єднаного кола визначає фактичну напругу на вході фільтра. У багатьох генераторах цей опір дорівнює 50 Ω, але значення та спосіб відображення амплітуди залежать від моделі й заданого навантаження.[^keysight-generator-load-termination]

Для простого RC-ФНЧ, якщо джерело має опір `R_s`, а резистор фільтра дорівнює `R`, конденсатор бачить сумарний послідовний опір `R_s + R`. Тому реальна частота полюса визначається цією сумою, коли вихід знімають із конденсатора, а джерело можна описати моделлю Тевенена. Вхідний рівень також може просісти, особливо якщо опір фільтра порівнянний із вихідним опором генератора.

Наприклад, налаштування генератора на амплітуду для навантаження 50 Ω не гарантує тієї самої амплітуди на вході високого імпедансу: для багатьох приладів напруга без 50-омного навантаження буде приблизно вдвічі більшою за показане значення. Це правило стосується калібрування приладу саме для такого навантаження; налаштування High-Z може змінювати показ, а не фізичну схему виходу.[^keysight-generator-load-termination]

**Типові помилки:**
- Підставляти лише резистор фільтра у формулу, не врахувавши вихідний опір джерела.
- Вважати амплітуду на дисплеї гарантованою напругою на вимірюваному вузлі.

У вимірюванні АЧХ контролюйте `V_in` саме на вході фільтра та визначайте вихідний опір генератора з документації. Так ви відокремите власну характеристику фільтра від навантаження джерела й уникнете зсуву оціненої частоти зрізу.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
