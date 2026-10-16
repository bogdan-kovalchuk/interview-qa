---
id: emb-elee-0145
title: "Коли замість стабілітрона з резистором краще використати інтегральний стабілізатор?"
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
---

## Short answer

Коли струм навантаження змінюється в широких межах або навантаження потужне. Резистор вибирають за максимальним струмом навантаження, а без навантаження весь цей струм іде через стабілітрон і гріє його.[^nexperia-an90031] Інтегральний лінійний стабілізатор має нормовану load regulation (для LM340A – до 25 мВ в діапазоні 5 мА – 1,5 А), а також внутрішнє обмеження струму й thermal shutdown.[^ti-lm340]

## Detailed explanation

Стабілітрон із резистором – це шунтовий стабілізатор: резистор `R1` задає загальний струм від джерела, а стабілітрон забирає ту частину, яку не бере навантаження. Щоб стабілітрон лишався в крутій ділянці пробою за максимального навантаження, резистор обирають за формулою `R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max))`.[^nexperia-an90031] Якщо навантаження захоче більше, ніж дає `R1`, струму для стабілітрона не лишиться, він перестане проводити, регуляція зникне, а резистор утворить з навантаженням дільник.[^fiore-rectification]

Звідси й обмеження: `R1` фіксований, а струм навантаження змінюється, тож струм стабілітрона мусить компенсувати всю різницю. Без навантаження через нього йде весь струм `R1`, і саме тоді він розсіює найбільше: `P_Z = V_Z*(V_IN - V_Z)/R1`.[^nexperia-an90031] До того ж динамічний опір стабілітрона не нульовий, тому напруга трохи змінюється разом зі струмом: `ΔV_Z = r_dif*ΔI_Z`.[^nexperia-an90031] Тому Nexperia описує таку базову схему як придатну для порівняно невеликих потужностей.[^nexperia-an90031]

**Приклад.** `V_IN = 12 V`, `V_Z = 5.1 V`, `I_Z(min) = 5 mA`, `I_LOAD(max) = 100 mA`. Тоді `R1 = 6.9/0.105 ≈ 65.7 Ω`. Без навантаження через стабілітрон іде `6.9/65.7 ≈ 105 mA`, він розсіює `5.1*0.105 ≈ 0.54 W`, резистор – `6.9*0.105 ≈ 0.72 W`, а від джерела береться `12*0.105 = 1.26 W` без жодної користі. Лінійний стабілізатор типу LM340A у тому ж режимі споживає лише власний quiescent current, до 6 мА за таблицею, тобто порядку `12*0.006 ≈ 0.07 W` (оцінка).[^ti-lm340]

Інтегральний стабілізатор змінює режим на протилежний: він бере зі входу приблизно струм навантаження плюс власний quiescent current, а не фіксований струм, розрахований на найгірший випадок. Для LM340A load regulation – не більше 25 мВ у діапазоні 5 мА – 1,5 А, тобто не гірше 0,5 % від 5 В; є внутрішнє обмеження струму й thermal shutdown.[^ti-lm340] Але це не безкоштовно: потрібен запас напруги (dropout 2 В типово за 1 А), а розсіювання на кристалі дорівнює приблизно `(V_IN - V_OUT)*I_LOAD`, і воно обмежене тепловим опором корпуса.[^ti-lm340]

**Типові помилки:**

- Розраховувати `R1` лише під типовий струм, а не під максимальний: на піку навантаження стабілітрон вийде з пробою й стабілізація зникне.[^fiore-rectification]
- Забувати про розсіювання стабілітрона за відключеного навантаження: саме там потужність максимальна.[^nexperia-an90031]
- Вважати лінійний інтегральний стабілізатор «безвтратним»: він розсіює різницю між входом і виходом і потребує dropout.[^ti-lm340]
