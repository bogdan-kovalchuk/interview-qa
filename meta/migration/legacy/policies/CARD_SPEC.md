# Специфікація карток

Це єдине джерело правил для людей і ШІ, які наповнюють колоду.

## Мета й аудиторія

- Мета: підготовка до загальних Python-інтерв’ю від Junior до Senior.
- Основний предмет: Python Core, стандартна бібліотека та CPython там, де це доречно.
- Короткий огляд: алгоритми й структури даних, SQL, Git, CI/CD та SDLC.
- Overview topics have a hard ceiling of 7 accepted cards each, never a target quota. Exceeding
  the ceiling requires an explicit user decision.
- Не входять: Web/API, Django, DRF, FastAPI, SQLAlchemy, frontend і cloud-specific trivia.
- Мова: пояснення українською; код, API, ідентифікатори й усталені терміни англійською.
- Базова версія: Python 3.14. Іншу версію або preview потрібно позначати тегом.

## Формат файлу

Кожен файл починається з п’яти незмінних рядків:

```text
#separator:tab
#html:true
#deck:Python Interview Questions
#notetype:Python Interview Basic
#tags column:3
```

Після заголовка одна картка займає один фізичний рядок:

```text
Front<TAB>Back<TAB>Tags
```

- Між полями – реальний TAB (`0x09`), рівно два на рядок.
- Усередині поля немає фізичних переносів; використовувати `<br>`.
- У текстовому Python-коді екранувати `&` як `&amp;`, `<` як `&lt;`, `>` як `&gt;`.
- Inline-код: `<code>value</code>`.
- Блок коду: `<pre class="code-block"><code>...</code></pre>`.
- Головна теза: `<span class="key">...</span>`.
- Небезпечна помилка: `<span class="warn">...</span>`.
- Джерело для provenance: `<div class="source">Джерело: <a href="URL">назва</a></div>`.
  Шаблон Anki приховує цей блок від учня; він зберігається в TSV для фактчекінгу.

### Completed package source

Every TSV in `cards/` is a direct package source. `Back` must be non-empty and
the `stage::FrontOnly` tag is forbidden. Temporary Front-only experiments belong
outside this repository until they are completed, source-checked, and reviewed.
Every stable card ID requires a row in `tracking/front_sources.csv`; see
[FRONT_PROVENANCE.md](FRONT_PROVENANCE.md).

## Обов’язкові теги

Кожна картка має рівно по одному тегу з кожної групи:

```text
topic::NN_slug
type::Definition|Mechanism|Contrast|Code|Trap|Scenario
level::Junior|Middle|Senior
scope::Core|Overview
```

Необов’язкові теги:

```text
runtime::CPython
version::Py3_12
version::Py3_13
version::Py3_14
version::Py3_15_preview
source::PythonDocs
source::PEP
source::Community
review::NeedsFactCheck
card::PYI_05_014
```

Тег `runtime::CPython` обов’язковий для деталей bytecode, reference counting, GC, GIL,
interning та інших властивостей, не гарантованих усіма реалізаціями Python.

## Типи карток

- `Definition`: коротке й точне значення одного терміна.
- `Mechanism`: як або чому працює один механізм.
- `Contrast`: одна межа між двома близькими поняттями.
- `Code`: передбачити результат або поведінку та пояснити її.
- `Trap`: знайти помилку, хибне припущення або небезпечний edge case.
- `Scenario`: обрати інструмент чи підхід за заданих умов і назвати trade-off.

## Правила фронту

1. Одна головна перевірювана думка.
2. Запитання самодостатнє й однозначне без назви файлу або попередньої картки.
3. Не використовувати «розкажіть усе про…», довгі переліки та yes/no без пояснення.
4. Для коду питати і результат, і причину.
5. Указувати `Python`, `CPython`, версію або конфігурацію, якщо відповідь від цього залежить.
6. Не показувати тег теми на фронті: він не повинен бути підказкою.
7. Не питати довідкову дрібницю, яку розробник нормально перевіряє в документації.

## Правила відповіді

1. Перше речення – пряма відповідь.
2. Далі – механізм, мінімальний приклад або ключовий trade-off.
3. Типова довжина – 2–5 коротких речень, не враховуючи код і джерело.
4. Для списку перевіряється один критерій або невелика стабільна група, не енциклопедія.
5. Для CPython-деталей прямо писати, що це властивість CPython.
6. Для версійної поведінки додавати версію в текст і тег.
7. Посилання на джерело в даних картки обов’язкове для версійних, суперечливих або implementation-specific тверджень. Воно є службовим provenance і не відображається в шаблоні учня.

## Допустимі джерела

Пріоритет:

1. Python Language Reference, Standard Library docs, HOWTO.
2. PEP і документація CPython.
3. Документація стандартів або бібліотек у темах огляду.
4. Високоякісне community-джерело як джерело ідей, але не остаточна перевірка факту.

Правила добору описані в [SOURCE_POLICY.md](SOURCE_POLICY.md).

## Якість набору

- Покриття визначається картою теми, а не бажаною круглою кількістю карток.
- Дублікати за змістом об’єднуються, навіть якщо фронти сформульовані по-різному.
- Пов’язані погляди на важливу тему дозволені, якщо кожна картка перевіряє іншу операцію пам’яті.
- Картка нижче рівня реальної співбесіди вилучається або підсилюється сценарієм.
- Якщо відповідь неможливо чесно оцінити, фронт переписується.

## Приклад рядка

Символ `⇥` нижче лише показує місце TAB; у TSV має бути реальний TAB:

```text
Чим <code>is</code> відрізняється від <code>==</code>?⇥<span class="key"><code>is</code> перевіряє ідентичність об’єктів, а <code>==</code> – рівність значень.</span> Оператор <code>==</code> може викликати <code>__eq__</code>, тоді як <code>is</code> не перевантажується.⇥topic::03_objects_types_mutability type::Contrast level::Junior scope::Core
```
