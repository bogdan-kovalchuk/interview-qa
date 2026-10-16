---
id: emb-elee-0027
title: "Який конденсатор отримує більшу напругу при послідовному з’єднанні?"
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
  - source_id: aac-capacitors-series-parallel
    title: "All About Circuits textbook: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
  - source_id: ti-series-capacitor-voltage-balancing
    title: "Texas Instruments: Bulk capacitors for high bus voltage – connect in series"
    url: https://www.ti.com/content/dam/videos/external-videos/en-us/2/3816841626001/5575134803001.mp4/subassets/Very_high_Voltage_bias_BK_13-Sept_complete.pdf
---

## Short answer

За однакового заряду в ідеальному усталеному стані більшу напругу має конденсатор із меншою ємністю, бо `V = Q/C`. Під час перехідного процесу розподіл залежить від ємностей, але через розкид витоку й допуск реальний розподіл може відрізнятися; у високовольтному ланцюжку потрібне проєктне балансування.[^aac-capacitors-series-parallel][^ti-series-capacitor-voltage-balancing]

## Detailed explanation

У початковому ідеальному розрахунку більша напруга припадає на конденсатор із меншою ємністю, якщо послідовні елементи несуть однаковий заряд.[^aac-capacitors-series-parallel]

Для кожного елемента `V = Q/C`. За фіксованого заряду зменшення `C` збільшує `V`, а сума напруг на конденсаторах дорівнює напрузі джерела. Наприклад, пара 10 мкФ і 20 мкФ у простій моделі має напруги у відношенні 2:1: менша ємність отримує дві третини загальної напруги, більша – одну третину. Це модель розподілу за ємностями під час заряджання або для ідеальних елементів, а не гарантія надійного поділу в реальному DC-ланцюжку.[^aac-capacitors-series-parallel]

Після заряджання реальні струми витоку можуть відрізнятися, а ємності мають допуски. Тому напруга на окремому конденсаторі може зрости понад просту оцінку за номінальною ємністю. TI прямо вказує на потребу балансувальних резисторів у послідовному наборі високовольтних bulk-конденсаторів і на те, що струм балансування має значно перевищувати струм витоку.[^ti-series-capacitor-voltage-balancing] У конкретній схемі застосовують також активне балансування, якщо пасивні резистори не відповідають вимогам за втратами чи точністю.[^ti-series-capacitor-voltage-balancing]

Приклад для загальної напруги 30 В:

```text
V_10uF = 30 V * 20/(10+20) = 20 V
V_20uF = 30 V * 10/(10+20) = 10 V
```

**Типова помилка:** вважати, що напруга ділиться пропорційно ємності, або покладатися на номінальні значення як на гарантію безпечного режиму. У реальному наборі перевіряють граничну напругу кожного елемента з урахуванням допуску, витоку, температури й перехідних процесів.
