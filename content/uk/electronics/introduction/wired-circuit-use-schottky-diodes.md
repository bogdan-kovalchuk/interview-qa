---
id: emb-elintro-0176
title: "Що таке wired-OR схема і навіщо там Шотткі-діоди?"
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
  - source_id: ti-diode-oring
    title: "TI: PowerPath Management Solution for ASH"
    url: https://www.ti.com/lit/pdf/SLVAF21
  - source_id: aac-schottky-diodes
    title: "All About Circuits textbook: Special-purpose Diodes"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/special-purpose-diodes/
  - source_id: ti-schottky-selection
    title: "TI: Schottky Diode Selection in Asynchronous Boost Converters"
    url: https://www.ti.com/tw/lit/pdf/snva762
---

## Short answer

У схемі diode ORing кожне джерело під’єднують до спільного виходу через діод, який дає струму йти до навантаження та ізолює гілки від зворотного струму. Шотткі часто обирають через відносно мале пряме падіння напруги, але точне значення залежить від конкретного діода, струму й температури.[^ti-diode-oring][^aac-schottky-diodes]

## Detailed explanation

Diode ORing об’єднує кілька джерел живлення так, щоб навантаження могло отримувати енергію від доступної гілки, а струм не повертався з виходу в інше джерело. Для цього кожну гілку під’єднують через діод: анод спрямований до джерела, катод – до спільного вузла. Коли напруга джерела достатня, його діод проводить; якщо напруга іншої гілки нижча, її діод закривається і перешкоджає зворотному струму. Це не гарантує ідеального резервування: напруги джерел, їхні характеристики та умови перемикання визначають, яка гілка фактично несе навантаження.[^ti-diode-oring]

У прикладі з USB та адаптером таке з’єднання зменшує ризик подачі напруги з одного входу назад в інший. Два джерела не варто просто з’єднувати паралельно, якщо їхні виробники не дозволяють режим current sharing: навіть невелика різниця вихідних напруг може змусити одне джерело приймати струм від іншого. Діод створює ізоляцію, але його падіння зменшує напругу на навантаженні.[^ti-diode-oring]

Шотткі часто використовують, бо його пряме падіння зазвичай нижче, ніж у звичайного кремнієвого випрямного діода, що може зменшити втрати `P = V_f*I`. Значення на кшталт `0.3 V` не є сталою властивістю всіх Шотткі: перевіряють графік або специфікацію конкретної деталі при робочому струмі й температурі. Також важливі максимальна зворотна напруга, допустимий струм і reverse leakage, який у Шотткі може помітно зростати з температурою.[^aac-schottky-diodes][^ti-schottky-selection]

**Типові помилки:**
- вважати, що обидва джерела автоматично ділять струм порівну;
- приймати `0.3 V` за гарантоване падіння для кожного діода;
- не враховувати нагрівання від прямого струму та зворотний витік.[^ti-diode-oring][^ti-schottky-selection]
