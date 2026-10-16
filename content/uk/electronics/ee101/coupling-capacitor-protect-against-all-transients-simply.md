---
id: emb-elee-0113
title: "Чи захищає розділовий конденсатор від усіх перехідних процесів і чи можна просто перемножити H фільтрів у каскаді?"
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
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor Transient Response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
  - source_id: aac-filter-cascading
    title: "All About Circuits: Introduction to Analog Filters"
    url: https://www.allaboutcircuits.com/TEXTBOOK/designing-analog-chips/filters/introduction-to-analog-filters/
---

## Short answer

Ні: розділовий конденсатор не є універсальним захистом від перехідних напруг, бо стрибок входу створює вихідний імпульс. Передавальні функції каскадів можна перемножити, коли вони не навантажують один одного, наприклад через буфер; інакше треба аналізувати спільну схему.[^aac-capacitor-transient] [^aac-filter-cascading]

## Detailed explanation

Розділовий конденсатор блокує усталену складову DC після заряджання, але не гарантує захисту наступного каскаду від усіх стрибків і перенапруг. Коли вхід змінюється стрибком, напруга конденсатора не може миттєво змінитися; тому короткочасна напруга передається на вихід, а потім згасає відповідно до сталої часу RC. Амплітуда та форма імпульсу залежать від опору джерела, опору навантаження, початкового заряду та величини стрибка. Захист від перенапруг потребує окремо спроєктованих обмежувачів або інших захисних елементів із перевіркою допустимих напруг і енергії.[^aac-capacitor-transient]

Для лінійних систем, з’єднаних каскадом, загальна передавальна функція є добутком окремих функцій лише якщо межа між каскадами не змінює їхню поведінку. Буфер з високим вхідним і низьким вихідним опором наближує цю умову, бо зменшує взаємне навантаження. У пасивних RC-мережах наступний ступінь зазвичай відбирає струм у попереднього, тож його вхідний імпеданс змінює ефективні опори й полюси. Тоді слід вивести передавальну функцію всієї мережі з урахуванням усіх елементів, а не множити ізольовані формули ступенів.[^aac-filter-cascading]

Приклад: сигнал проходить через послідовний конденсатор, а резистор навантаження формує ФВЧ; стрибок на вході дає короткий перехідний імпульс, хоча постійна складова зрештою не проходить. Якщо за цим ступенем без буфера підключити ще одну RC-ланку, її резистори чи конденсатори можуть змінити реакцію першої. Уявне множення двох виміряних окремо функцій не враховує цього зв’язку між ступенями.[^aac-capacitor-transient] [^aac-filter-cascading]

**Типові помилки:** плутати блокування постійної складової із захистом від імпульсної напруги та вважати будь-які каскади незалежними. У першому випадку перевірте перехідний максимум на вході наступного компонента та передбачте clamp чи інший захист, якщо це потрібно. У другому порівняйте імпеданс виходу попереднього ступеня з імпедансом входу наступного або проаналізуйте повну схему. Окремі функції можна перемножати, якщо каскади справді ізольовані або модель явно включає їхнє навантаження.[^aac-capacitor-transient] [^aac-filter-cascading]
