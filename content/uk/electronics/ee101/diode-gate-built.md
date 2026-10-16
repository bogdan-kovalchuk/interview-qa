---
id: emb-elee-0146
title: "Як побудований діодний елемент AND?"
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
  - source_id: nexperia-diode-handbook
    title: "Nexperia: Diode Application Handbook (Design Engineer’s Guide), 2022"
    url: https://assets.nexperia.com/documents/brochure/Nexperia_document_book_DiodeApplicationHandbook_2022.pdf
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models
---

## Short answer

Вихід підтягнуто резистором до живлення, аноди діодів з’єднано з виходом, катоди – із входами. Будь-який низький вхід відкриває свій діод і тримає вихід приблизно на `V_in,LOW + V_F`; високий рівень на виході з’являється лише тоді, коли всі входи високі.[^nexperia-diode-handbook][^utah-cs6710-diode-logic]

## Detailed explanation

Схема складається з резистора між живленням і вихідним вузлом та діодів, анодами підключених до цього вузла, а катодами – до входів. Поки хоча б один вхід низький, його діод зміщений у прямому напрямку: струм тече від живлення через резистор і діод у джерело низького сигналу, тому на виході залишається лише `V_F` над рівнем цього входу.[^nexperia-diode-handbook][^utah-cs6710-diode-logic] Якщо ж усі входи високі (на рівні живлення або вище), діоди закриті, і резистор підтягує вихід до живлення; при `V_in,HIGH < V_CC` діоди лишаються відкритими, див. нижче. Так виходить функція AND.[^nexperia-diode-handbook]

Інші діоди при цьому закриті: їхні катоди на вищій напрузі, ніж вихід, тож високий вхід не тягне струм у низький. Саме так діоди розв’язують входи між собою. За простою моделлю діода те саме працює і тоді, коли високий рівень входів нижчий за живлення: діоди лишаються відкритими, і високий вихід дорівнює приблизно `V_in,HIGH + V_F`, обмежений живленням.

**Приклад.** `V_CC = 5 V`, підтягування `10 kΩ`, `V_F ≈ 0.7 V` (наближення для кремнію).[^libretexts-fiore-diode-models] Вхід A = 0 В, вхід B = 5 В: діод A відкритий, вихід ≈ `0 + 0.7 = 0.7 V`, струм `(5 - 0.7)/10000 = 0.43 mA`, і його мусить поглинати драйвер входу A. Діод B закритий, бо його катод (5 В) вищий за анод (0,7 В). Обидва входи 5 В: струму немає, вихід підтягується до 5 В (без навантаження).

Цю схему використовують як дуже дешеве рішення для простих повільних логічних функцій.[^nexperia-diode-handbook] Але низький рівень виходу не дорівнює нулю, а при каскадуванні падіння `V_F` додаються, тому з’єднувати такі вентилі у довгі ланцюжки складно (див. qid:emb-elee-0149).[^utah-cs6710-diode-logic]

**Типові помилки:**

- Вважати, що низький вихід дорівнює 0 В: він вищий за низький вхід на `V_F`.
- Переплутати полярність: у AND аноди діодів сходяться на виході (підтягування до живлення), у OR – катоди (підтягування до землі).
- Забути, що струм підтягування тече у джерело низького сигналу, і драйвер входу має його витримати.
