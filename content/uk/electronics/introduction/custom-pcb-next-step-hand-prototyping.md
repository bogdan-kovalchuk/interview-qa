---
id: emb-elintro-0303
title: "Чому після ручного прототипування наступний крок – власна PCB?"
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
  - source_id: ti-rf-pcb-layout-review
    title: "Texas Instruments: AN098, Layout Review Techniques for Low Power RF Designs"
    url: https://www.ti.com/lit/an/swra367a/swra367a.pdf
---

## Short answer

Perfboard і wire wrap добрі для навчання та перевірки ідей, але їхнє компонування важче відтворити. PCB фіксує розташування й routing для виготовлення; у RF-схемах геометрія доріжок і stack-up безпосередньо впливають на роботу кола.[^udemy-electronics-course] [^ti-rf-pcb-layout-review]

## Detailed explanation

Власна PCB переносить перевірену на макетці або перфоплаті схему в документований і повторюваний фізичний layout. У ручному прототипі дроти та контакти зручно змінювати, тому він підходить для швидкої перевірки ідеї; натомість з’єднання легко переплутати, вони займають місце й можуть створювати непередбачувані паразитні ефекти. PCB фіксує розташування компонентів, ширину й маршрут доріжок та місця підключення, тож ту саму конструкцію можна відтворити й оглянути.[^udemy-electronics-course]

Перехід до PCB особливо корисний, коли макет уже виконує потрібну функцію, потрібно зменшити розмір, підвищити механічну надійність, перевірити електромагнітні взаємодії або виготовити кілька однакових екземплярів. Для високочастотних схем геометрія доріжок, stack-up, земляний шар і розміщення компонентів впливають на імпеданс і зв’язок між вузлами; просте перенесення з’єднань без дотримання layout-вимог може змінити поведінку схеми.[^ti-rf-pcb-layout-review]

Перед замовленням плати слід перевірити схему й footprint компонентів, технологічні обмеження виробника, ширину доріжок, зазори, шари та правила живлення. Для першої ревізії варто передбачити test/debug точки й доступ до критичних сигналів, щоб вимірювання не вимагали небезпечного торкання сусідніх виводів. PCB не гарантує, що схема працюватиме: помилкова схема, footprint або виробничі файли так само дадуть помилковий результат.

**Типові помилки:**

- Надто рано переходити до плати, не перевіривши функцію та номінали на простому прототипі.
- Вважати, що layout неважливий, бо принципова схема правильна; у RF-колах фізична геометрія є частиною електричної поведінки.[^ti-rf-pcb-layout-review]
- Не залишати тестових точок, через що первинну плату складніше налагодити.
