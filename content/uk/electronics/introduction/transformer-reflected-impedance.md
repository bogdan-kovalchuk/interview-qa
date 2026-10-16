---
id: emb-elintro-0154
title: "Що таке \"відображений імпеданс\" трансформатора?"
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
  - source_id: aac-transformer-impedance
    title: "All About Circuits: Special Transformers and Applications"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-9/special-transformers-applications/
---

## Short answer

Для ідеального трансформатора навантаження, приведене до первинної обмотки, дорівнює `Z_primary = (N_primary/N_secondary)^2*Z_load`. Отже, трансформатор змінює видимий імпеданс навантаження відповідно до квадрата відношення витків. Наприклад, щоб узгодити 8 Ω динамік із джерелом на 8 kΩ, потрібне відношення витків приблизно `sqrt(8000/8) = 31.6:1`; реальні втрати та частотна смуга обмежують точність.[^aac-transformer-impedance]

## Detailed explanation

Відображений імпеданс – це навантаження вторинної обмотки, виражене як імпеданс, який бачить джерело на первинній обмотці. В ідеальному трансформаторі відношення напруг дорівнює відношенню витків, а струми мають обернене відношення. Оскільки імпеданс – це відношення напруги до струму, ці два перетворення дають квадрат відношення витків: `Z_primary = (N_primary/N_secondary)^2*Z_load`.[^aac-transformer-impedance]

Звідси випливає, що підвищувальний трансформатор напруги відображає вторинне навантаження як більший імпеданс на первинному боці; знижувальний – як менший. Це дає змогу узгоджувати джерело з навантаженням, наприклад аудіопідсилювач із динаміком. Формула є наближенням для ідеального трансформатора: опір обмоток, leakage inductance, втрати осердя та частотна залежність змінюють фактичний вхідний імпеданс.[^aac-transformer-impedance]

Приклад розрахунку для ідеального пристрою:

```text
Z_load = 8 kΩ
N_primary/N_secondary = 1/31.6
Z_primary = (1/31.6)^2 * 8000 Ω ≈ 8 Ω
```

Отже, навантаження 8 kΩ на вторинній стороні відображається приблизно як 8 Ω на первинній. Для цього потрібне відношення витків близько 1:31.6, а не 1:1000: імпеданс змінюється як квадрат відношення витків.[^aac-transformer-impedance]

**Типові помилки:**
- множити імпеданс на відношення витків лише в першому степені;
- перевертати відношення, не вказавши, до якої обмотки приводять навантаження;
- вважати розрахунок точним для реального трансформатора в будь-якому частотному діапазоні.
