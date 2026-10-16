---
id: emb-elee-0076
title: "Як пов’язані RMS, пікова і розмахова (peak-to-peak) амплітуди синусоїди?"
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
---

## Short answer

Для синусоїди без DC-зсуву `V_RMS = V_peak/√2 = V_pp/(2√2)`, а `V_pp = 2*V_peak`. RMS характеризує еквівалентну за нагріванням постійну напругу; ці співвідношення не можна безпосередньо переносити на довільну форму сигналу.[^aac-alternating-current]

## Detailed explanation

Для чистої синусоїди без постійної складової пікова амплітуда `V_peak` вимірюється від середнього рівня до вершини, а розмах `V_pp` – від нижньої до верхньої вершини. Тому `V_pp = 2*V_peak`. RMS – це квадратний корінь із середнього квадрата миттєвої напруги за період; для синусоїди інтегрування дає `V_RMS = V_peak/√2`, а отже `V_RMS = V_pp/(2√2)`.[^aac-alternating-current]

Приклад: синусоїда з `V_peak = 10 V` має `V_pp = 20 V` і `V_RMS ≈ 7.07 V`. Зворотно, якщо осцилограф показує `V_pp = 2 V`, RMS становить приблизно `0.707 V`, але лише за зазначених припущень. RMS не є просто «середнім значенням» сигналу: середнє за повний період симетричної синусоїди дорівнює нулю, тоді як RMS додатний і пов’язаний із потужністю на резисторі.[^aac-alternating-current]

Якщо сигнал має DC-зсув, його піки відносно нуля несиметричні: розмах усе ще дорівнює різниці верхнього й нижнього рівнів, але RMS повної напруги містить також внесок DC. Для спотвореної або імпульсної хвилі коефіцієнт між peak та RMS залежить від форми; застосовуйте істинний RMS вимірювач із достатньою смугою. Звичайний усереднювальний мультиметр може бути відкалібрований у RMS лише для синусоїди.[^aac-alternating-current]

**Типові помилки:**
- Плутати peak із peak-to-peak і втрачати множник два.
- Використовувати синусоїдальне співвідношення для будь-якого сигналу.
- Ігнорувати DC-зсув або обмежену смугу вимірювача.

Під час порівняння симулятора, генератора й осцилографа перевіряйте, чи кожен показує RMS, peak або peak-to-peak, а також чи сигнал заданий із DC-зсувом. Напис «1 V» без конвенції амплітуди недостатній для однозначного порівняння.[^aac-alternating-current]
