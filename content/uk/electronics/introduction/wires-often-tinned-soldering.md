---
id: emb-elintro-0297
title: "Чому дроти перед пайкою часто лудять?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: adafruit-wire-tinning
    title: "Adafruit: First Steps, UNTZtrument"
    url: https://learn.adafruit.com/untztrument-trellis-midi-instrument/first-steps
  - source_id: nasa-wire-tinning
    title: "NASA-STD-8739.4A: Workmanship Standard for Crimping, Interconnecting Cables, Harnesses, and Wiring"
    url: https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/nasa-std-8739.4a.pdf
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Лудіння багатожильного дроту з’єднує його тонкі жили, щоб вони не розпушувалися й не утворювали випадкових контактів. Наносьте лише стільки припою, щоб він затік між жилами: надлишок може зробити кінець надто товстим для клеми.[^nasa-wire-tinning]

## Detailed explanation

Лудіння – це попереднє змочування оголеного провідника припоєм. У багатожильному дроті окремі тонкі жили легко розходяться після зняття ізоляції; припій утримує їх разом, тому кінець легше вставити в отвір, клему або роз’єм. Це також зменшує ризик, що окрема жила вилізе за межі контакту й торкнеться сусіднього провідника.[^nasa-wire-tinning]

Під час лудіння нагрівайте сам провідник і подавайте припій до нагрітих жил, щоб він розтікся між ними, а не утворив кульку лише на поверхні. Зберігайте обриси жил видимими й не допускайте затікання припою далеко під ізоляцію: залуджена частина стає жорсткішою, тоді як решта дроту має залишатися гнучкою.[^nasa-wire-tinning]

Лудіння потрібне лише там, де його передбачає спосіб з’єднання: NASA-STD-8739.4A описує його для багатожильного провідника, який буде частиною паяного контакту в solder cup. Вимоги цієї специфікації стосуються її виробничого контексту, тож для іншого роз’єму чи клеми перевіряйте інструкцію виробника. Саме лудіння не гарантує коротшого часу остаточної пайки. Наприклад, перед монтажем гнучкого дроту в solder cup тонкий рівномірний шар припою має охоплювати робочу довжину, але жила має залишатися помітною, а ізоляція – не затікати припоєм; не переносьте цю вказівку автоматично на пружинну або гвинтову клему.[^nasa-wire-tinning]
