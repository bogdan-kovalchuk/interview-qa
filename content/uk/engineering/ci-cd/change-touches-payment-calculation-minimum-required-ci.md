---
id: eng-cicd-0001
title: "Зміна торкається payment calculation: який мінімальний required CI gate з unit, integration та static checks слід обрати за failure risks?"
description: "Обов'язковий CI gate визначають реальні failure boundaries зміни, а не універсальний список перевірок."
track: engineering
section: ci-cd
level: middle
type: practical
tags: []
status: published
updated: 2026-09-08
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: github-continuous-integration
    title: "GitHub Docs: Continuous Integration"
    url: https://docs.github.com/en/actions/get-started/continuous-integration
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Пояснює CI checks та автоматизований feedback у pull request; не приписує одного універсального набору перевірок."
  - source_id: py314-decimal
    title: "Python 3.14 documentation: decimal"
    url: https://docs.python.org/3.14/library/decimal.html
    accessed: 2026-09-08
    kind: official
    version: "3.14"
    applicability: "Визначає точну decimal-арифметику, явні режими округлення та quantize для грошового прикладу на Python."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/development/ci_cd.md#L3-L60
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Універсального мінімального checklist немає: зроби обов'язковими перед merge перевірки, що
покривають реальні failure boundaries цієї зміни.** Завжди детерміновано тестуй грошові правила,
граничні значення та названий режим округлення. Додавай integration-тести БД або провайдера лише
тоді, коли зміна перетинає ці межі, і запускай релевантні для проєкту type, lint та security checks.
CI робить вибрані перевірки видимими й обов'язковими для pull request.[^github-continuous-integration]

## Detailed explanation

CI gate – це набір автоматизованих перевірок, які мають пройти успішно, перш ніж зміну дозволено
змержити в основну гілку.[^github-continuous-integration]

Обов'язковий набір випливає з failure model, а не з ярлика «payment». Почни зі зміненого шляху:
арифметики та правила округлення, представлення в storage, serialization, database transaction або
контракту провайдера. Для зміни чистого обчислення можуть бути потрібні вичерпні unit- та
property-тести, але не live service. Зміна schema чи repository потребує тесту з репрезентативною
БД. Зміна gateway client потребує contract- або sandbox-тесту на цій межі. Static analysis входить
у gate, коли проєкт налаштував його ловити релевантний клас дефектів; він доповнює executable tests,
але не замінює їх.

Money-тести мають використовувати точні decimal-значення й називати правило округлення. Модуль
Python `decimal` точно представляє десяткові inputs і надає явні rounding modes.[^py314-decimal]
Перевіряй нуль, від'ємні значення, якщо domain їх допускає, максимальні підтримувані значення,
точність валюти й ties по обидва боки парної цифри. Тести storage і провайдера фокусуй лише на
припущеннях, яких справді торкається зміна.

Приклад unit-тесту на граничне значення для payment calculation:

```python
def test_rounds_half_cent_with_half_even():
    assert calculate_total_cents(
        subtotal_cents=90,
        tax_rate="0.05",
        rounding="ROUND_HALF_EVEN",
    ) == 94
```

Тут податок становить точно 4.5 цента, а `ROUND_HALF_EVEN` округлює його до 4, тому підсумок дорівнює
94 центам. Інтерфейс ілюстративний; production-тест має викликати фактичний domain API.

**Типові помилки з CI gate для payment-коду:**
- вважати generic linter, type checker, database або sandbox test обов'язковим, не пов'язавши його
  з failure, яку може спричинити зміна;
- покривати лише happy path і пропускати точні half-unit, limit, sign та currency-precision boundaries;
- тестувати лише формулу, коли змінена поведінка також залежить від storage або provider semantics;
- називати required кожну доступну перевірку, подовжуючи feedback без збільшення впевненості.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
