---
id: emb-elintro-0245
title: "Що таке body diode у MOSFET?"
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
  - source_id: toshiba-body-diode
    title: "Toshiba: What are the characteristics of MOSFET body diodes?"
    url: https://toshiba.semicon-storage.com/ap-en/semiconductor/knowledge/faq/mosfet/electrical-characteristics-of-mosfetsbody-diode-idr-idrp-vdsf-tr.html
---

## Short answer

Body diode – це внутрішній паразитний PN-перехід між source і drain, утворений структурою MOSFET. У звичайного enhancement-mode N-channel MOSFET його анод з’єднаний із source, а катод – із drain, тому він проводить у зворотному напрямку, коли транзистор вимкнений; напрямок для P-channel протилежний.[^toshiba-body-diode]

## Detailed explanation

Body diode – це паразитний PN-перехід між source і drain, який виникає через будову силового MOSFET. У звичайного discrete N-channel компонента діод має анод на source та катод на drain; у P-channel полярність протилежна. Перевіряйте схему конкретного компонента за його datasheet.[^toshiba-body-diode]

Затвор керує каналом, але не прибирає цей PN-перехід. Тому вимкнений MOSFET не блокує струм в обох напрямках: якщо напруга на source достатньо вища за напругу на drain для N-channel, body diode може відкритися й пропускати струм. У простому односторонньому ключі це означає, що навантаження або джерело з протилежною полярністю можуть створити небажаний шлях провідності.[^toshiba-body-diode]

Падіння напруги, допустимий прямий струм і reverse-recovery характеристики залежать від моделі та заданих виробником умов. Діод може бути корисним шляхом для індуктивного струму, наприклад у період dead time напівмосту, але його втрати й швидкість відновлення треба перевіряти для конкретної схеми. У синхронному випрямлячі після ввімкнення каналу струм може перейти з діода в канал MOSFET, зменшуючи втрати за відповідного керування.[^toshiba-body-diode]

Приклад: у низькобічного N-channel ключа drain зазвичай під’єднаний до навантаження, source – до землі. Body diode спрямований від source до drain, тож за нормальної позитивної напруги на навантаженні він зворотно зміщений, коли ключ вимкнений. Перестановка полярності джерела може зробити його прямозміщеним навіть без сигналу на gate.[^toshiba-body-diode]

**Типова помилка:** думати, що команда вимкнення gate ізолює drain від source в обох напрямках. Перед застосуванням перевірте напрямок вбудованого діода на схемі компонента, зворотну напругу та струм у всіх фазах роботи.[^toshiba-body-diode]
