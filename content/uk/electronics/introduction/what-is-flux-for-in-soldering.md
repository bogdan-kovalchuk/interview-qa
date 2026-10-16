---
id: emb-elintro-0284
title: "Для чого потрібен флюс у пайці?"
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
  - source_id: koki-flux-wetting
    title: "KOKI: Powerful Wetting Wave Soldering Flux for General Applications"
    url: https://koki-global.com/product/js-e-15x/
  - source_id: kester-cored-solder-wire
    title: "Kester: 275 Flux-Cored Wire"
    url: https://www.kester.com/products/product/275-flux-cored-wire
  - source_id: hse-solder-fume-indg248
    title: "Health and Safety Executive: Solder fume and you (INDG248)"
    url: https://www.hse.gov.uk/pubns/indg248.pdf
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
