---
id: py-testing-0004
title: "Які seams потрібні, щоб тест не залежав від реальної мережі, clock та external service?"
track: python
section: testing
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
  - source_id: py314-library-unittest-mock-patch
    title: "Python 3.14: Library/unittest.mock (patch)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch
  - source_id: py314-library-unittest-mock-where-to-patch
    title: "Python 3.14: Library/unittest.mock (where to patch)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch
  - source_id: freezegun-readme
    title: "FreezeGun README (Usage)"
    url: https://github.com/spulec/freezegun#usage
  - source_id: vcrpy-docs
    title: "VCR.py documentation"
    url: https://vcrpy.readthedocs.io/en/latest/
  - source_id: respx-guide
    title: "RESPX User Guide"
    url: https://lundberg.github.io/respx/guide/
---

## Short answer

**Тест не має залежати від реальної мережі, часу чи external service: кожну таку залежність замінюють контрольованим test double через seam.** Для мережі підміняють HTTP-клієнт через `unittest.mock.patch`[^py314-library-unittest-mock-patch] або fixture; для часу – `freezegun`[^freezegun-readme] або injectable clock; для external service – fake, stub, record-replay (`vcrpy`[^vcrpy-docs]) або mock запитів HTTPX (`respx`[^respx-guide]). <span class="warn">Без seams тест залежить від оточення: мережевий таймаут, зміна часу чи недоступний сервіс можуть зробити його flaky або зламати CI.</span>

## Detailed explanation

Seam – це місце в коді, де залежність можна замінити без зміни логіки. Недетермінізм тесту зазвичай походить із трьох джерел: мережа, поточний час і зовнішній сервіс. Результат такого тесту залежить від стану поза кодом (сервер, годинник, чужий API), тож той самий тест може пройти сьогодні й впасти завтра.

Для мережі найпростіше підмінити HTTP-клієнт. `unittest.mock.patch` тимчасово замінює об’єкт, на який вказує ім’я.[^py314-library-unittest-mock-patch] Підміняти треба ім’я там, де код його шукає, а не там, де воно визначене: якщо модуль уже імпортував функцію, патч на вихідному модулі не має ефекту.[^py314-library-unittest-mock-where-to-patch]

Для часу `freezegun` заморожує `datetime.datetime.now()`, `datetime.date.today()`, `time.time()` та інші функції часу на час декоратора або context manager.[^freezegun-readme] Без бібліотеки той самий ефект дає параметр `clock`, який у тесті повертає фіксоване значення.

Для external service fake – це спрощена робоча реалізація, stub – готові відповіді, а record-replay записує реальні HTTP-взаємодії й відтворює їх. `vcrpy` саме так і працює: записує в cassette, а при повторному запуску читає відповіді без HTTP-трафіку.[^vcrpy-docs] `respx` перехоплює запити HTTPX і повертає задані відповіді.[^respx-guide]

Приклад без `patch`:

```python
import datetime as dt
from unittest.mock import Mock


def fetch_rate(client, clock):
    response = client.get("/rates")  # network seam: any object with get()
    return {"rate": response["rate"], "fetched_at": clock()}  # clock seam


def test_fetch_rate_without_network_or_real_clock():
    client = Mock()  # the Mock records the call; no socket is opened
    client.get.return_value = {"rate": 1.25}
    fixed_now = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)

    result = fetch_rate(client, clock=lambda: fixed_now)

    assert result == {"rate": 1.25, "fetched_at": fixed_now}
    client.get.assert_called_once_with("/rates")
```

Seams самі по собі не роблять тест правдивим: fake і mock доводять реакцію коду на задану відповідь, а не те, що реальний сервіс повертає саме її. Після зміни API cassette треба записати заново, інакше тест перевірятиме застарілу відповідь.[^vcrpy-docs]

**Типові помилки:**
- патчити ім’я в модулі, де його визначено, а не там, де код його використовує;
- лишати виклик `datetime.now()` або `time.time()` прямо в логіці, яку треба тестувати детерміновано;
- вважати, що fake або mock доводить поведінку реального сервісу.
