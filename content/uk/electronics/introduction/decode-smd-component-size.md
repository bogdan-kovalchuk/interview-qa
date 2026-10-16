---
id: emb-elintro-0011
title: Як розшифрувати розмір `SMD`-компонента "0805"?
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
  - source_id: vishay-sizes
    title: "Vishay D/CRCW e3 standard thick film chip resistors"
    url: https://www.vishay.com/docs/20035/dcrcwe3.pdf
---

## Short answer

Для поширених rectangular chip resistors imperial size code 0805 означає приблизно 0.08 на 0.05 inches; звичайні nominal dimensions – 2.0 на 1.25 mm, що відповідає metric 2012. Перевірте систему коду та actual package drawing, бо imperial і metric codes можна переплутати. [^vishay-sizes]

## Detailed explanation

Imperial code розділяють на length і width, кожну в hundredths of an inch. Точне перетворення 0.08 inch дає 2.032 mm, а 0.05 inch – 1.270 mm. Проте package naming номінальне: drawing Vishay для CRCW0805 задає nominal length 2.0 mm і width 1.25 mm з manufacturing tolerances. [^vishay-sizes]

Відповідний metric code 2012 позначає приблизний naming class 2.0 на 1.2 mm; він не вимагає width рівно 1.20 mm. Аналогічно imperial 0402 у цій resistor family зазвичай відповідає nominal 1.0 на 0.5 mm та metric 1005. [^vishay-sizes]

Body size сам по собі не є PCB land pattern. Pad dimensions, termination geometry, clearance та assembly recommendations беруть з відповідного drawing чи footprint specification. Розмір також не визначає однозначно resistance або power rating. При виборі компонента явно вказуйте unit system, щоб не сплутати imperial 0805 з metric designation.
