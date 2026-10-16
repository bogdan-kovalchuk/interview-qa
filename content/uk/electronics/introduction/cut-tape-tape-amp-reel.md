---
id: emb-elintro-0180
title: "Що таке cut tape і tape &amp; reel?"
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
  - source_id: digikey-cut-tape
    title: "DigiKey: A Closer Look at Taped Packaging including Cut Tape and Tape and Reels"
    url: https://forum.digikey.com/t/a-closer-look-at-taped-packaging-including-cut-tape-and-tape-and-reels/17211
---

## Short answer

Cut tape – це відрізана стрічка з кількістю компонентів за замовленням, зручна для малих партій і прототипів. Factory tape and reel постачається на котушці та призначена для подавання компонентів у pick-and-place обладнання; кількість на котушці залежить від конкретної деталі. Мінімальне замовлення cut tape також залежить від продавця й позиції.[^digikey-cut-tape]

## Detailed explanation

У стрічковій упаковці компоненти лежать у кишеньках carrier tape, закритих верхньою плівкою; геометрія стрічки утримує їх у заданій орієнтації. Подавач обладнання протягує стрічку з кроком кишеньок, а pick-and-place машина підбирає компоненти та встановлює їх на плату. Такий формат допомагає автоматизувати складання і захищає деталі під час зберігання та транспортування.[^digikey-cut-tape]

Factory tape and reel – це виробнича стрічка, змотана на котушку відповідно до формату конкретного компонента. Кількість у котушці не є сталою: її задає виробник для певної деталі, і вона може бути сотнями або тисячами. Cut tape – це коротший відрізок тієї самої стрічки, який продавець відраховує від виробничої котушки у замовленій кількості. Він зручний для ручного складання, лабораторних робіт і прототипів, але короткий відрізок не завжди можна безпосередньо подати в автоматичний фідер.[^digikey-cut-tape]

Деякі дистриб’ютори пропонують перемотування короткого замовлення на малу котушку з додатковими порожніми ділянками на початку та в кінці. У DigiKey така послуга називається Digi-Reel; це комерційний формат постачальника, а не синонім заводської повної котушки. Умови, мінімальна кількість і додаткова плата залежать від продавця, конкретного компонента та вибраного пакування.[^digikey-cut-tape]

**Приклад:** для прототипу з кількома платами інженер може замовити потрібну кількість компонентів у cut tape замість цілої заводської котушки. Для серійного монтажу стрічку перевіряють на сумісність із фідером, орієнтацію компонентів і вимоги до лідерної ділянки; однієї лише назви «cut tape» недостатньо, щоб гарантувати машинну подачу.[^digikey-cut-tape]

**Типові помилки:**
- вважати, що кожна заводська котушка містить однакову кількість деталей;
- припускати, що будь-який відрізок cut tape готовий для автоматичної лінії;
- сприймати мінімальну кількість замовлення як властивість упаковки, а не умову продавця.[^digikey-cut-tape]
