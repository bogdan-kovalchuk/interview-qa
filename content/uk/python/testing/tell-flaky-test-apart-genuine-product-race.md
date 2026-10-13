---
id: py-testing-0018
title: "Як відрізнити flaky test від product race та як зберегти evidence для відтворення?"
description: "Flaky test – недетермінований тест, що падає без змін коду; product race – реальна гонка в застосунку. Розрізняють їх ізольовані повторні запуски і збережений evidence."
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
  - source_id: pytest-usage-node-ids
    title: "pytest documentation: Specifying which tests to run"
    url: https://docs.pytest.org/en/stable/how-to/usage.html#specifying-which-tests-to-run
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Офіційна документація pytest: запуск окремого тесту за node id у форматі файл::функція."
  - source_id: pytest-output-junitxml
    title: "pytest documentation: Creating JUnitXML format files"
    url: https://docs.pytest.org/en/stable/how-to/output.html#creating-junitxml-format-files
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Офіційна документація pytest: створення звіту у форматі JUnit XML через --junit-xml."
  - source_id: pytest-logging
    title: "pytest documentation: How to manage logging"
    url: https://docs.pytest.org/en/stable/how-to/logging.html#how-to-manage-logging
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Офіційна документація pytest: показ захоплених логів для впалих тестів; за замовчуванням записи рівня WARNING і вище."
---

## Short answer

**Flaky test – недетермінований тест (час, порядок, спільний стан, `random`); product race – реальна гонка в застосунку.** Тест запускають ізольовано за node id, наприклад `tests/test_mod.py::test_func`.[^pytest-usage-node-ids] Повторні запуски розрізняють причини: падіння лише в складі набору зазвичай означає спільний стан або залежність від порядку; падіння й в ізоляції – недетермінізм тесту, гонку в продукті або звичайний детермінований дефект. Для відтворення зберігають команду, seed випадкових даних, звіт `--junit-xml` і логи падіння.[^pytest-output-junitxml][^pytest-logging]

## Detailed explanation

Обидва явища однаково виглядають у CI: червоний тест, який наступного разу зелений. Відрізняє їх джерело недетермінізму. Flaky test – проблема самого тесту: він залежить від реального часу, `random` без seed, мережі, порядку запуску або спільного глобального стану. Product race – проблема застосунку: два потоки або задачі без синхронізації змінюють спільні дані, і результат залежить від того, як вони переплелися. Частота падінь тут нічого не розрізняє, бо обидва можуть падати рідко.

Найчастіше плутають тест, який залежить від порядку через спільний стан. Ось модуль з глобальним реєстром і два тести, які pytest запускає в порядку файлу:

```python
_handlers: dict[str, object] = {}       # module-level state shared by all tests


def register(name: str, handler: object) -> None:
    _handlers[name] = handler


def handler_count() -> int:
    return len(_handlers)


def test_register_adds_handler() -> None:
    register("email", print)
    assert handler_count() == 1         # passes only if no earlier test registered a handler


def test_register_sms() -> None:
    register("sms", print)
    assert handler_count() == 1         # fails after test_register_adds_handler in file order
```

Окремий запуск `test_register_sms` проходить, а весь файл падає на ньому. Це не гонка: у фіксованому порядку падіння детерміноване. Але той самий дефект виглядає як flaky, коли порядок змінюється між запусками, тому ізольований запуск – перший крок діагностики.

Діагностика починається з повторів в ізоляції, наприклад у циклі shell: `for i in $(seq 50); do pytest 'tests/test_mod.py::test_func' -q || break; done`. Якщо тест падає й ізольовано, спершу перевіряють недетермінізм у самому тесті: час, `random` без seed, мережу, таймаути. Лише після цього шукають гонку в продукті. Її відтворюють не `sleep` у тесті, а створенням переплетення: багато потоків або задач одночасно і штучна затримка в місці спільного доступу. Якщо тест падає лише в наборі, шукають спільний стан: глобальні змінні, фікстури з ширшим scope, незачищені побічні ефекти.

Для відтворення пізніше зберігають команду з node id, seed будь-якого random-джерела, звіт `--junit-xml`[^pytest-output-junitxml] і логи падіння. За замовчуванням pytest показує для впалого тесту лише записи рівня WARNING і вище; INFO треба ввімкнути явно, наприклад `--log-level=INFO`.[^pytest-logging] Без цього тест можна лише перезапустити, а причину не знайти.

**Типові помилки:**
- додавати `time.sleep()` у тест, щоб він «став стабільним», замість виправлення синхронізації в продукті;
- оголошувати тест flaky, не перевіривши падіння в ізоляції і спільний стан;
- перезапускати тест до зеленого без збереження evidence: падіння зникає, а причина лишається.

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
