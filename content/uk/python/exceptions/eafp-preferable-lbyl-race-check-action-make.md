---
id: py-excpt-0014
title: "Коли EAFP доречніший за LBYL і як race між check та action може зробити LBYL некоректним?"
track: python
section: exceptions
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
  - source_id: py314-glossary-term-lbyl
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-LBYL
  - source_id: py314-glossary-term-eafp
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-EAFP
  - source_id: py314-library-os-os-access
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.access
---

## Short answer

**EAFP доречніший, коли стан може змінитися між перевіркою і дією.** LBYL спочатку перевіряє умову, а потім діє, тож між кроками інший потік, процес або мережевий запит може змінити стан (race типу TOCTOU, time-of-check to time-of-use). EAFP виконує дію одразу й обробляє exception, якщо вона не вдалась, тому окремого вікна немає. Документація `os.access()` попереджає саме про цей випадок і рекомендує EAFP.[^py314-library-os-os-access]

## Detailed explanation

LBYL (look before you leap) явно перевіряє передумови до виклику або пошуку, а EAFP (easier to ask forgiveness than permission) припускає, що операція зазвичай успішна, і ловить exception, якщо припущення не справдилось.[^py314-glossary-term-lbyl][^py314-glossary-term-eafp] Обидва підходи можуть бути коректними. Різниця в тому, де тримається гарантія: у EAFP її дає сама операція, а у LBYL – перевірка, яка на момент дії може вже бути неправдивою.

Race виникає, коли між перевіркою і дією є проміжок, у якому стан може змінитися. Документація `os.access()` описує саме цей випадок: перевірка доступу, а потім `open()` дають зловмиснику вікно, щоб підмінити файл, тому рекомендовано EAFP.[^py314-library-os-os-access] Імітація нижче показує ту саму механіку на словнику: `remove_key` поводиться як інший потік, що видаляє ключ у проміжку між перевіркою і дією. Це детермінована імітація, а не реальний паралельний код.

```python
def lbyl(d, key, other_thread):
    if key in d:             # check
        other_thread(d)      # another thread runs here and removes the key
        return d[key]        # action: KeyError, the check is already stale
    return None

def eafp(d, key, other_thread):
    other_thread(d)          # the removal happens here too, but there is no check to go stale
    try:
        return d[key]        # action; the exception is handled where it occurs
    except KeyError:
        return None

def remove_key(d):
    d.pop('k', None)

try:
    print(lbyl({'k': 1}, 'k', remove_key))
except KeyError as exc:
    print('LBYL failed:', exc)     # LBYL failed: 'k'
print(eafp({'k': 1}, 'k', remove_key))  # None
```

EAFP доречніший, коли помилка є нормальним сценарієм (ключа немає, файлу немає, мережа відповіла помилкою) і код має її обробити; коли стан спільний і може змінитися; і коли блок `try` вузький, тож ловиться очікуваний exception саме від потрібної операції. LBYL лишається доречним, коли часткова дія небезпечна або її не можна відкотити: краще перевірити всі вхідні дані до першого запису, ніж залишити запис наполовину зробленим.

EAFP не робить послідовність атомарною. Якщо після першої успішної дії друга падає, перша вже виконана; для цього потрібні транзакція, lock або інший механізм синхронізації.

**Типові помилки:**
- ловити широкий `Exception` навколо великого блоку, тоді помилка з сусідньої операції виглядає як «ключа немає»;
- вважати, що `try` робить кілька кроків атомарними: після першого успішного кроку другий може впасти;
- залишати `if os.path.exists(p)` перед `open(p)` «для надійності», тобто відтворювати ту саму проблему з вікном, яку EAFP прибирає.
