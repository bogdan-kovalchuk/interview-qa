---
id: emb-elcirc-0046
title: "Який мінімальний чек-лист перед довірою до SPICE-результату?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-spice-series-parallel
    title: "All About Circuits: SPICE Simulation of Series and Parallel Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/spice-simulation-of-series-and-parallel-circuits/
  - source_id: aac-spice-model-quality
    title: "All About Circuits: Just How Accurate Is a SPICE Model?"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/simulation/how-accurate-is-a-spice-model/
---

## Short answer

Перевірте одиниці й префікси, вузол 0 як опорний, з’єднання вузлів і полярність джерел; звірте моделі компонентів та тип аналізу з тим, що саме вимірюєте. Потім порівняйте результат із ручним розрахунком для спрощеного випадку: розбіжність може вказувати на помилку схеми, налаштувань або моделі, а не лише на модель.[^aac-spice-series-parallel] [^aac-spice-model-quality]

## Detailed explanation

SPICE обчислює математичну модель схеми, описану netlist або створену зі схеми в графічному редакторі. Результат відповідає саме цій моделі та вибраному аналізу, а не автоматично реальному пристрою. Тому перевірка починається з відповідності опису задуму: вузли, номінали, полярність джерел і моделей мають бути правильними.[^aac-spice-series-parallel] [^aac-spice-model-quality]

У SPICE вузол `0` задає опорний потенціал для вимірювання вузлових напруг; він не обов’язково є фізичним заземленням плати чи захисним earth. Перевірте, що точки, які мають бути електрично спільними, справді з’єднані в схемі, а не лише намальовані поруч. Полярність важлива для знаку напруги та струму, а джерела можуть визначати напрямок відліку результату.[^aac-spice-series-parallel]

Виберіть аналіз, що відповідає питанню. Робоча точка або DC-аналіз описують усталений режим, AC-аналіз – малосигнальну частотну відповідь, а transient – зміну в часі. Коректний тип аналізу сам собою не гарантує, що початкові умови, часовий крок чи діапазон частот відповідають реальній задачі. Перегляньте повідомлення симулятора про помилки та попередження, а також масштаби осей і одиниці результатів.[^aac-spice-series-parallel]

Модель компонента має межі точності й застосовності. Спрощена модель транзистора, наприклад, може не відтворити поведінку в насиченні; відповідність моделі конкретній деталі й режиму потрібно перевіряти в документації або вимірюванням.[^aac-spice-model-quality]

**Приклад перевірки:**

Для джерела 9 V і послідовних резисторів 3 kΩ, 10 kΩ та 5 kΩ ручний розрахунок дає `I = 9 V / 18 kΩ = 0.5 mA`. Якщо симуляція показує істотно інше значення, перевірте послідовність вузлів, номінали, напрямок вимірювання струму і вибраний аналіз; у прикладі All About Circuits результат SPICE збігається з розрахунком за законом Ома.[^aac-spice-series-parallel]

Такий збіг підтверджує узгодженість цього простого прикладу, але не є загальним доказом точності складної схеми. Для аналогового пристрою врахуйте характеристики моделі, температуру та допуски компонентів; для важливого рішення зіставте симуляцію з datasheet, незалежним розрахунком або вимірюванням прототипу.[^aac-spice-model-quality]
