---
id: emb-elintro-0155
title: "Що таке center tap трансформатора і де він використовується?"
description: "Що таке center tap трансформатора і де він використовується?"
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
  - source_id: aac-center-tap-rectifier
    title: "All About Circuits: Rectifier Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/rectifier-circuits/
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Робота дводіодного двопівперіодного випрямляча з center-tapped secondary; інші застосування залежать від схеми."
---

## Short answer

Center tap – це електричний відвід від середини обмотки, який ділить її на дві приблизно однакові секції. Якщо його обрати за спільну точку відліку, кінці секцій мають протилежні фази й рівні за модулем напруги, наприклад +12 V і −12 V відносно відводу, якщо кожна половина дає 12 V. Center tap також дає змогу побудувати дводіодний двопівперіодний випрямляч; потрібна напруга визначається номіналом обмотки та схемою.[^aac-center-tap-rectifier]

## Detailed explanation

Center tap – це провідний відвід від проміжної точки обмотки. У рівномірно намотаній вторинній обмотці, відвід посередині ділить її приблизно навпіл, тому кожна половина має близьку кількість витків і створює близьку напругу відносно center tap. Миттєві напруги на двох кінцях мають протилежні фази. Назви на кшталт 12-0-12 V зазвичай означають 12 V RMS від відводу до кожного краю і 24 V RMS між краями; завжди перевіряють паспорт конкретного трансформатора.[^aac-center-tap-rectifier]

Відвід часто обирають спільною точкою або умовним нулем у двополярному живленні. Тоді відносно нього напруга на крайніх виводах змінюється з протилежними знаками; після випрямлення та фільтрації можна отримати позитивну й негативну шини. Сам center tap не є землею автоматично – це залежить від того, як його з’єднано в схемі.[^aac-center-tap-rectifier]

Інше поширене застосування – дводіодний двопівперіодний випрямляч. У кожну півхвилю проводить свій діод і відповідна половина вторинної обмотки, тож струм через навантаження має той самий напрямок в обох півперіодах. Така схема використовує лише половину обмотки в конкретний момент, а також вимагає трансформатора з відводом; містковий випрямляч натомість застосовує чотири діоди й може працювати без center tap.[^aac-center-tap-rectifier]

Приклад: якщо на обмотці вказано 12-0-12 V AC, між кожним краєм і відводом буде близько 12 V RMS, а між крайніми виводами – близько 24 V RMS без навантаження або за паспортних умов. Після випрямлення пікові значення відрізнятимуться від RMS і залежатимуть від діодів та фільтра.[^aac-center-tap-rectifier]

**Типові помилки:**
- називати center tap окремою обмоткою;
- трактувати його як землю незалежно від підключення;
- плутати напругу кожної половини з напругою між крайніми виводами.

## Sources

<!-- generated from frontmatter -->
