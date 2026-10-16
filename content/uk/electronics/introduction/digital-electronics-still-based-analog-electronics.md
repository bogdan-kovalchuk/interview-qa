---
id: emb-elintro-0017
title: Чому цифрова електроніка все одно базується на аналоговій?
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
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Digital information передають фізичні напруги й струми з analog behavior. Gates інтерпретують діапазони напруг як символи, а реальні сигнали мають скінченні transition times, delay і noise. Правильна digital operation залежить від дотримання electrical та timing limits. [^ti-hc00]

## Detailed explanation

Logic diagram приховує більшу частину electrical waveform. Transistor gate усе одно заряджає capacitance і керує load, тому output не може миттєво перейти від одного rail до іншого. TI окремо задає propagation delay та transition time: logical response і тривалість output edge – різні фізичні ефекти. [^ti-hc00]

Noise може зсунути напругу до receiver threshold. Valid HIGH або LOW range залишає запас для обмеженого збурення; undefined region не є третім корисним станом звичайної binary logic. Повільні transitions також можуть порушити recommended input transition limits, навіть якщо кінцеві рівні допустимі. Datasheet SN74HC00 явно містить ці limits. [^ti-hc00]

При debugging ненадійного digital link перевіряйте supply voltage, grounding, output loading, waveform quality і timing, а не лише задуману послідовність bits. Binary abstraction лишається корисною, але працює тому, що underlying circuit задовольняє analog conditions.
