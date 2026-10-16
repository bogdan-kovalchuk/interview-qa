---
id: emb-elee-0147
title: "Як побудований діодний елемент OR і яка його особливість?"
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

Аноди діодів з’єднано із входами, катоди – з виходом, а вихід підтягнуто резистором до землі. Будь-який високий вхід піднімає вихід, але високий рівень на виході приблизно на `V_F` нижчий за вхідний.[^nexperia-diode-handbook][^utah-cs6710-diode-logic]

## Detailed explanation

У діодному OR кожен вхід підключено до анода свого діода, а всі катоди зведено у вихідний вузол, який резистор тримає біля землі. Коли на якомусь вході з’являється напруга помітно вище за `V_F`, його діод відкривається, через резистор іде струм, і на виході виникає додатна напруга; для кількох входів достатньо додати діоди.[^nexperia-diode-handbook] Це й дає функцію OR: вихід високий, якщо високий хоча б один вхід.[^utah-cs6710-diode-logic]

Особливість випливає з того, що відкритий діод не ідеальний провідник: на ньому лишається падіння `V_F` (для кремнію в простій моделі 0,7 В).[^libretexts-fiore-diode-models] Тому високий рівень виходу дорівнює приблизно `V_in,HIGH - V_F`, тобто на `V_F` нижчий за рівень входу, і вхід, що не перевищує `V_F`, взагалі не відкриє діод. Діоди також розв’язують входи: якщо один сигнал високий, струм не тече у входи з низьким рівнем.[^nexperia-diode-handbook]

**Приклад.** Вхід A = 5 В, вхід B = 0 В, резистор `10 kΩ` до землі. Для `V_F = 0.7 V` вихід ≈ `5 - 0.7 = 4.3 V`, струм `4.3/10000 = 0.43 mA` бере з джерела входу A. Діод B закритий: його анод 0 В, катод 4,3 В. Якщо обидва входи 0 В, діоди не проводять, і резистор тримає вихід біля 0 В (без навантаження). Для діода Шотткі з `V_F ≈ 0.3 V` вихід був би `4.7 V`, а струм `0.47 mA`.

Тож діодний OR втрачає частину рівня, і наступний каскад має це допускати. Nexperia описує такі схеми як дуже дешеве рішення для простих повільних логічних функцій.[^nexperia-diode-handbook]

**Типові помилки:**

- Очікувати на виході повний рівень входу: насправді він нижчий на `V_F`.
- Подавати на вхід напругу, що не перевищує `V_F`, і чекати високого виходу.
- Підключити діоди навпаки (аноди до виходу) і отримати AND замість OR.
