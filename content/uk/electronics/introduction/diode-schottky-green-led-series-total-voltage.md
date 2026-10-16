---
id: emb-elintro-0190
title: "Каскад Si-діод + Шотткі + зелений `LED`: яке сумарне падіння напруги?"
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
  - source_id: aac-diode-forward-voltage
    title: "All About Circuits: Introduction to Diodes and Rectifiers"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/introduction-to-diodes-and-rectifiers/
  - source_id: aac-led-forward-voltage
    title: "All About Circuits: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
---

## Short answer

Сумарне падіння в послідовному колі дорівнює сумі миттєвих forward voltage діодів за їхнього фактичного струму, а не фіксованій сумі для всіх компонентів.[^aac-diode-forward-voltage] Значення `0.7 V`, `0.3 V` і `2.1 V` дають лише грубу оцінку `3.1 V`; при `12 V` і `330 Ω` вона передбачає струм приблизно `27 mA`, який треба звірити з datasheet LED, а не автоматично вважати допустимим.[^aac-led-forward-voltage]

## Detailed explanation

Сумарне падіння напруги в послідовному ланцюжку діодів у заданій робочій точці дорівнює сумі напруг на кожному елементі. Значення `0.7 V` для кремнієвого діода є зручним наближенням, а не сталою властивістю при будь-якому струмі. У Schottky diode падіння зазвичай нижче, а в LED воно залежить від напівпровідникового матеріалу, кольору, струму й температури.[^aac-diode-forward-voltage] [^aac-led-forward-voltage]

Спершу треба задати або оцінити струм кола, після чого взяти відповідні forward voltage з datasheet кожного конкретного компонента. Для послідовного кола струм однаковий у всіх елементах, а резистор має погасити залишок напруги джерела: `I = (V_supply - ΣV_f)/R`. Формула зручна для першої оцінки, однак якщо струм змінюється, змінюються й падіння на діодах; точніше рішення знаходять узгоджено з їхніми характеристиками або перевіряють вимірюванням.[^aac-diode-forward-voltage] [^aac-led-forward-voltage]

Приклад розрахунку: якщо для ілюстрації прийняти падіння `0.7 V`, `0.3 V` і `2.1 V`, сума буде `3.1 V`. За джерела `12 V` та резистора `330 Ω` отримаємо оцінку `I = (12 V - 3.1 V)/330 Ω ≈ 27 mA`. Це обчислення припускає саме такі forward voltage, а не підтверджує, що вибраний LED можна безпечно експлуатувати при `27 mA`: треба перевірити максимальний безперервний струм і потужність, а також допуски джерела. Зелені LED мають широкий діапазон напруги між моделями, тому одного значення кольору недостатньо.[^aac-led-forward-voltage]

**Типові помилки:**

- Додавати типові падіння та вважати суму гарантованою незалежно від струму й температури.
- Називати отримані `27 mA` «нормальними» для будь-якого LED без перевірки конкретного datasheet і теплових меж.[^aac-led-forward-voltage]
