---
id: py-testing-0015
title: "Як заміна real clock на injected clock або frozen time робить timeout і expiry tests детермінованими?"
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
  - source_id: py314-library-time
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
---

## Short answer

**Замість `time.sleep()` і реального очікування код отримує годинник ззовні, а тест сам переводить час на потрібну точку; timeout і expiry тоді перевіряються миттєво.** Для таймаутів і TTL в одному процесі беруть `time.monotonic()`: він не йде назад і не змінюється оновленням системного часу, але його початок не визначений, тож дійсна лише різниця двох викликів.[^py314-library-time] Expiry, яке переживає перезапуск або передається між процесами (cookie, JWT `exp`), потребує wall-clock часу.

## Detailed explanation

Таймаути, TTL і expiry залежать від поточного часу. Тест, який чекає справжній час через `time.sleep()`, повільний і на перевантаженому CI може випадково падати. Injected clock прибирає цю залежність: код отримує годинник як параметр, тобто callable, що повертає секунди. У продакшені туди передають реальний годинник, а в тесті – керований об’єкт, який тест зсуває вперед.

Нижче кеш токенів із TTL 30 секунд і тест самої межі, а не лише «через мить» і «через годину». Тест переходить межу у два кроки: 29 секунд, коли запис ще дійсний, і ще 1 секунда, коли він уже недійсний. `get` порівнює `now < expires_at`, тож перевірка «через 60 секунд» не відрізнить `<` від `<=`.

```python
from collections.abc import Callable


class TokenCache:
    def __init__(self, ttl_seconds: float, clock: Callable[[], float]) -> None:
        self._ttl = ttl_seconds
        self._clock = clock                 # injected: production passes time.monotonic
        self._values: dict[str, str] = {}
        self._expires_at: dict[str, float] = {}

    def put(self, key: str, value: str) -> None:
        self._values[key] = value
        self._expires_at[key] = self._clock() + self._ttl

    def get(self, key: str) -> str | None:
        if key in self._values and self._clock() < self._expires_at[key]:
            return self._values[key]
        self._values.pop(key, None)
        self._expires_at.pop(key, None)
        return None


class FakeClock:
    def __init__(self, now: float = 0.0) -> None:
        self.now = now

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


def test_entry_expires_exactly_at_ttl() -> None:
    clock = FakeClock()
    cache = TokenCache(ttl_seconds=30, clock=clock)
    cache.put("token", "abc")
    clock.advance(29)
    assert cache.get("token") == "abc"  # 29 s < 30 s: still valid
    clock.advance(1)
    assert cache.get("token") is None   # now == expiry: the entry is gone
```

Для таймаутів і TTL в одному процесі беруть монотонний годинник. `time.monotonic()` не може йти назад і не змінюється оновленням системного часу, тому production-код передає саме його. Його початок не визначений, тож має сенс лише різниця двох значень.[^py314-library-time] Саме значення не можна зберігати між процесами чи перезапусками: для expiry, яке має їх пережити, потрібен wall-clock час. `time.time()` може повернути менше значення, ніж у попередньому виклику, якщо системний годинник перевели назад.[^py314-library-time]

Без injected clock теж можна зробити frozen time: якщо код викликає `time.monotonic()` у тілі методу, `unittest.mock.patch("time.monotonic")` змінює об’єкт, на який вказує це ім’я, тож виклик побачить підставлене значення.[^py314-library-unittest-mock] Пастка – значення за замовчуванням: `clock=time.monotonic` у сигнатурі обчислюється, коли виконується `def`,[^py314-reference-compound-stmts-function-definitions] і пізніший `patch` його вже не замінить. Тому годинник краще передавати явно або читати `time.monotonic()` у тілі методу.

**Типові помилки:**
- `time.sleep(0.5)` у тесті замість керованого годинника: тест повільний і залежить від навантаження машини;
- `time.time()` для timeout і TTL: переведення системного годинника назад ламає порівняння;
- `clock=time.monotonic` у сигнатурі разом із пізнішим `patch`: підміни не буде, і код працюватиме з реальним часом;
- перевірка лише далеко від межі, наприклад через 60 секунд при TTL 30: не ловить помилку `<` замість `<=`.
