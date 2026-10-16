---
id: emb-elintro-0001
title: Що таке "lumped circuit model" і навіщо він потрібен?
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: mit-lumped
    title: "MIT 6.200 Lecture 1: Lumped circuit abstraction"
    url: https://circuits.mit.edu/_static/S23/handouts/lec01a/lecture01a.pdf
---

## Short answer

Lumped circuit model подає коло як з’єднані ідеалізовані елементи: резистори, конденсатори та індуктивності. Замість просторової задачі електромагнітного поля він використовує напруги, струми й рівняння кола, якщо затримка поширення та інші відкинуті польові ефекти несуттєві. [^mit-lumped]

## Detailed explanation

Резистор зосереджує опір в одному елементі, конденсатор – запасання енергії електричного поля, індуктивність – магнітного поля. З’єднувальні проводи спочатку вважають ідеальними. Рівняння Kirchhoff описують напруги вузлів і струми гілок без обчислення повного розподілу поля. Це наближення з явними припущеннями, а не інший фізичний закон. [^mit-lumped]

Припущення щодо поширення вимагає, щоб час проходження сигналу через коло був значно меншим за характерний час його зміни. Повільний сигнал на невеликій платі часто можна описати так; довгий кабель чи швидкий цифровий фронт можуть вимагати transmission-line model. Важливий rise time фронту, навіть якщо частота повторення clock низька. [^mit-lumped]

Наприклад, джерело та резистор можна подати однією напругою й одним струмом гілки замість окремої напруги в кожній точці проводу. Якщо відкинутий імпеданс чи затримка проводу стають суттєвими, модель уточнюють parasitic елементами або розподіленими з’єднаннями. Корисна модель – найпростіша, яка зберігає потрібні для задачі ефекти.
