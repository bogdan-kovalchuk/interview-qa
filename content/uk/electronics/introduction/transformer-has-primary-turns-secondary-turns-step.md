---
id: emb-elintro-0150
title: "Трансформатор: 100 витків на первинній, 1000 на вторинній – step-up чи step-down?"
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
  - source_id: aac-transformer-ratio
    title: "All About Circuits: Step-up and Step-down Transformers"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-9/step-up-and-step-down-transformers/
---

## Short answer

Це step-up трансформатор: у вторинній обмотці вдесятеро більше витків, ніж у первинній. Для ідеальної моделі змінні 12 V на первинній дадуть приблизно 120 V на вторинній без навантаження; за передавання тієї самої потужності вторинний струм буде вдесятеро меншим за первинний.[^aac-transformer-ratio]

## Detailed explanation

Трансформатор називають step-up або step-down за тим, чи збільшує він напругу на обмотці, до якої під’єднане навантаження. У цій задачі первинна обмотка має `N₁ = 100` витків, а вторинна – `N₂ = 1000`. Оскільки `N₂/N₁ = 10`, ідеальна модель дає вторинну напругу, у десять разів більшу за первинну; отже, це step-up transformer.[^aac-transformer-ratio]

Для трансформатора потрібен змінний магнітний потік, який індукує напругу в обох обмотках. Ідеальне співвідношення RMS-напруг дорівнює відношенню витків: `V₂/V₁ = N₂/N₁`. Якщо на первинну подати змінні 12 V, ідеальна оцінка вторинної напруги становить 120 V. Це не твердження про точну напругу реального пристрою: втрати, магнітне розсіювання та навантаження спричиняють відхилення.[^aac-transformer-ratio]

Зі збільшенням напруги зменшується струм, доступний за тієї самої переданої потужності. Для ідеального трансформатора `V₁*I₁ = V₂*I₂`, тому струм вторинної обмотки у цьому прикладі становить приблизно десяту частину первинного струму, якщо знехтувати струмом намагнічування та втратами. Реальний трансформатор також споживає струм намагнічування, а первинний струм залежить від навантаження та конструкції.[^aac-transformer-ratio]

**Приклад розрахунку:**

```text
N₁ = 100, N₂ = 1000
V₁ = 12 V AC
V₂ ≈ 12 * 1000/100 = 120 V AC
```

Значення 12 V у вихідній картці є прикладом для ідеального трансформатора, а не гарантією для довільного компонента. Не можна подавати сталу 12 V DC на звичайний трансформатор: після перехідного процесу немає змінного потоку для індукції вторинної напруги, а первинна обмотка може перегрітися через надмірний струм. Робота також залежить від номінальної частоти та допустимого навантаження.[^aac-transformer-ratio]

**Типова помилка:** сказати step-down, бо «вторинна сторона має більший струм» або переплутати індекси обмоток. Назву визначає саме співвідношення напруг, а збільшення напруги супроводжується зменшенням струму в ідеальній моделі.[^aac-transformer-ratio]
