---
id: emb-elee-0062
title: "Як відкладають R, L і C на комплексній площині імпедансу?"
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
  - source_id: aac-rxz-review
    title: "All About Circuits: Review of R, X, and Z (Resistance, Reactance and Impedance)"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/review-of-r-x-and-z/
---

## Short answer

У комплексній площині імпедансу резистор має додатну дійсну складову `R`, індуктивність – додатну уявну `jωL`, а ємність – від’ємну уявну `-j/(ωC)`. Отже, їхні ідеальні імпеданси спрямовані відповідно праворуч, угору та вниз.[^aac-rxz-review]

## Detailed explanation

Комплексний імпеданс подають як `Z = R + jX`: дійсну складову `R` відкладають по горизонтальній осі, а реактивну складову `X` – по вертикальній. Такий запис зберігає і величину опору змінному струму, і фазовий зв’язок між напругою та струмом.[^aac-rxz-review]

Для ідеального резистора `Z_R = R`, тому його точка лежить на додатній дійсній осі. Для ідеальної котушки `Z_L = jωL`, де `ω = 2π*f`; додатний знак уявної складової розміщує імпеданс на додатній уявній осі. Для ідеального конденсатора `Z_C = -j/(ω*C)`, тож його уявна складова від’ємна.[^aac-rxz-review]

У реальному послідовному колі RLC імпеданси додаються як комплексні числа: `Z = R + j(X_L - X_C)`. Точка загального імпедансу має горизонтальну координату `R`, а вертикальна координата показує різницю реактивностей. Якщо вони рівні, вертикальна складова дорівнює нулю і сумарний імпеданс лежить на дійсній осі; з обох боків від цієї умови знак реактивної складової різний.[^aac-rxz-review]

Наприклад, за `X_L > X_C` вектор сумарного імпедансу спрямований вище дійсної осі, що відповідає індуктивному характеру; за `X_C > X_L` він спрямований нижче неї. Це векторне подання пояснює, чому не можна додавати модулі реактивностей як звичайні додатні числа: їхні знаки протилежні.[^aac-rxz-review]

**Типова помилка:** вважати, що координата по вертикалі завжди додатна, бо реактивний опір вимірюють у омах. Одиниця однакова для `R` і `X`, але знак `X` кодує фазу. Також не плутайте комплексну площину імпедансу з графіком фізичного компонента: положення вектора описує модель для заданої частоти.[^aac-rxz-review]
