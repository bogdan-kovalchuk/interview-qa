---
id: emb-elintro-0082
title: "Чому дешевий мережевий адаптер 9 V без навантаження видає ~14 V?"
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
  - source_id: aac-transformer-regulation
    title: "All About Circuits: Voltage Regulation"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-9/voltage-regulation/
  - source_id: aac-power-supply-circuits
    title: "All About Circuits: Power Supply Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-9/power-supply-circuits/
---

## Short answer

У простому нестабілізованому адаптері без навантаження вторинна напруга трансформатора може бути вищою за номінальну через його погане регулювання, але значення залежить від конкретної моделі. Після випрямляча й фільтрувального конденсатора напруга наближається до піку вторинної синусоїди мінус падіння на діодах; номінальні 9 V зазвичай позначають напругу під заданим навантаженням.[^aac-transformer-regulation] [^aac-power-supply-circuits]

## Detailed explanation

Дешевий нестабілізований мережевий адаптер часто складається з трансформатора, випрямляча та конденсатора, без активного регулятора, який підтримував би сталу вихідну напругу. Позначення «9 V» зазвичай стосується виходу за певного навантаження, а не обіцянки рівно 9 V за будь-якого струму. Вторинна обмотка має опір, а трансформатор має скінченну внутрішню імпедансність, тому зі збільшенням струму навантаження вихідна напруга зменшується; величина зміни залежить від конструкції та навантаження.[^aac-transformer-regulation]

Якщо вихід містить діодний випрямляч і конденсатор, діоди заряджають конденсатор поблизу вершин вхідної синусоїди. За малого навантаження конденсатор втрачає мало заряду між вершинами, тому його напруга наближається до пікової напруги вторинної обмотки за вирахуванням падіння на провідних діодах. При підключенні навантаження конденсатор розряджається між імпульсами заряджання, а внутрішній опір трансформатора та діодів спричиняє додаткове просідання.[^aac-power-supply-circuits]

Приклад для розуміння: якщо вторинна обмотка справді дає `9 V RMS` синусоїди без навантаження, її пік приблизно `9*sqrt(2) = 12.7 V`; після мосту буде трохи менше через падіння на двох діодах. Це лише ілюстрація, а не вимірювання адаптера з картки: написані на корпусі 9 V можуть стосуватися навантаженого режиму, і реальна вторинна напруга може відрізнятися. Типова помилка – вважати, що виміряні мультиметром приблизно 14 V обов’язково є 14 V DC на виході: спершу з’ясовують, де й у якому режимі зроблено вимірювання, та чи вимірюють AC вторинної обмотки або випрямлену напругу.[^aac-transformer-regulation] [^aac-power-supply-circuits]
