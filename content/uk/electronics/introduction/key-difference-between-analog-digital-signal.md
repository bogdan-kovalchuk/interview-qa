---
id: emb-elintro-0002
title: Яка ключова різниця між аналоговим і цифровим сигналом?
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
  - source_id: ti-pam4
    title: "TI SNAA325A: PAM-4 signaling"
    url: https://www.ti.com/lit/an/snaa325a/snaa325a.pdf
---

## Short answer

Analog signal подає інформацію через величину, що може змінюватися неперервно; digital signal використовує дискретний набір символів. Binary logic зазвичай має LOW і HIGH, але digital signaling може мати більше двох рівнів: PAM-4 використовує чотири рівні та передає два біти на символ. [^ti-pam4]

## Detailed explanation

Відмінність стосується способу подання й інтерпретації інформації. Analog voltage може кодувати виміряну температуру в неперервному діапазоні. Digital receiver відносить прийняту форму сигналу до одного зі скінченного набору символів. Сама електрична напруга під час переходів усе одно змінюється неперервно; фізично дискретною величиною вона не стає.

У binary signaling два розпізнавані стани кодують 0 та 1. PAM-4 спростовує правило, ніби кожен digital signal має тільки два рівні напруги: чотири рівні символів кодують два біти на символ. Отже, digital – ширше поняття, ніж binary. [^ti-pam4]

Сигнал також може бути дискретним у часі, не будучи двійковим за амплітудою. Sampling визначає моменти спостереження; quantization – значення амплітуди, які можна подати. У поясненні ADC ці дві операції потрібно розрізняти. Цифрове подання дозволяє обробляти символи, але саме по собі не гарантує нечутливості до електричного шуму.
