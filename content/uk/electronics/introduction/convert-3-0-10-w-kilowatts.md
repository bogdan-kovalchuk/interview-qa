---
id: emb-elintro-0026
title: "Як перетворити 3.0 × 10⁴ Вт у кіловати?"
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
  - source_id: nist-si-prefixes
    title: "NIST: SP 330, Section 3 – Decimal multiples and sub-multiples of SI units"
    url: https://www.nist.gov/pml/special-publication-330/sp-330-section-3
---

## Short answer

Оскільки префікс kilo означає 10³, 3.0 × 10⁴ Вт дорівнюють 30 кВт. Це також 0.03 МВт, бо mega означає 10⁶.[^nist-si-prefixes]

## Detailed explanation

Щоб перевести вати у кіловати, поділіть значення у ватах на 1000: префікс kilo означає множник 10³. Тут `3.0 × 10⁴ Вт` – це `30 000 Вт`, тому `30 000 / 1000 = 30 кВт`.[^nist-si-prefixes]

Коефіцієнт 3.0 має дві значущі цифри, тож запис `30 кВт` зберігає точність вихідного числа. Не слід читати kilo як 1024: SI-префікси є десятковими, а для двійкових множників використовують окремі префікси на кшталт kibi.[^nist-si-prefixes]

Той самий перерахунок можна виконати, розклавши степені десяти: `3.0 × 10⁴ Вт = 3.0 × 10 × 10³ Вт`. Оскільки `10³ Вт` становить один кіловат, коефіцієнт перед ним дорівнює 30. Такий спосіб допомагає уникнути помилки на три порядки, коли потрібно перейти від базової одиниці до одиниці з префіксом.[^nist-si-prefixes]

Одиниця Вт не змінює фізичну величину: і вати, і кіловати вимірюють потужність. Змінюється лише масштаб запису, тому значення потрібно ділити на кількість ватів в одному кіловаті, а не множити на 1000.[^nist-si-prefixes]

**Перевірка порядку величини:** `30 кВт = 30 000 Вт`, тож початкові вати та результат кіловатів описують ту саму потужність.
