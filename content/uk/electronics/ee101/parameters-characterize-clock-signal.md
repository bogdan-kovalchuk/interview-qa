---
id: emb-elee-0243
title: "Які параметри характеризують тактовий сигнал?"
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
  - source_id: ti-snaa285
    title: "TI SNAA285: Time-Domain Jitter Measurement Considerations for Low-Noise Oscillators"
    url: https://www.ti.com/lit/an/snaa285/snaa285.pdf
  - source_id: ti-sdaa032
    title: "TI SDAA032: Seamless PWM Duty Cycle Updates Without Intermediate Artifacts"
    url: https://www.ti.com/lit/an/sdaa032/sdaa032.pdf
---

## Short answer

Тактовий сигнал характеризують частота `f`, період `T = 1/f` і частка високого стану `D = t_HIGH/T` (у відсотках `D = 100*t_HIGH/T`; у TI записують `D = 100*High/(High + Low)`).[^ti-sdaa032] Також важливі логічні рівні, час наростання й спадання фронтів і jitter, тобто відхилення тривалості циклу від ідеального періоду.[^ti-snaa285]

## Detailed explanation

Тактовий сигнал описують частотою і часовими параметрами. Частота `f` вимірюється в герцах, а період `T = 1/f` – це час одного повного циклу. Частка високого стану (duty cycle) показує, яку частину періоду сигнал тримає в стані 1: `D = t_HIGH/T`, а у відсотках `D = 100*t_HIGH/T`. У документі TI про PWM це записують як `D = 100*High/(High + Low)`, де сума High і Low дає період.[^ti-sdaa032]

**Приклад:** при `f = 50 МГц` маємо `T = 1/(50*10^6) = 20 нс`. Якщо `t_HIGH = 9 нс`, то `t_LOW = 11 нс` і `D = 100*9/(9 + 11) = 45 %`. Такий сигнал несиметричний, і це важить для схем, які залежать від тривалості високого стану, а не лише від частоти.

Логічні рівні визначають, які напруги наступний вхід сприймає як 1 і як 0. Час наростання й спадання фронтів визначає, скільки часу сигнал проходить між цими рівнями, і від цього залежить, наскільки швидко й чисто схема перемикається.

Jitter – це відхилення від ідеального часу. За JEDEC JESD65B period jitter – це відхилення тривалості циклу від ідеального періоду на випадковій вибірці циклів, а cycle-to-cycle jitter – зміна тривалості між сусідніми циклами.[^ti-snaa285] Period jitter здебільшого використовують для гарантії setup і hold часу логіки в CPU та FPGA. Вимірювати його треба на вибірці з 1000 до 10 000 циклів.[^ti-snaa285]

**Типові помилки:**

- вважати duty cycle 50 % за замовчуванням без перевірки datasheet;
- плутати jitter з похибкою частоти: jitter описує відхилення окремих циклів, а допуск у ppm зсуває всю частоту;
- вимірювати jitter на малій кількості циклів, тоді як для достовірного результату потрібно багато циклів.
