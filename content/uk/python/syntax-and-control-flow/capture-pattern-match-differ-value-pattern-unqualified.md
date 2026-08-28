---
id: py-syntax-0009
title: "Чим capture pattern у `match` відрізняється від value pattern і чому незакваліфіковане ім’я може несподівано зв’язати нову змінну?"
description: "Capture pattern (голе ім'я, напр. case x:) завжди успішний і прив'язує subject до нового імені; value pattern (кваліфіковане ім'я, напр. case Color.RED:) порівнює subject через == з відомим значенням."
track: python
section: syntax-and-control-flow
level: middle
type: comparison
tags: [match]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L164-L228
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Capture pattern (голе ім'я, напр. `case x:`) завжди успішний і прив'язує subject до нового імені; value pattern (кваліфіковане ім'я, напр. `case Color.RED:`) порівнює subject через `==` з відомим значенням.**[^py314-reference-expressions] Якщо ви очікували, що `case status:` порівняє з наявною змінною `status`, натомість створиться нова змінна `status`, що затінить попередню. Щоб порівняти з відомим значенням, використовуйте dotted name (`case MyEnum.status:`) або literal.

## Detailed explanation

У `match` голе ім'я ніколи не означає «порівняй з тим, що в цій змінній». Граматика вирішує це за
формою імені: некваліфіковане ім'я – це capture pattern, а ім'я з крапкою – value
pattern.[^py314-reference-compound-stmts]

Capture pattern завжди успішний. Він нічого не порівнює, а просто прив'язує subject до цього імені –
тому будь-який `case x:` збігається з чим завгодно й перекриває всі наступні case.

Value pattern порівнює. Він обчислює кваліфіковане ім'я (`Color.RED`, `settings.MODE`) і звіряє
subject з ним через `==`.

```python
status = 404

match code:
    case status:          # capture pattern: matches ANY code and rebinds `status`
        print('matched')  # runs always; `status` is now equal to `code`

match code:
    case HTTPStatus.NOT_FOUND:   # value pattern: compares with ==
        print('not found')
```

Причина такого рішення – читабельність у типовому випадку. Більшість патернів розбирають структуру і
дають іменам частини subject, тож форма без крапки зарезервована саме під це; порівняння зі
збереженим значенням – рідший випадок, і для нього треба написати щось відмінне.

**Як порівняти з наявним значенням:**
- перенести константу в клас або enum і використати dotted name: `case Status.ACTIVE:`;
- зібрати константи в модуль і писати `case codes.NOT_FOUND:`;
- використати літерал безпосередньо, якщо значення відоме: `case 404:`;
- у крайньому разі – capture з guard: `case value if value == status:`, але це вже звичайне
  порівняння, лише багатослівніше.

Помилку легко не помітити, бо код не падає: гілка просто спрацьовує завжди, а змінна тихо
перезаписується. Статичні аналізатори здебільшого попереджають про недосяжні наступні case – і це
найнадійніший сигнал, що замість порівняння написано
capture.[^py314-reference-expressions]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
