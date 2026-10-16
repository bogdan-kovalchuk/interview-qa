---
id: emb-elintro-0300
title: "Чому виводи компонентів іноді згинають перед пайкою?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: kingbright-lead-forming
    title: "Kingbright: Technical Notes"
    url: https://www.kingbrightusa.com/webimages/2015/catalog/Technical%20Notes.pdf
  - source_id: adafruit-perfboard
    title: "Adafruit: Collin's Lab, Breadboards & Perfboards"
    url: https://learn.adafruit.com/collins-lab-breadboards-and-perfboards?view=all
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Виводи іноді згинають, щоб зафіксувати наскрізний компонент у платі до пайки або підігнати їх до потрібного кроку отворів. Згинати треба до пайки й так, щоб не передавати зусилля на корпус; надмірний вигин може пошкодити компонент або замкнути сусідні площадки.[^kingbright-lead-forming]

## Detailed explanation

Вивід наскрізного компонента можуть зігнути, щоб тимчасово втримати деталь у платі під час перевертання або щоб сумістити виводи з отворами потрібного кроку. На perfboard вивід іноді також формують як коротку перемичку між площадками, якщо це узгоджується зі схемою. Сам вигин не створює електричного з’єднання з іншими площадками: контакт виникає лише там, де вивід припаяний або торкається оголеного провідника.[^adafruit-perfboard]

Для фіксації достатньо невеликого відхилення кінчика на стороні пайки; сильне заламування не додає надійності й ускладнює демонтаж. Важливо формувати вивід до пайки. Наприклад, рекомендації Kingbright для LED вимагають не передавати силу згинання на корпус і лінзу, не згинати змонтований компонент і залишати відстань від корпусу до першого вигину; конкретні відстані залежать від компонента, тому слід звірятися з його документацією.[^kingbright-lead-forming]

Для роботи використовуйте плоскогубці або шаблон, який утримує вивід близько до місця вигину, а не сам корпус. Не згинайте вивід повторно туди-сюди: метал втомлюється, а напруга може пошкодити ущільнення виводу чи внутрішнє з’єднання. Після вставлення огляньте нижню сторону плати: надлишок довжини обріжте, а кожен вивід ізолюйте від сусідніх площадок і доріжок. Якщо компонент має крихкий корпус або задані правила формування виводів, його datasheet має перевагу над загальною монтажною звичкою.[^kingbright-lead-forming]
