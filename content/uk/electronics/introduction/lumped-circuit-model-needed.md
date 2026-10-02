---
id: emb-elintro-0001
title: Що таке "lumped circuit model" і навіщо він потрібен?
description: Що таке "lumped circuit model" і навіщо він потрібен?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання;
    конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела
    живлення; конкретні номінали й схеми курсу можуть відрізнятися.'
- source_id: mit-lumped
  title: 'MIT 6.200 Lecture 1: Lumped circuit abstraction'
  url: https://circuits.mit.edu/_static/S23/handouts/lec01a/lecture01a.pdf
  accessed: 2026-10-04
  kind: book
  version: Spring 2023
  applicability: Lumped assumptions and propagation-time limitation, slides 3-4.
---

## Short answer

Lumped circuit model подає коло як з’єднані ідеалізовані елементи: резистори, конденсатори та індуктивності. Замість просторової задачі електромагнітного поля він використовує напруги, струми й рівняння кола, якщо затримка поширення та інші відкинуті польові ефекти несуттєві. [^mit-lumped]

## Detailed explanation

Резистор зосереджує опір в одному елементі, конденсатор – запасання енергії електричного поля, індуктивність – магнітного поля. З’єднувальні проводи спочатку вважають ідеальними. Рівняння Kirchhoff описують напруги вузлів і струми гілок без обчислення повного розподілу поля. Це наближення з явними припущеннями, а не інший фізичний закон. [^mit-lumped]

Припущення щодо поширення вимагає, щоб час проходження сигналу через коло був значно меншим за характерний час його зміни. Повільний сигнал на невеликій платі часто можна описати так; довгий кабель чи швидкий цифровий фронт можуть вимагати transmission-line model. Важливий rise time фронту, навіть якщо частота повторення clock низька. [^mit-lumped]

Наприклад, джерело та резистор можна подати однією напругою й одним струмом гілки замість окремої напруги в кожній точці проводу. Якщо відкинутий імпеданс чи затримка проводу стають суттєвими, модель уточнюють parasitic елементами або розподіленими з’єднаннями. Корисна модель – найпростіша, яка зберігає потрібні для задачі ефекти.

## Sources

<!-- generated from frontmatter -->
