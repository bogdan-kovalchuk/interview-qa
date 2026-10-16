---
id: emb-elintro-0130
title: "Які типи конденсаторів полярні, а які – ні?"
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
  - source_id: aac-capacitor-polarity
    title: "All About Circuits: Practical Considerations - Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/practical-considerations-capacitors/
---

## Short answer

Звичайні алюмінієві electrolytic і tantalum конденсатори полярні: їх потрібно підключати з правильною полярністю, зазначеною на корпусі.[^aac-capacitor-polarity] Ceramic і film конденсатори зазвичай неполярні, але тип компонента варто підтверджувати за маркуванням і datasheet.[^aac-capacitor-polarity] Не можна узагальнювати, що полярні конденсатори завжди дешевші чи мають більшу ємність: вибір залежить від вимог і конкретної серії.

## Detailed explanation

Полярність описує допустимий знак напруги між виводами компонента. У типового полярного конденсатора внутрішня конструкція розрахована на визначений напрямок напруги, тому його позначений плюс або мінус має відповідати схемі. Зворотне підключення може пошкодити компонент; для electrolytic і tantalum це особливо важливе обмеження.[^aac-capacitor-polarity]

Поширені алюмінієві electrolytic і tantalum конденсатори є полярними. Полярність зазвичай позначають на корпусі: у різних конструкцій маркування може вказувати мінусовий або плюсовий вивід, тож не покладайтеся лише на звичний вигляд смуги чи довжину ніжки. Перед встановленням перевірте конкретну деталь і її datasheet.[^aac-capacitor-polarity]

Ceramic та film конденсатори зазвичай неполярні, тобто їхні виводи можна поміняти місцями без порушення полярності. Це не означає, що вони взаємозамінні з будь-яким іншим типом: номінальна напруга, ємність, температурні властивості та призначення залишаються важливими. Загальна назва сімейства не замінює перевірку конкретного компонента, особливо коли позначення на схемі або корпусі неоднозначне.[^aac-capacitor-polarity]

Приклад перевірки перед монтажем: знайдіть маркування полярності на корпусі, звірте його з документацією, а тоді зіставте позитивний вузол схеми з плюсовим виводом полярного компонента. Для неполярного ceramic конденсатора такого узгодження виводів за полярністю не потрібно, хоча орієнтація може мати значення для механічного розміщення чи інших вимог конструкції.[^aac-capacitor-polarity]

**Типові помилки:**

- Вважати будь-який electrolytic придатним до підключення у довільному напрямку.
- Визначати полярність лише за формою корпусу, не прочитавши його позначення.
- Припускати, що всі ceramic та film деталі можна вибрати без перевірки номінальної напруги й datasheet.[^aac-capacitor-polarity]
