---
id: py-strtxt-0001
title: "У чому різниця між str і bytes у Python 3, і коли використовувати кожен тип?"
track: python
section: objects-and-types
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
  - source_id: py314-howto-unicode
    title: "Python 3.14: Howto/unicode"
    url: https://docs.python.org/3.14/howto/unicode.html#tips-for-writing-unicode-aware-programs
---

## Short answer

**`str` є незмінною послідовністю Unicode code points для тексту, а `bytes` є незмінною послідовністю цілих чисел від 0 до 255 для encoded text або довільних binary data.**[^py314-library-stdtypes] Усередині програми текст варто тримати як `str`, а на binary чи protocol boundaries використовувати `bytes`, якщо цього вимагає API. Encoding перетворює `str` на `bytes` із заданими character encoding та error policy (за замовчуванням `utf-8` і `strict`), а decoding виконує зворотне перетворення.[^py314-library-stdtypes] Об’єкт `bytes` не зберігає інформації про те, яке encoding його створило.

## Detailed explanation

`str` і `bytes` – два різні типи, і Python не перетворює їх одне на одне мовчки. `str` зберігає текст як послідовність Unicode code points: `len('é')` дорівнює 1 незалежно від того, скільки байтів займає символ у файлі чи в мережі. `bytes` зберігає послідовність байтів, тобто цілих чисел від 0 до 255, тому `data[0]` повертає `int`, а `text[0]` повертає `str`.[^py314-library-stdtypes]

Межа між ними проходить через encoding. За замовчуванням `str.encode()` використовує `utf-8` і `strict`: символ, якого немає в обраному encoding, викликає `UnicodeError`, а не губиться мовчки.[^py314-library-stdtypes] Декодування тим самим encoding відновлює текст, а з іншим може дати інший текст або помилку, бо `bytes` не несе назви encoding.

Приклад показує обидва боки межі. Коментарі містять вивід, перевірений на CPython 3.13:

```python
text = 'é'                              # one code point
data = text.encode('utf-8')             # str -> bytes
print(len(text), len(data))             # 1 2
print(data)                             # b'\xc3\xa9'
print(data[0])                          # 195: indexing bytes gives an int
print(text[0])                          # é: indexing str gives a str
print(data.decode('utf-8') == text)     # True: the same encoding restores the text

try:
    'a' + b'a'                          # str and bytes are never concatenated implicitly
except TypeError:
    print('TypeError')                  # TypeError

raw = b'\xe9'                           # one byte; the object does not record its encoding
print(raw.decode('latin-1'))            # é
try:
    raw.decode('utf-8')
except UnicodeDecodeError:
    print('not valid UTF-8')            # not valid UTF-8
```

На практиці з цього випливає поділ обов’язків. Текст у програмі тримають як `str`, вхідні байти декодують якомога раніше, а кодують лише на виході. Документація Unicode HOWTO описує саме такий підхід і прямо каже, що автоматичного encoding чи decoding немає: `str + bytes` дає `TypeError`.[^py314-howto-unicode] `bytes` доречні там, де дані вже є байтами: бінарний файл, сокет, протокол або API, яке їх вимагає.

**Типові помилки:**
- вважати, що `len()` від `bytes` рахує символи: `len(b'\xc3\xa9')` дорівнює 2, а `len('é')` дорівнює 1;
- декодувати байти без явного encoding, хоча формат чи протокол його задає;
- змішувати `str` і `bytes` в одній операції, наприклад у конкатенації, або чекати, що Python перетворить їх сам.
