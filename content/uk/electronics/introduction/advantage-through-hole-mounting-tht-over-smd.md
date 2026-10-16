---
id: emb-elintro-0013
title: Яка перевага вивідного монтажу (`THT`) над `SMD`?
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
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: vishay-sizes
    title: "Vishay D/CRCW e3 standard thick film chip resistors"
    url: https://www.vishay.com/docs/20035/dcrcwe3.pdf
---

## Short answer

Through-hole mounting використовує виводи, вставлені в отвори PCB, і може бути зручним для hand assembly, prototyping та деяких механічно навантажених з’єднань. Переваги залежать від компонента й конструкції; він не універсально міцніший за будь-яке SMD рішення. Більший lead pitch може полегшувати ручну роботу. [^ti-hc00]

## Detailed explanation

THT leads проходять через отвори; surface-mount terminations кріпляться до pads на поверхні плати. Практична перевага багатьох through-hole parts – фізичний доступ: виводи можна окремо тримати, згинати й паяти. Це залежна від конструкції причина вибору компонента, а не доказ універсальної mechanical superiority.

Для конкретного порівняння geometry datasheet TI SN74HC00 має PDIP package з lead pitch 2.54 mm та SOIC package з pitch 1.27 mm. Більший pitch може полегшити hand wiring. Невеликі SMD chip resistors ще компактніші: imperial 0402 Vishay має nominal body 1.0 на 0.5 mm. Це конкретні приклади, а не розміри всіх THT чи всіх SMD components. [^ti-hc00] [^vishay-sizes]

Для connector, який часто підключатимуть, оцінюйте весь load path: body support, mounting hardware, solder joints і конструкцію PCB. Through-hole lead може допомагати утримувати конкретний part, а належно підтриманий SMD connector теж може бути міцним. SMD корисний, коли важливі board area й automated assembly; вибір визначають фактичні design requirements.
