---
id: eng-cicd-0001
title: "Зміна торкається payment calculation: який мінімальний required CI gate з unit, integration та static checks слід обрати за failure risks?"
description: "Для payment calculation мінімальний CI gate – unit-тести на граничні значення та формати валют, інтеграційні тести з реальною БД або її емуляцією, і статичні перевірки (linter + type checker)."
track: engineering
section: ci-cd
level: middle
type: practical
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: git-git-merge
    title: "Git docs: Git Merge"
    url: https://git-scm.com/docs/git-merge
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: git-git-rebase
    title: "Git docs: Git Rebase"
    url: https://git-scm.com/docs/git-rebase
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: git-git-revert
    title: "Git docs: Git Revert"
    url: https://git-scm.com/docs/git-revert
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: git-git-reset
    title: "Git docs: Git Reset"
    url: https://git-scm.com/docs/git-reset
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: git-git-reflog
    title: "Git docs: Git Reflog"
    url: https://git-scm.com/docs/git-reflog
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Git."
  - source_id: github-continuous-integration
    title: "GitHub Docs: Continuous Integration"
    url: https://docs.github.com/en/actions/get-started/continuous-integration
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація GitHub."
  - source_id: gcloud-deployment-strategies
    title: "Google Cloud docs: Deployment Strategies"
    url: https://docs.cloud.google.com/deploy/docs/deployment-strategies
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Google Cloud."
  - source_id: google-standard
    title: "Google Engineering Practices: Standard"
    url: https://google.github.io/eng-practices/review/reviewer/standard.html
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційний матеріал Google Engineering Practices."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/development/ci_cd.md#L3-L60
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Для payment calculation мінімальний CI gate – unit-тести на граничні значення та формати валют, інтеграційні тести з реальною БД або її емуляцією, і статичні перевірки (linter + type checker).**[^git-git-merge] Помилка в обчисленнях має високий failure risk (фінансові збитки, некоректні транзакції), тому пропускати будь-який рівень перевірок неприпустимо. Unit-тести покривають формули та edge cases, інтеграційні – взаємодію з БД та зовнішніми сервісами, а static checks ловлять помилки типів і невикористані змінні до запуску тестів. Merge дозволено лише після повного «зеленого» pipeline.

## Detailed explanation

CI gate – це набір автоматизованих перевірок, які мають пройти успішно, перш ніж зміну дозволено
змержити в основну гілку.[^github-continuous-integration]

Мінімальний обов'язковий набір залежить від failure risk: чим дорожча помилка, тим ширше покриття
потрібне до merge. Для payment calculation ціна дефекту – гроші (неправильна сума, подвійне
списання, втрачена копійка через округлення), тому жоден із трьох рівнів перевірок не можна
пропускати.

Unit-тести перевіряють саму формулу обчислення – граничні значення (нуль, від'ємні суми, максимум),
округлення, роботу з різними валютами і locale. Integration-тести перевіряють, що обчислення
коректно взаємодіє з реальною чи емульованою БД і зовнішніми сервісами (наприклад, payment
gateway) – саме тут ловляться помилки на кшталт неправильного типу колонки для money. Static checks
(linter, type checker) ловлять клас помилок, які не залежать від логіки – неправильний тип
аргументу, невикористану змінну, – і роблять це до запуску тестів, тобто дешевше і швидше.

Приклад unit-тесту на граничне значення для payment calculation:

```python
def test_rounds_half_cent_down():
    assert calculate_total(cents=1005, tax_rate=0.0725) == 1078  # not 1079
```

**Типові помилки з CI gate для payment-коду:**
- вважати статичні перевірки формальністю і не блокувати merge через них, хоча вони ловлять помилки
  типів у грошових розрахунках;
- покривати unit-тестами лише «щасливий шлях», пропускаючи граничні значення (нуль, округлення,
  від'ємні суми);
- тестувати обчислення ізольовано від БД, не помічаючи, що реальна колонка зберігає суму як
  `float` замість `decimal`.

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
