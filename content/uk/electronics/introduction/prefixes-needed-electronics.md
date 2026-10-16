---
id: emb-elintro-0025
title: "Навіщо потрібні SI-префікси в електроніці?"
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
  - source_id: bipm-si-prefixes
    title: "BIPM: SI prefixes"
    url: https://www.bipm.org/en/measurement-units/si-prefixes
---

## Short answer

В електроніці префікси SI стисло позначають десяткові множники одиниць.[^bipm-si-prefixes] Наприклад, `k = 10³`, `m = 10⁻³`, `µ = 10⁻⁶` і `n = 10⁻⁹`.[^bipm-si-prefixes]

## Detailed explanation

Префікс SI додають до назви або символу одиниці, щоб записати її десяткове кратне чи частку без довгого ряду нулів. Наприклад, `1 kΩ = 1000 Ω`, а `1 µF = 0.000001 F`.[^bipm-si-prefixes]

Префікс є множником, а не окремою одиницею. Його символ пишуть без пробілу перед символом одиниці: `mA`, `kΩ`, `µF`. Регістр важливий: `m` означає milli (`10⁻³`), а `M` означає mega (`10⁶`), тож підміна літери змінює значення у мільярд разів.[^bipm-si-prefixes]

Під час перерахунку між префіксами змінюється лише числовий множник, а фізична величина лишається тією самою. Так, `1 mA = 0.001 A`, а `1000 µF = 1 mF`; обидва записи в кожній рівності описують ту саму величину заряду або струму відповідної одиниці. У складених одиницях префікс стосується одиниці, до якої його приєднано, тому перед піднесенням величини до степеня чи діленням треба уважно розкрити множник.[^bipm-si-prefixes]

**Приклад перерахунку:** `4.7 kΩ = 4.7 * 10³ Ω = 4700 Ω`. У схемах та вимірюваннях префікси дають змогу швидко порівнювати номінали, але перед обчисленням значення треба привести до сумісних одиниць.

**Типова помилка:** плутати `m` і `M` або трактувати префікс як одиницю. Перевіряйте символ і його степінь десяти, особливо під час читання номіналів резисторів і конденсаторів.
