---
id: emb-elintro-0141
title: "Чому розрив кола з індуктором небезпечний?"
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
  - source_id: aac-inductor-voltage
    title: "All About Circuits, Inductor Voltage and Current Relationship"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
---

## Short answer

Під час розмикання індуктор створює напругу, що протидіє швидкій зміні струму: `v = L*(di/dt)`. Її пік залежить від кола й захисту, тому значення «сотні вольт» не є універсальним; flyback-діод обмежує напругу, але сповільнює спад струму.[^aac-inductor-voltage]

## Detailed explanation

Під час розмикання кола індуктор створює напругу, яка намагається підтримати струм через обмотку. Струм в індукторі не може миттєво змінитися в ідеальній моделі: за співвідношенням `v = L*(di/dt)` швидке зменшення струму вимагає великої напруги з полярністю, що протидіє цьому зменшенню. Це не означає, що індуктор «виробляє» енергію з нічого: до розмикання енергія була запасена в його магнітному полі.[^aac-inductor-voltage]

Коли контакти вимикача розходяться, повітряний проміжок має дуже великий опір, але поле може пробитися іонізацією повітря. Тоді виникає дуга, через яку струм спадає повільніше, а енергія магнітного поля переходить у тепло та світло. Без дуги або іншого шляху розсіювання напруга зростає настільки, наскільки дозволяють паразитні ємності та ізоляція; реальна межа залежить від компонента й схеми, тому вона не є фіксованою величиною.[^aac-inductor-voltage]

Наприклад, у релейному колі вимкнення струму котушки може створити викид напруги, здатний пошкодити транзисторний ключ. Захисний діод, під’єднаний паралельно котушці у зворотному напрямку під час нормального живлення, дає струму шлях циркуляції після вимкнення; це обмежує напругу, хоча й уповільнює спад струму котушки. Для швидкого вимкнення застосовують інші обмежувачі, підібрані до допустимих напруг ключа та потрібного часу спаду.[^aac-inductor-voltage]

**Типова помилка:** вважати, що розімкнений вимикач гарантує нульовий струм і нульову напругу на котушці. Після розмикання струм спочатку продовжує текти через дугу, захисний елемент або паразитний шлях; план захисту має враховувати, куди саме піде запасена енергія.[^aac-inductor-voltage]
