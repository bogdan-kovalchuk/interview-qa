---
id: emb-elintro-0067
title: "Чим електричний двигун відрізняється від генератора?"
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
  - source_id: openstax-motors
    title: "OpenStax University Physics Volume 2: Electric Generators and Back Emf"
    url: https://openstax.org/books/university-physics-volume-2/pages/13-6-electric-generators-and-back-emf
---

## Short answer

Електричний двигун перетворює електричну енергію на механічну роботу, а генератор – механічну роботу на електричну енергію.[^openstax-motors] Конструктивно вони схожі, і багато машин можуть працювати в обох режимах: двигун, який обертають ззовні, сам генерує ЕРС.[^openstax-motors] Чи буде на виході генератора змінний, чи постійний струм, залежить від конструкції, наприклад від наявності колектора.

## Detailed explanation

Електричний двигун перетворює електричну енергію на механічну, а генератор перетворює механічну енергію на електричну. У двигуні струм у провідниках ротора взаємодіє з магнітним полем і створює момент сили; у генераторі механічне обертання змінює магнітний потік через обмотки й індукує ЕРС.[^openstax-motors]

Це взаємні напрями перетворення енергії, і багато електричних машин можуть працювати в обох режимах. Відмінність визначають тим, до якого порту підводять енергію та звідки її знімають. Реальна машина має втрати в обмотках, магнітопроводі, підшипниках і вентиляції, тому перетворення не є стовідсотково ефективним.[^openstax-motors]

Наприклад, двигун постійного струму, який зовнішній механізм розкручує, генерує напругу на своїх клемах. Якщо під’єднати навантаження, він може віддавати електричну потужність і гальмувати обертання; напрям струму залежить від полярності та схеми збудження. Асинхронна машина також може віддавати енергію в мережу, коли її вал приводять швидше за синхронну швидкість.[^openstax-motors]

**Типова помилка:** казати, що генератор завжди виробляє змінний струм або що двигун і генератор обов’язково є різними типами конструкції. На виході буде змінний чи постійний струм залежно від конструкції та випрямляча, а принципова різниця полягає в напрямі потоку енергії.[^openstax-motors]
