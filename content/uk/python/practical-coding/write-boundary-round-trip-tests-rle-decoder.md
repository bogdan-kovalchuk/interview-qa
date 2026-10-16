---
id: py-prac-0025
title: "Складіть boundary та round-trip tests для RLE decoder з grammar `count:character|count:character`: count є positive decimal, а character не може бути `:` чи `|`; malformed input викликає `ValueError`."
track: python
section: practical-coding
sources:
  - source_id: py314-library-exceptions-valueerror
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html#ValueError
  - source_id: py314-library-functions-int
    title: "Python 3.14: Library/functions"
    url: https://docs.python.org/3.14/library/functions.html#int
---

## Short answer

**Boundary: мінімальний `count=1`, round-trip `decode(encode(s)) == s` для непорожнього `s` без `:` і `|`; malformed input має викликати `ValueError` (аргумент правильного типу з неприйнятним значенням).**[^py314-library-exceptions-valueerror] Валідні: `"3:a|2:b|1:c" -> "aaabbc"`; `"1:x" -> "x"`; `"12:a" -> "a" * 12`. Malformed: `""`, `":a"`, `"0:a"`, `"-1:a"`, `" 3:a"`, `"1::"`, `"1:|"`, `"3:a|"`, `"12:ab"`.

## Detailed explanation

Тести для RLE decoder діляться на три групи: boundary, round-trip і malformed input. Формат – `count:character`, run-и розділені `|`. Мінімальний валідний count – 1: `"1:x"` дає `"x"`. Багатоцифровий count теж має працювати: `"12:a"` дає `"a" * 12`, тобто парсер не може читати лише одну цифру. Count `0`, порожній character, а також `:` або `|` як character – malformed. За цією граматикою malformed input має викликати `ValueError`.[^py314-library-exceptions-valueerror]

Найтонша пастка – розбір count. `int()` приймає пробіли навколо рядка, знак і одиничні підкреслення між цифрами; цифри 0–9 можуть бути будь-якими Unicode decimal digits.[^py314-library-functions-int] Тому `int(" 3")` дає 3, `int("1_0")` дає 10, а `int("١")` (арабська цифра один, U+0661) дає 1. Якщо граматика означає ASCII-цифри, count треба перевіряти окремо, наприклад регулярним виразом `[0-9]+`, і лише потім викликати `int()`. Наївний парсер без такої перевірки пропускає `" 3:a"`, і тест його ловить:

```python
import unittest


def count_of(run):
    # Naive parser: int() also accepts surrounding whitespace, a sign and underscores.
    count_text, _, _ = run.partition(":")
    return int(count_text)


class TestCount(unittest.TestCase):
    def test_count_is_plain_digits(self):
        # count_of(" 3:a") returns 3 instead of raising, so this test fails.
        with self.assertRaises(ValueError):
            count_of(" 3:a")


if __name__ == "__main__":
    unittest.main()
```

Round-trip перевіряє, що encode і decode узгоджені: `encode("aabbc")` дає `"2:a|2:b|1:c"`, а decode повертає `"aabbc"`. Але round-trip не доводить правильність, якщо encode і decode помиляються однаково, тому фіксовані приклади на кшталт `"3:a|2:b|1:c" -> "aaabbc"` лишаються обов’язковими. Порожній рядок у round-trip не входить: за цією граматикою `decode("")` має викликати `ValueError`, тож encode порожнього `s` теж має відмовляти. Символи `:` і `|` encode відхиляє, бо вони є розділювачами граматики.

**Типові помилки:**
- перевіряти count через `int()` без окремої перевірки символів, тож `" 3"` і `"1_0"` приймаються;
- тестувати лише однозначні count, без `12` і без `0`;
- вважати, що character може бути рядком довшим за один символ, наприклад `"12:ab"`.
