---
id: emb-elee-0029
title: "Навіщо паралельно кожному з послідовних конденсаторів ставлять балансуючі резистори?"
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
  - source_id: ti-series-capacitor-voltage-balancing
    title: "Texas Instruments: Bulk capacitors for high bus voltage – connect in series"
    url: https://www.ti.com/content/dam/videos/external-videos/en-us/2/3816841626001/5575134803001.mp4/subassets/Very_high_Voltage_bias_BK_13-Sept_complete.pdf
---

## Short answer

Балансувальні резистори паралельно кожному конденсатору створюють керований шлях струму, який послаблює вплив різниці струмів витоку та допомагає вирівняти напруги. Їхній опір не є універсальним значенням на кшталт 100 кОм: струм балансування має перевищувати очікуваний витік, а втрати потужності й номінали резисторів треба перевірити для конкретної схеми.[^ti-series-capacitor-voltage-balancing]

## Detailed explanation

Балансувальний резистор підключають паралельно кожному конденсатору в послідовному ланцюжку, щоб забезпечити контрольований шлях струму через кожну секцію.[^ti-series-capacitor-voltage-balancing]

У реальних компонентів струми витоку відрізняються. Без додаткових шляхів вони можуть призвести до нерівномірного усталеного розподілу напруги: один конденсатор отримає більше за очікувану частку й може перевищити свій рейтинг. Резистор задає струм, що переважає варіації витоку, та утворює пасивний подільник для DC. У матеріалі TI для послідовно з’єднаних високовольтних bulk-конденсаторів прямо зазначено, що балансувальний струм має бути значно більшим за струм витоку; там також відзначені додаткові втрати потужності.[^ti-series-capacitor-voltage-balancing]

Номінал резистора не можна вибрати за одним універсальним правилом «100 кОм». Він залежить від максимальної напруги на секції, найгіршого очікуваного витоку, потрібного запасу балансування та допустимого нагрівання. Наприклад, за 200 В на резисторі 100 кОм струм буде 2 мА, а потужність – 0.4 Вт; слід обрати компонент із відповідним запасом за напругою й потужністю. Такий приклад не є рекомендацією номіналу для будь-якого ланцюжка: треба врахувати дані конденсатора й режим роботи.[^ti-series-capacitor-voltage-balancing]

Приклад оцінки втрат:

```text
I_R = V/R = 200 В/100 кОм = 2 мА
P_R = V*I = 200 В*2 мА = 0.4 Вт
```

**Типова помилка:** вважати, що однакові резистори самі гарантують однакову напругу незалежно від витоку, температури й допусків. У проєкті перевіряють найгірший дисбаланс і вибирають струм балансування та потужність резисторів із запасом; для швидких перехідних процесів може знадобитися окрема перевірка ємнісного поділу або активне балансування.[^ti-series-capacitor-voltage-balancing]
