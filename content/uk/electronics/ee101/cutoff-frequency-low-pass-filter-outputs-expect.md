---
id: emb-elee-0103
title: "Яка частота зрізу RC-ФНЧ з 1 kΩ і 100 nF і які виходи очікувати при 1 V RMS на 160 Hz, 1.59 kHz і 15.9 kHz?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-low-pass
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Для ідеального RC-ФНЧ `f_c = 1/(2π*R*C) ≈ 1.59 kHz`. За входу 1 V RMS виходи на 160 Hz, 1.59 kHz і 15.9 kHz становлять приблизно 0.995 V, 0.707 V і 0.0995 V; на частоті зрізу фаза відстає на 45°.[^aac-low-pass]

## Detailed explanation

Простий RC-ФНЧ складається з резистора послідовно з входом і конденсатора від вихідного вузла до землі. Зі зростанням частоти імпеданс конденсатора зменшується, тому більша частина сигналу відводиться до землі, а вихід слабшає. За ідеального ненавантаженого виходу частота зрізу дорівнює `f_c = 1/(2π*R*C)`; на ній амплітуда становить `1/sqrt(2) ≈ 0.707` від низькочастотного значення.[^aac-low-pass]

Для `R = 1 kΩ` та `C = 100 nF` добуток `R*C` дорівнює `0.0001 s`, тому `f_c ≈ 1591.5 Hz`. Амплітудне відношення ідеального фільтра на частоті `f` дорівнює `1/sqrt(1+(f/f_c)^2)`. На 160 Hz частота приблизно вдесятеро нижча за зріз; на 1.59 kHz вона майже дорівнює зрізу; на 15.9 kHz – приблизно вдесятеро вища.[^aac-low-pass]

Приклад для синусоїдального входу 1 V RMS:

```text
160 Hz:   1/sqrt(1+(160/1591.5)^2) ≈ 0.995, Vout ≈ 0.995 V RMS
1591.5 Hz: 1/sqrt(2) ≈ 0.707, Vout ≈ 0.707 V RMS
15915 Hz: 1/sqrt(1+(15915/1591.5)^2) ≈ 0.0995, Vout ≈ 0.0995 V RMS
```

Це розрахунок для номінальних компонентів, ідеального джерела та виходу без навантаження; реальний опір входу наступного каскаду може змінити і підсилення, і частоту зрізу. На частоті зрізу вихід також має фазове відставання 45° в цій схемі. Типова помилка – вважати, що «частота зрізу» повністю припиняє сигнал, хоча спад є плавним, або що значення 0.707 є половиною амплітуди; це близько половини потужності за однакових опорів.[^aac-low-pass]
