---
id: emb-elee-0178
title: "Як з’єднуються діодний міст, конденсатор і стабілізатор у навчальному джерелі живлення?"
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
  - source_id: vishay-gbu4
    title: "Vishay: GBU4A-GBU4M glass passivated single-phase bridge rectifier (datasheet)"
    url: https://www.vishay.com/docs/88614/gbu4a.pdf
  - source_id: vishay-alu-intro
    title: "Vishay BCcomponents: Aluminum Electrolytic Capacitors – Introduction, Basic Concepts, and Definitions"
    url: https://www.vishay.com/docs/28356/alucapsintrobcc.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
---

## Short answer

Два виводи моста «~» підключають до вторинної обмотки, а «+» і «−» дають випрямлену напругу; розташування виводів визначають за маркуванням на корпусі.[^vishay-gbu4] Плюс електролітичного конденсатора йде на «+» моста, мінус – на «−» (спільний провід), а вхід стабілізатора приєднують до того самого «+» після конденсатора, його GND – до «−».[^vishay-alu-intro][^ti-lm340]

## Detailed explanation

**Послідовність.** Вторинна обмотка живить клеми «~» моста, а «+» і «−» віддають пульсуючу постійну напругу. У кожному півперіоді проводять два діоди, тож навантаження бачить вторинну напругу мінус два падіння на діодах.[^fiore-rectification] Між «+» і «−» паралельно ставлять фільтрувальний конденсатор: він живить навантаження між піками, а його розряд і створює пульсації (оцінка – qid:emb-elee-0130).[^fiore-rectification] Вхід стабілізатора підключають до цього самого вузла, тож стабілізатор бачить напругу конденсатора, а не «сирий» вихід моста. Земля стабілізатора, «−» моста, мінус конденсатора й повернення навантаження об’єднуються в спільний провід.

**Числовий приклад.** Вторинна обмотка 9 В RMS дає пік `9*sqrt(2) ≈ 12.7 V`; за двох діодів по ≈ 0,7 В на конденсаторі виходить `12.7 - 1.4 ≈ 11.3 V`. Для uA7805 рекомендована вхідна напруга лежить у межах 7–25 В, тому 11,3 В залишають запас `11.3 - 7 = 4.3 V` до нижньої межі: стільки можуть складати пульсації й просідання, перш ніж вхід вийде за рекомендований діапазон.[^ti-ua78] Конденсатор вибирають на пікову напругу із запасом: у прикладі Fiore пік 34 В, і береться конденсатор на 50 В.[^fiore-rectification] Для піка 12,7 В запас дає, наприклад, 25 В.

**Полярність і маркування.** Електролітичний конденсатор полярний: Vishay позначає негативний вивід смужкою, поясом або знаком «−» і визначає U_REV як максимальну напругу зворотної полярності на виводах.[^vishay-alu-intro] Тому мінус конденсатора йде на «−» моста, а плюс – на «+». У datasheet на мости GBU4 клеми «~», «+» і «−» показано на кресленні, а полярність відсилає до маркування на корпусі.[^vishay-gbu4] Тому розташування виводів перевіряють за корпусом чи datasheet, а не за пам’яттю (чому контакти моста не переставляють навмання – qid:emb-elee-0181).

**Стабілізатор.** У корпусі TO-220 стабілізатора LM7805 вивід 1 – вхід, 2 – земля, 3 – вихід.[^ti-lm340] Вхідний конденсатор біля мікросхеми потрібен лише тоді, коли стабілізатор розташований далеко від фільтрувального конденсатора джерела живлення, тому довгі провідники між ними краще уникати.[^ti-lm340] Докладніше про підключення 7805 – qid:emb-elee-0163.

**Типові помилки:**

- Підключити клеми «~» моста до конденсатора чи навантаження замість вторинної обмотки.
- Поставити електролітичний конденсатор навпаки.
- Не об’єднати «−» моста, GND стабілізатора й повернення навантаження в один спільний провід.
- Визначати виводи моста чи стабілізатора за пам’яттю, а не за datasheet.
