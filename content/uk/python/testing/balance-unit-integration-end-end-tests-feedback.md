---
id: py-testing-0003
title: "Як збалансувати unit, integration та end-to-end tests за feedback speed, fidelity і maintenance cost?"
description: "Тримайте більше швидких unit-тестів, менше integration-тестів і найменше end-to-end-тестів: чим вищий рівень, тим повільніший і крихкіший тест; точні пропорції залежать від системи."
track: python
section: testing
level: senior
type: practical
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація pytest."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Hypothesis (property-based testing)."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація mutmut (mutation testing)."
  - source_id: martinfowler-integration-test
    title: "Martin Fowler: Integration Test"
    url: https://martinfowler.com/bliki/IntegrationTest.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Есей Мартіна Фаулера (не офіційна документація): визначення integration test, вузькі й широкі варіанти, contract tests для перевірки заглушок."
  - source_id: martinfowler-test-pyramid
    title: "Martin Fowler: Test Pyramid"
    url: https://martinfowler.com/bliki/TestPyramid.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Есей Мартіна Фаулера (не офіційна документація): піраміда тестів як компроміс, широкі тести як повільні, дорогі й крихкі, обмеження цього припущення."
  - source_id: martinfowler-practical-test-pyramid
    title: "The Practical Test Pyramid (martinfowler.com, Ham Vocke)"
    url: https://martinfowler.com/articles/practical-test-pyramid.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Стаття Гема Воке на martinfowler.com (не офіційна документація): етапи pipeline за швидкістю й охопленням, end-to-end сценарії, високі витрати на підтримку й flaky-тести."
---

## Short answer

**Найбільше має бути швидких unit-тестів, менше integration-тестів і найменше end-to-end-тестів, бо чим вищий рівень, тим повільніший і крихкіший тест.**[^martinfowler-test-pyramid] Unit-тести дають швидший feedback і дешевшу підтримку, а end-to-end-тести, за оцінкою Фаулера, мають високу вартість підтримки і схильні до недетермінізму.[^martinfowler-test-pyramid][^martinfowler-practical-test-pyramid] <span class="warn">Інверсія піраміди, коли e2e-тестів багато, а unit мало, сповільнює CI і збільшує кількість flaky-тестів.</span>[^martinfowler-test-pyramid][^martinfowler-practical-test-pyramid]

## Detailed explanation

Три критерії тягнуть у різні боки: feedback speed (як швидко видно поломку), fidelity (наскільки тест схожий на роботу реальної системи) і maintenance cost (скільки коштує написати й підтримувати тест). Піраміда тестів – евристика, яка пояснює цей компроміс: тестів нижчого рівня має бути значно більше, ніж широких UI-тестів, бо широкі тести повільні, дорогі й крихкі.[^martinfowler-test-pyramid]

Піраміда не є фіксованою пропорцією. Її припущення – широкі тести повільні, дорогі й крихкі. Фаулер прямо зазначає, що якщо високорівневі тести швидкі, надійні й дешеві в змінах, нижчорівневі тести можуть бути не потрібні.[^martinfowler-test-pyramid] Є і протилежна позиція: частина авторів радить більше integration-тестів і менше unit-тестів, але різниця, за Фаулером, імовірно позірна через різні визначення unit test.[^martinfowler-test-pyramid]

Кожен рівень має свою роль. Unit-тести перевіряють логіку гілок і граничні значення, і їх можна запускати часто, на кожен commit. Integration-тести перевіряють стики з БД, мережею чи іншими сервісами, де заглушки можуть не відповідати реальності.[^martinfowler-integration-test] End-to-end тести Гем Воке радить зводити до кількох ключових сценаріїв користувача, наприклад пошуку товару, додавання в кошик і оплати.[^martinfowler-practical-test-pyramid]

Практичний критерій – швидкість і широта, а не тип тесту. Гем Воке пише, що етапи pipeline визначаються швидкістю й охопленням, тому швидкі вузькі integration-тести можуть стояти разом з unit-тестами.[^martinfowler-practical-test-pyramid] Коли високорівневий тест знаходить помилку, її варто спершу відтворити unit-тестом: тоді вона лишається під контролем на нижчому рівні.[^martinfowler-test-pyramid]

**Типові помилки:**
- будувати піраміду за кількістю тестів, а не за часом їх виконання і тим, наскільки швидко вони показують помилку;
- покривати логіку end-to-end тестами: це повільно, а помилка видна лише як падіння сценарію без причини;
- вважати будь-які пропорції обов’язковими, не виміряючи час pipeline і частку flaky-тестів;
- не писати integration-тести взагалі, покладаючись на заглушки, які ніхто не перевіряв.

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
