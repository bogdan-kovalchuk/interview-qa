---
id: emb-elintro-0041
title: "Що таке електричний струм і яка його одиниця?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-voltage-current-resistance
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Струм – це швидкість перенесення електричного заряду через поперечний переріз: `I = ΔQ/Δt` для середнього значення. Одиниця струму – ампер (A), причому `1 A = 1 C/s`; один кулон відповідає приблизно `6.24×10¹⁸` елементарним зарядам.[^aac-voltage-current-resistance]

## Detailed explanation

Електричний струм описує, як швидко заряд проходить крізь обрану поверхню, наприклад поперечний переріз дроту. Якщо за інтервал `Δt` через цей переріз пройшов заряд `ΔQ`, середній струм дорівнює `I = ΔQ/Δt`. Для миттєвого значення використовують границю цього відношення, тобто похідну заряду за часом; у простих задачах зі сталим струмом достатньо середнього відношення.[^aac-voltage-current-resistance]

Ампер є одиницею струму в SI. Рівність `1 A = 1 C/s` означає, що через переріз проходить один кулон заряду за секунду, а не що рухається рівно один електрон. Елементарний заряд електрона за модулем становить приблизно `1.602×10⁻¹⁹ C`, тому один кулон відповідає приблизно `6.24×10¹⁸` електронам за модулем. У металі самі електрони дрейфують у напрямку, протилежному умовному напрямку струму, але знак і напрям струму визначають домовленістю щодо позитивного заряду.[^aac-voltage-current-resistance]

Приклад: якщо за `2 s` через переріз пройшло `6 C`, середній струм становить `3 A`. Такий розрахунок потребує заряду, що перетнув саме обраний переріз за зазначений інтервал; не слід плутати його з кількістю заряду, що зберігається в компоненті, або з напругою. У змінному колі струм може змінюватися з часом і напрямом, тому одного середнього значення за довгий інтервал може бути недостатньо для опису сигналу.[^aac-voltage-current-resistance]

**Типова помилка:** ототожнювати ампер із кількістю електронів або вважати, що `1 A` означає один електрон за секунду. Ампер вимірює потік заряду за час, а число носіїв залежить від заряду кожного носія та інтервалу вимірювання.
