---
id: emb-elintro-0284
title: "Для чого потрібен флюс у пайці?"
description: "Для чого потрібен флюс у пайці?"
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Походження питання: лекція 25, курс Udemy; оригінальна картка збережена в imports. Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; курс не є доказом цих тверджень."
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: DC-кола, закон Ома, закони Кірхгофа, джерела й вимірювання; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Авторитетне джерело рівня секції: діоди, стабілітрони, біполярні й польові транзистори та джерела живлення; конкретні номінали й схеми курсу можуть відрізнятися."
  - source_id: koki-flux-wetting
    title: "KOKI: Powerful Wetting Wave Soldering Flux for General Applications"
    url: https://koki-global.com/product/js-e-15x/
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує конкретний flux для хвильового паяння: видалення оксидів і краще змочування; ефект залежить від складу флюсу та процесу."
  - source_id: kester-cored-solder-wire
    title: "Kester: 275 Flux-Cored Wire"
    url: https://www.kester.com/products/product/275-flux-cored-wire
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Описує флюсовий дріт Kester 275 для ручного паяння та таблицю варіантів із флюсовою жилою; не стверджує, що кожен дріт припою має таку жилу."
  - source_id: hse-solder-fume-indg248
    title: "Health and Safety Executive: Solder fume and you (INDG248)"
    url: https://www.hse.gov.uk/pubns/indg248.pdf
    accessed: 2026-10-04
    kind: official
    version: "INDG248(rev2) 09/15"
    applicability: "Пояснює ризики диму від каніфольного флюсу та заходи контролю, зокрема витяжку й уникнення потоку диму; не описує склад дроту припою або хімічну дію флюсу."
---

## Short answer

Флюс допомагає прибрати або обмежити утворення оксидів на нагрітих поверхнях і полегшує змочування їх розплавленим припоєм. Він не є засобом передавання тепла; у деяких видах дроту для ручного паяння є флюсова жила, що подає флюс у зону з’єднання.[^koki-flux-wetting] [^kester-cored-solder-wire]

## Detailed explanation

Флюс – це хімічний матеріал, який допомагає припою змочувати поверхню металу під час нагрівання. Металеві поверхні швидко вкриваються оксидами, а цей тонкий шар заважає розплавленому припою контактувати з чистим металом. Активний флюс прибирає наявні оксиди або стримує їх утворення під час нагрівання, тому припій може розтектися по з’єднанню замість того, щоб збиратися кулькою.[^koki-flux-wetting]

Флюс не замінює належного прогрівання деталей. Тепло передається від жала до контактів через безпосередній фізичний контакт; флюс підтримує хімічно придатну поверхню для змочування. Потрібний тип флюсу визначають матеріали та процес. Наприклад, флюс для електроніки має бути сумісним із платою й подальшим очищенням; сантехнічний кислотний флюс не можна автоматично переносити на друковані плати. Залишки деяких складів можуть бути корозійними, тому перевіряйте маркування та документацію виробника.[^koki-flux-wetting]

Дріт припою для ручного паяння випускають із флюсовою жилою; наприклад, у лінійці Kester 275 вказані різні розміри жили й частки флюсу. Під час нагрівання такий флюс працює біля місця плавлення припою. Це зручно, але не означає, що додатковий флюс ніколи не потрібен: за окисненої поверхні чи складного теплового режиму його додають відповідно до процесу та інструкцій матеріалу.[^kester-cored-solder-wire]

Приклад: якщо припій збирається краплею на окисненому мідному майданчику, додавання відповідного електронного флюсу може допомогти поверхні очиститися й змочитися. Якщо саме з’єднання залишається холодним, флюс не компенсує брак тепла від жала або поганий механічний контакт.[^koki-flux-wetting]

**Типові помилки:**
- Приписувати флюсу механічне очищення або передачу тепла замість його ролі в контролі оксидів і змочуванні.
- Вважати будь-який флюс придатним для електроніки та залишати невідомі активні залишки на платі.
- Дихати димом: дим каніфольного флюсу може шкодити здоров’ю, тому використовуйте витяжку й тримайте обличчя поза його потоком.[^hse-solder-fume-indg248]

## Sources

<!-- generated from frontmatter -->
