---
id: eng-cicd-0002
title: "Коли обрати rolling, blue-green чи canary deployment за blast radius, traffic control і rollback speed?"
description: "Rolling – поступове оновлення інстансів без даунтайму, простий але повільний rollback; blue-green – два повних середовища з миттєвим rollback через перемикання трафіку; canary – найменший blast radius через прогресивне..."
track: engineering
section: ci-cd
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/development/ci_cd.md#L61-L95
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Rolling – поступове оновлення інстансів без даунтайму, простий але повільний rollback; blue-green – два повних середовища з миттєвим rollback через перемикання трафіку; canary – найменший blast radius через прогресивне нарощування частки трафіку на нову версію.**[^git-git-merge] Rolling підходить для звичайних релізів, коли потрібна простота і нульовий даунтайм. Blue-green – коли критична швидкість rollback (перемикання load balancer за секунди) і є ресурси на повне дублювання середовища. Canary – для ризикових змін (наприклад, payment logic), де потрібно спочатку перевірити нову версію на малій частці користувачів і лише потім нарощувати трафік.

## Detailed explanation

Deployment strategy визначає, як нова версія сервісу замінює стару в production і скільки трафіку
одночасно потрапляє на кожну версію під час викочування.[^gcloud-deployment-strategies]

Rolling deployment послідовно замінює старі інстанси новими – невеликими партіями, доки весь флот
не оновиться. Даунтайму немає, бо частина інстансів завжди обслуговує трафік, але rollback вимагає
такого самого поступового процесу в зворотний бік, тому він повільний, і в певний момент старий та
новий код працюють одночасно.

Blue-green тримає два повністю однакових середовища (blue – поточне, green – нове) і перемикає
весь трафік одним атомарним кроком на рівні load balancer чи DNS. Rollback – це те саме перемикання
назад, тому він відбувається за секунди, але ціна – подвійні ресурси на весь час викочування.

Canary спрямовує на нову версію спочатку невеликий відсоток трафіку (наприклад, 1–5%), спостерігає
за метриками помилок і latency, і лише потім поступово нарощує частку. Blast radius найменший з
трьох підходів, бо помилка в новій версії зачіпає малу частину користувачів до того, як її
виявлять і відкотять.

Приклад canary-конфігурації, яка спрямовує 5% трафіку на нову версію:

```yaml
# istio VirtualService: 95% to stable, 5% to canary
http:
  - route:
      - destination: {host: svc, subset: stable}
        weight: 95
      - destination: {host: svc, subset: canary}
        weight: 5
```

**Типові помилки при виборі deployment strategy:**
- обирати blue-green для сервісу, де подвоєння ресурсів неприйнятне з точки зору вартості;
- запускати canary без реальних метрик і алертів – без спостереження прогресивне нарощування
  трафіку не дає жодної переваги перед rolling;
- вважати rolling deployment безпечним для змін схеми БД, хоча старий і новий код тимчасово
  працюють одночасно проти тієї самої БД.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
