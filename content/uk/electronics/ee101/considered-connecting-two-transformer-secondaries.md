---
id: emb-elee-0176
title: "Що треба враховувати, з’єднуючи дві вторинні обмотки трансформатора?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: kuphaldt-phasing
    title: "Workforce LibreTexts: Lessons in Electric Circuits, Vol. II (Kuphaldt), 10.4 Phasing"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.04:_Phasing
  - source_id: esp-transformers-part2
    title: "Elliott Sound Products: Beginners’ Guide to Transformers, Part 2 (section 8, Windings in Series and Parallel)"
    url: https://sound-au.com/xfmr2.htm
  - source_id: hammond-266m20
    title: "Hammond Manufacturing: 266M20 power transformer, dual primary and secondary (datasheet)"
    url: https://www.hammfg.com/files/parts/pdf/266M20.pdf
---

## Short answer

Спершу з’ясовують фазування за позначками (dots) на виводах і номінальні напруги обмоток.[^kuphaldt-phasing] Послідовне з’єднання в фазі складає напруги, а струм обмежує обмотка з меншим номіналом; у протифазі напруги віднімаються.[^esp-transformers-part2] Паралельно з’єднують лише обмотки з однаковою напругою, у фазі й тільки якщо це дозволяє виробник: у протифазі паралельне з’єднання майже коротко замикає обмотки.[^esp-transformers-part2]

## Detailed explanation

**Фазування.** Кожна обмотка має початок і кінець, а dot convention позначає виводи з однаковою миттєвою полярністю.[^kuphaldt-phasing] Дві обмотки, з’єднані послідовно в фазі, дають суму напруг, а в протифазі – різницю.[^esp-transformers-part2] Приклад: трансформатор із двома обмотками 25 В / 5 А (250 VA) у послідовному з’єднанні дає 50 В при 5 А, а в паралельному – 25 В при 10 А; потужність у VA та сама.[^esp-transformers-part2] Виробник вказує такі пари в datasheet: для Hammond 266M20 (60 VA) це 20 В / 3 А послідовно й 10 В / 6 А паралельно, а `20*3 = 10*6 = 60 VA`.[^hammond-266m20]

**Послідовне з’єднання.** Обмотки можна з’єднувати послідовно незалежно від напруги, а максимальний струм дорівнює номіналу обмотки з найменшим струмом.[^esp-transformers-part2] Помилка фазування тут не руйнівна: для двох однакових обмоток у протифазі вихід дорівнює нулю, і трансформатору це не шкодить.[^esp-transformers-part2] Тому таку помилку видно одразу за нульовою напругою.

**Паралельне з’єднання.** Воно допустиме лише для обмоток з однаковою напругою, з’єднаних у фазі: навіть різниця 1 В породжує циркулюючий струм, обмежений лише опором обмоток.[^esp-transformers-part2] Для двох обмоток по 0,25 Ом різниця 1 В дає `1/0.5 = 2 A` марних втрат і зайвий нагрів. Для двох обмоток по 25 В у протифазі напруга контуру дорівнює 50 В, і струм має порядок `50/0.5 = 100 A`, доки не спрацює запобіжник або не перегорить обмотка.[^esp-transformers-part2] Значення 0,25 Ом – приклад для обмотки на 5 А з тієї самої статті, а реальний струм залежить ще й від індуктивності розсіювання.

**Як діяти.** Паралельну схему використовують лише тоді, коли її дозволяє виробник: для 266M20 він прямо вказує, що вторинні обмотки можна використовувати з середньою точкою, паралельно або окремо.[^hammond-266m20] Якщо інформації немає, напруги обмоток вимірюють і не паралелять їх, коли вони відрізняються більш ніж на кілька сотень мілівольт; нове з’єднання перевіряють із запобіжником.[^esp-transformers-part2]

**Типові помилки:**

- Паралелити обмотки з різною напругою або невідомим фазуванням.
- Вважати, що паралельне з’єднання збільшує напругу, а послідовне – струм (насправді навпаки).
- У послідовному з’єднанні брати струм більший за номінал найслабшої обмотки.
- Перевіряти нове з’єднання без запобіжника.
