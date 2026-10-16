---
id: emb-elintro-0124
title: "Як температура впливає на пряму напругу LED?"
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
  - source_id: kingbright-wp154a4
    title: "Kingbright WP154A4SEJ3VBDZGC/CA datasheet"
    url: https://www.kingbrightusa.com/images/catalog/SPEC/WP154A4SEJ3VBDZGC-CA.pdf
---

## Short answer

Із нагріванням `V_f` багатьох LED зменшується; для червоного Kingbright WP154A4SEJ3VBDZGC/CA вказано коефіцієнт −2.0 mV/°C за `I_F = 20 mA`.[^kingbright-wp154a4] У колі з джерелом напруги та резистором це може збільшити струм, тоді як constant-current driver підтримує заданий струм у межах робочого діапазону.[^kingbright-wp154a4]

## Detailed explanation

Пряма напруга `V_f` залежить від температури переходу, і для багатьох LED вона зменшується при нагріванні. Знак і величина коефіцієнта залежать від типу компонента та робочого струму, тому числове значення слід брати з datasheet, а не переносити з одного LED на всі інші.[^aac-semiconductors]

У простому колі з джерелом напруги й послідовним резистором струм приблизно задається різницею напруг живлення та `V_f`, поділеною на опір. Якщо `V_f` падає, на резисторі лишається більша напруга, і струм зростає. Це може створювати позитивний зворотний зв’язок через нагрівання, але його сила залежить від резистора, тепловідведення та режиму; thermal runaway не є неминучим у кожному колі.[^aac-semiconductors]

Для конкретного прикладу datasheet Kingbright WP154A4SEJ3VBDZGC/CA наводить коефіцієнт `−2.0 mV/°C` для червоного варіанта при `I_F = 20 mA`. Зміна температури переходу на 10 °C відповідає приблизно `−20 mV` зміни `V_f` за умов datasheet; це не можна без перевірки застосовувати до інших кольорів, струмів чи деталей.[^kingbright-wp154a4]

Регульований за струмом драйвер компенсує зміну `V_f`, поки має достатній запас вихідної напруги. Він не скасовує зниження допустимого струму при високій температурі: потрібне теплове проєктування та дотримання обмежень виробника.[^aac-semiconductors]
