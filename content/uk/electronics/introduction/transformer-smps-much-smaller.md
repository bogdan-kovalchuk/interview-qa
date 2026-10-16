---
id: emb-elintro-0183
title: "Чому в SMPS трансформатор може бути набагато меншим?"
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
  - source_id: ti-magnetics-design1
    title: "Magnetics Design for Switching Power Supplies: Section 1, Introduction and Basic Magnetics"
    url: https://www.ti.com/lit/ml/slup123/slup123.pdf
  - source_id: ti-magnetics-design4
    title: "Magnetics Design for Switching Power Supplies: Section 4, Power Transformer Design"
    url: https://www.ti.com/lit/ml/slup126/slup126.pdf
---

## Short answer

SMPS працює на десятках або сотнях кілогерц, а не на 50/60 Гц. За інших однакових умов підвищення робочої частоти зменшує потрібний area product осердя, тому трансформатор може бути компактнішим; точний розмір залежить також від втрат та теплових обмежень.[^ti-magnetics-design4]

## Detailed explanation

В ізольованому SMPS трансформатор працює на частоті перемикання, зазвичай набагато вищій за мережеві 50/60 Гц, тому для тієї самої потужності можна використати менші магнітні компоненти. Реальний розмір також обмежують потужність, втрати осердя, нагрівання та вимоги ізоляції.[^ti-magnetics-design1]

Імпульсний блок живлення перетворює вхідну напругу на імпульси за допомогою силового транзистора. Якщо топологія ізольована, ці імпульси подаються на трансформатор, який передає енергію та забезпечує потрібне співвідношення напруги й гальванічну ізоляцію. На відміну від трансформатора, підключеного безпосередньо до мережевої частоти, він працює на частоті перемикання перетворювача.[^aac-semiconductors]

За законом Фарадея зміна магнітного потоку пов’язана з напругою на витку та часом її прикладання. У початковій оцінці area product залежить від вихідної потужності, допустимого розмаху магнітної індукції та робочої частоти; зі зростанням частоти потрібний добуток площ осердя й вікна обмотки зменшується. Це не означає, що лінійні габарити зменшуються обернено пропорційно частоті: матеріал, втрати, температура й обмеження конструкції впливають на вибір.[^ti-magnetics-design1] [^ti-magnetics-design4]

Наприклад, перехід від 50/60 Гц до десятків або сотень кілогерц дає змогу застосувати компактне феритове осердя замість великого низькочастотного осердя. Частота не є універсальною сталою, а її підвищення збільшує комутаційні втрати та може посилити електромагнітні завади.[^aac-semiconductors]

**Типова помилка:** пояснювати зменшення лише «меншим магнітним потоком». Важливі частота, форма й амплітуда напруги на обмотці та допустима щільність потоку; крім того, розмір можуть визначати ізоляційні відстані й охолодження. Не кожен SMPS має трансформатор – це залежить від топології та вимоги ізоляції.
