---
id: emb-elintro-0029
title: "Чому кремній є напівпровідником?"
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
  - source_id: mit-semiconductor-physics
    title: "MIT OpenCourseWare: 6.012, Lecture 2 – Semiconductor Physics (I)"
    url: https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2005/resources/lec2/
---

## Short answer

У кристалічному кремнії валентні електрони утворюють ковалентні зв'язки; теплова енергія може вивільнити частину електронів і створити рухомі пари electron-hole. Їхня кількість залежить від температури, тому провідність кремнію можна змінювати, зокрема легуванням.[^mit-semiconductor-physics]

## Detailed explanation

Кремній є напівпровідником завдяки будові кристала та енергетичним станам його електронів, а не просто тому, що в атома «чотири валентні електрони». У кристалі кожен атом Si ділить валентні електрони з сусідами й формує ковалентні зв'язки; за дуже низької температури майже всі ці електрони залишаються зв'язаними.[^mit-semiconductor-physics]

За скінченної температури частина зв'язків може розірватися через теплову енергію. Тоді виникають рухомий електрон і дірка – відсутність електрона у зв'язку, яка поводиться як позитивний носій заряду. Електричне поле може спричинити рух обох типів носіїв, і це дає струм.[^mit-semiconductor-physics]

У чистому кремнії теплове утворення створює електрони й дірки попарно. Додавання домішок під час легування дає змогу керувати концентрацією носіїв: донорні домішки підвищують концентрацію електронів, а акцепторні – дірок. Саме ця керованість робить кремній придатним для діодів і транзисторів; твердження, що він є напівпровідником лише через проміжну кількість валентних електронів, пропускає вирішальну роль кристалічної структури та енергії носіїв.[^mit-semiconductor-physics]

Отже, валентні електрони пояснюють, як формується ґратка, але переносити заряд можуть електрони й дірки, що стали рухомими.
