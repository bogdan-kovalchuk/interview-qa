---
id: emb-elintro-0268
title: "Чим осцилограф відрізняється від мультиметра?"
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
  - source_id: tek-oscilloscope-specs
    title: "Tektronix: Evaluating Oscilloscope Bandwidth, Sample Rate, and Key Specifications"
    url: https://www.tek.com/en/documents/primer/evaluating-oscilloscopes
---

## Short answer

Мультиметр показує вибране числове вимірювання, наприклад DC або RMS напругу, тоді як осцилограф відображає напругу як функцію часу.[^tek-oscilloscope-specs] Це допомагає побачити переходи й короткі зміни, але відображена форма обмежена характеристиками пробника та осцилографа.[^tek-oscilloscope-specs]

## Detailed explanation

Мультиметр і осцилограф дають різні подання електричного сигналу. Мультиметр призначений для числового вимірювання вибраної величини: наприклад, напруги DC, струму, опору або RMS-значення змінної напруги. Показ на дисплеї є одним числом за певний інтервал вимірювання; він не показує повну послідовність змін сигналу в часі.

Осцилограф захоплює напругу через часові інтервали й показує форму хвилі на екрані. За нею можна оцінити амплітуду, період, частоту, пульсації, шум, overshoot і тривалість фронту. Проте ці деталі видно лише настільки, наскільки дозволяють смуга пропускання, частота дискретизації, довжина запису та пробник. Недостатня смуга може згладити фронти, а рідкісна дискретизація – пропустити подію або показати її хибно.[^tek-oscilloscope-specs]

Приклад: стабільний вихід джерела живлення зручно швидко перевірити мультиметром. Якщо треба з’ясувати, чи на виході є високочастотна пульсація або короткий провал під час перемикання навантаження, осцилограф показує часову форму й тривалість явища. Звичайне показання мультиметра може усереднити таку коротку подію, тому два прилади відповідають на різні запитання.[^tek-oscilloscope-specs]

**Типові помилки:**

- Вважати, що будь-яке число мультиметра є середнім: режим може показувати, наприклад, RMS, а точне визначення залежить від приладу.
- Вважати осцилограму точною лише тому, що хвиля намальована: недостатня смуга чи дискретизація спотворює її.
- Обирати інструмент без урахування питання: для одного значення зручний мультиметр, для зміни в часі – осцилограф.
