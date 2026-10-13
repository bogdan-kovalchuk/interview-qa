---
id: py-stdlib-0018
title: "Чому pattern з nested або overlapping quantifiers може спричинити catastrophic backtracking на crafted input і як зменшити ReDoS risk?"
description: "Backtracking-рушій re може перебирати експоненційно багато шляхів, коли вкладені квантифікатори або перекривні альтернативи не дають збігу на спеціально підібраному вході."
track: python
section: standard-library
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: backtracking при повторах; possessive квантифікатори (*+, ++, ?+, {m,n}+) і atomic groups (?>...) з Python 3.11, їхня еквівалентність і те, як вони змінюють збіги."
  - source_id: owasp-regular-expression-denial-of-service-redos
    title: "OWASP: Regular Expression Denial of Service REDOS"
    url: https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Вікі-сторінка OWASP (матеріал спільноти, не офіційна документація Python): визначення ReDoS, зростання з довжиною input, подвоєння шляхів для (a+)+$ на кожен додатковий a і форма вразливих шаблонів."
---

## Short answer

**Backtracking-рушій `re` пробує інші шляхи збігу, коли частина шаблону не збігається.**[^py314-library-re] Якщо вкладені квантифікатори або перекривні альтернативи дають експоненційно багато таких шляхів, пошук без збігу стає надто повільним; це ReDoS, а `(a+)+$` на рядку з багатьох `a` і `!` наприкінці є класичним прикладом.[^owasp-regular-expression-denial-of-service-redos] Possessive квантифікатори й atomic groups (з Python 3.11) не повертаються назад, але можуть змінити набір збігів.[^py314-library-re] Тому для захисту варто прибрати повторення, які перекриваються (наприклад, замінити `(a+)+$` на `a+$`), і обмежити довжину input.

## Detailed explanation

Регулярний вираз `re` зіставляє шаблон зліва направо. Коли наступна частина не збігається, рушій повертається до попередніх квантифікаторів і пробує взяти менше символів: `a*a` на рядку `aaaa` спершу бере всі чотири `a`, а потім віддає одну.[^py314-library-re] Для звичайного шаблону альтернатив мало, тому відмова приходить швидко. Вибух відбувається, коли один і той самий фрагмент можна розбити багатьма способами: `(a+)+` ділить послідовність з n символів `a` на непорожні групи 2^(n-1) способами.

Коли рядок закінчується символом, якого шаблон не приймає (тут `!`), `$` не збігається, і рушій перебирає всі розбиття, перш ніж відмовити. За OWASP, кількість шляхів для такого шаблону подвоюється з кожним додатковим `a`.[^owasp-regular-expression-denial-of-service-redos] Код нижче показує, як atomic group змінює цей перебір.

```python
import re

# Vulnerable: returns None, after trying every split of the a's.
re.match(r"(a+)+$", "a" * 22 + "!")

# Atomic group: the inner a+ never gives characters back.
print(re.match(r"(?>a+)+$", "a" * 22 + "!"))  # None, without the blow-up
print(re.match(r"(?>a+)a", "aaa"))            # None: the group keeps all three a's
print(re.match(r"a+a", "aaa") is not None)    # True: ordinary backtracking gives one back
```

Атомарність має ціну. Atomic group і possessive квантифікатор не віддають символи назад, тож можуть відкинути збіг, який існував би з backtracking: `(?>a+)a` не збігається з `aaa`, а `a+a` збігається.[^py314-library-re] Possessive `x*+`, `x++`, `x?+` і `x{m,n}+` еквівалентні атомарним групам `(?>x*)`, `(?>x+)`, `(?>x?)` і `(?>x{m,n})`; вони з’явилися в Python 3.11.[^py314-library-re]

Що робити. Вкладення в `(a+)+$` тут зайве: `a+$` збігається з тими самими рядками й не має подвійного перебору. Типова вразлива форма за OWASP – група з повтором, а всередині неї повтор або альтернатива з перекриттям.[^owasp-regular-expression-denial-of-service-redos] Не кожен вкладений квантифікатор вразливий, але для ненадійного вводу варто обмежити довжину рядка до виклику `re`. Atomic groups і possessive квантифікатори лише зменшують перебір і не замінюють цього.

**Типові помилки:**
- вважати шаблон безпечним, бо тест з коротким рядком виконується миттєво: час росте разом з довжиною input, і це видно лише на довгому рядку;
- виправляти шаблон atomic group без перевірки набору збігів, наприклад `(?>a+)a` більше не збігається з `aaa`;
- приймати шаблон або рядок від користувача без обмеження довжини.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
