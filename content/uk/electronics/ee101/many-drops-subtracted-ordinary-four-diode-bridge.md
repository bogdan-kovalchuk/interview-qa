---
id: emb-elee-0131
title: "Скільки падінь `V_F` віднімають для звичайного чотиридіодного моста?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: vishay-1n400x
    title: "Vishay: 1N4001–1N4007 datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
---

## Short answer

Два: у кожному півперіоді струм проходить через два діоди мосту послідовно (пара по діагоналі), тому від пікової напруги вторинної обмотки віднімають `2*V_F`.[^fiore-rectification] Одне `V_F` віднімають у схемі з відводом від середини обмотки, але для моста це помилка.[^fiore-rectification] Значення `V_F` беруть з datasheet для робочого струму: для 1N4001 при 1 А воно сягає 1,1 В на діод.[^vishay-1n400x]

## Detailed explanation

Міст складається з чотирьох діодів так, що в кожному півперіоді відкрита одна діагональна пара, а друга закрита зворотною напругою. У додатний півперіод струм іде від верхнього виводу вторинної обмотки через один діод до навантаження, повертається по землі й через другий діод назад до нижнього виводу; у від’ємний півперіод цю роль виконує інша діагональна пара.[^fiore-rectification] Отже, в будь-який момент у колі струму навантаження стоять послідовно два діоди в прямому зсуві, і їхні падіння додаються: `V_out,peak = V_sec,peak - 2*V_F`.[^fiore-rectification]

У схемі з відводом від середини обмотки (два діоди) у колі навантаження лише один діод, і від напруги половини обмотки віднімають одне `V_F`.[^fiore-rectification] Плутанина виникає, коли готову формулу з одним падінням переносять на міст: міст використовує всю вторинну обмотку, але платить за це другим падінням на діоді.

**Приклад.** Вторинна обмотка 12 В RMS дає пік `12*sqrt(2) ≈ 16.97 V`. На кремнієвих діодах з `V_F ≈ 0.7 V` пік на виході моста `16.97 - 1.4 = 15.57 V`; якщо помилково відняти одне падіння, вийде `16.97 - 0.7 = 16.27 V`: завищення на 0,7 В, близько 4,5 %. Для вторинної обмотки 5 В RMS (пік `5*sqrt(2) ≈ 7.07 V`) правильний результат `7.07 - 1.4 = 5.67 V`, а помилковий `7.07 - 0.7 = 6.37 V`: похибка вже ≈ 12 %.

Значення 0,7 В – лише орієнтир. `V_F` росте зі струмом: datasheet діодів 1N4001–1N4007 дає максимум 1,1 В при 1 А для одного діода (25 °C).[^vishay-1n400x] Якщо через пару діодів протікає 1 А, на них падає до `2*1.1 = 2.2 V` і розсіюється до `2.2*1 = 2.2 W`. Коли за мостом стоїть конденсатор, діоди проводять короткими імпульсами, піковий струм яких набагато більший за середній,[^fiore-rectification] тому в момент піка падіння більше, ніж при середньому струмі.

**Типові помилки:**

- Віднімати одне `V_F` для чотиридіодного моста.
- Віднімати падіння від діючого (RMS) значення замість пікового: `V_pk = V_rms*sqrt(2)`.
- Брати 0,7 В для будь-якого діода й струму замість значення з datasheet.
- Ігнорувати `2*V_F` при низькій вторинній напрузі, де вони становлять велику частку.
