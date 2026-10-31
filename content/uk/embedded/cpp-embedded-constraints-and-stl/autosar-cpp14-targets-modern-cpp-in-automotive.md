---
id: emb-cppstl-0024
title: "Чим AUTOSAR C++14 відрізняється від MISRA C++?"
track: embedded
section: cpp-embedded-constraints-and-stl
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
  - source_id: autosar-cpp14-guidelines
    title: "AUTOSAR Guidelines for the use of the C++14 language in critical and safety-related systems"
    url: https://www.autosar.org/fileadmin/standards/adaptive/18-10/AUTOSAR_RS_CPP14Guidelines.pdf
  - source_id: misra-cpp-2008
    title: "MISRA C++:2008 Guidelines for the use of the C++03 language in critical systems"
    url: https://www.misra.org.uk/
  - source_id: misra-cpp-2023
    title: "MISRA C++:2023 Guidelines for the use of the C++17 language in critical systems"
    url: https://www.misra.org.uk/
---

## Short answer

**AUTOSAR (AUTomotive Open System ARchitecture) C++14 – автомобільний rule set для сучасного C++14; він регламентує templates, `constexpr`, `auto`, range-based for та інші фічі.**

Це не «C++ заборонений», а набір правил для безпечного застосування мови в safety-critical коді. MISRA C++ і AUTOSAR близькі за метою, але мають різні видання, scope і конкретні правила.

Правило: AUTOSAR C++14 = сучасний C++ у межах safety-дисципліни, а не дозвіл писати будь-які абстракції без контролю.[^embeddedinterviewlab]

## Detailed explanation

### Історичний контекст: еволюція від MISRA C++:2008 до AUTOSAR C++14

Тривалий час головним стандартом безпечного C++ в автомобільній галузі був MISRA C++:2008[^misra-cpp-2008]. Він базувався на стандарті ISO C++03 і орієнтувався на класичні мікроконтролерні блоки керування (AUTOSAR Classic Platform: ECU керування двигуном, гальмами, кузовними системами) з дуже суворими обмеженнями на пам’ять та обчислювальні ресурси.

Проте розвиток систем автономного водіння (ADAS), телематики, розпізнавання образів та складних шлюзів вимагав потужних багатоядерних процесорів (SoC) і високорівневих сервісів під керуванням повноцінних POSIX-сумісних ОС. Для цього було розроблено AUTOSAR Adaptive Platform, де базовою мовою програмування обрали сучасний C++.

Оскільки стандарт MISRA на той час не підтримував сучасні стандарти C++11 та C++14, консорціум AUTOSAR у 2017 році опублікував власний звід правил – AUTOSAR C++14 ("Guidelines for the use of the C++14 language in critical and safety-related systems")[^autosar-cpp14-guidelines].

### Головні відмінності між стандартами

1. **Цільовий стандарт мови та сучасні можливості**:
   - **MISRA C++:2008**: обмежений мовою C++03. У ньому повністю відсутні концепції move-семантики, лямбд, `constexpr` тощо.
   - **AUTOSAR C++14**: прямо регламентує безпечне використання фіч C++11 та C++14:
     - `constexpr`: заохочується для перенесення обчислень у compile-time;
     - Move-семантика (`std::move`, rvalue-посилання): дозволена для оптимізації передавання ресурсів без копіювання, але регламентується забороною використання об’єкта після переміщення (use-after-move);
     - Розумні покажчики (`std::unique_ptr`, `std::shared_ptr`): вимагаються замість використання «сирих» покажчиків і ручного управління пам’яттю;
     - Лямбда-вирази: дозволені, але заборонено неявне захоплення за посиланням `[&]` через ризик повислих посилань (dangling references);
     - Виведення типів (`auto`): дозволене лише тоді, коли воно явно покращує читабельність, а реальний тип є очевидним.

2. **Підхід до динамічної пам’яті (Heap)**:
   - **MISRA C++:2008**: майже повна заборона динамічної пам’яті після ініціалізації.
   - **AUTOSAR C++14**: дозволяє динамічне виділення пам’яті під час фази запуску системи (Startup Phase) із використанням `std::make_unique`, але вимагає детермінізму під час фази нормального функціонування (Execution Phase).

3. **Обробка винятків (Exception Handling)**:
   - **AUTOSAR C++14**: допускає використання винятків для обробки рідкісних критичних збоїв, встановлюючи суворі правила: специфікація `noexcept` для функцій переміщення та деструкторів, обов’язковий перехват винятків на межах потоків і заборона витоку винятків у сторонні C-інтерфейси.

### Конвергенція: поява стандарту MISRA C++:2023

Наявність двох паралельних стандартів створювала фрагментацію інструментів статичного аналізу (Coverity, Polyspace, Axivion, SonarQube). Тому організації MISRA та AUTOSAR об’єднали зусилля для створення єдиного стандарту наступного покоління.

Результатом цієї співпраці став документ MISRA C++:2023[^misra-cpp-2023]. Він інтегрував найкращі напрацювання AUTOSAR C++14, розширив охоплення на стандарт C++17 і наразі є єдиним актуальним спільним орієнтиром для безпечного системного та автомобільного програмування.
