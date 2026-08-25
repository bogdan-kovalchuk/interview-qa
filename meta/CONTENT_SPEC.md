# Специфікація файлу питання

Один файл = одне питання = одна сторінка = одна картка Anki.
Формат навмисно генератор-агностичний: чистий Markdown + YAML frontmatter, без MDX і без імпортів.

---

## 1. Розташування

```
content/{lang}/{track}/**/{slug}.md
content/en/python/asyncio/blocking-call-freezes-event-loop.md
content/uk/python/asyncio/blocking-call-freezes-event-loop.md
content/en/cpp/frameworks/qt/signal-slot-connection-types.md      # третій рівень дозволений
```

Шлях **рекурсивний**: таксономія має вкладені секції (`cpp/frameworks/qt`, `embedded/rtos/freertos`),
тож фіксована глибина не працює.

`slug` **однаковий в усіх мовах** – це те, що зв'язує переклади між собою і дозволяє перемикачу мов
працювати без мапи. Перекладається `title`, а не шлях.

**Ідентичність не виводиться зі шляху.** Канонічними є `id` і `section` у frontmatter; шлях мусить
їм відповідати, і валідатор звіряє це. Переміщення файлу не змінює ні `id`, ні `section` – воно або
супроводжується зміною frontmatter, або є помилкою.

---

## 2. Frontmatter

```yaml
---
# --- ідентичність (незмінне) ---
id: py-asyncio-0007

# --- відображення ---
title: Why does a blocking call freeze the whole asyncio event loop?
description: One line for the question list and for og:description. Written in this file's language.

# --- розташування (може змінюватись) ---
track: python
section: asyncio

# --- фасети ---
level: middle                  # junior | middle | senior
type: mechanism                # див. нормативний enum нижче
tags: [event-loop, blocking-io, executor]
frameworks: [fastapi]
# roles НЕ вказуються: членство в програмах виводиться з programs/*.yml (ADR-0010 §5)

# --- виконання і застосовність (необов'язково) ---
execution:
  language: python             # мова блоку коду; shell – теж мова
  standard: null               # стандарт мови (C++20) або null
  toolchain:                   # що саме виконало або скомпілювало приклад
    name: cpython
    version: "3.14.7"
  flags: []                    # прапорці збірки або запуску; [] – жодних
applies_to:
  - product: CPython
    version: "3.14"

# --- життєвий цикл ---
status: published              # див. нормативний enum нижче
updated: 2026-09-03

# --- ревізії і мовна синхронізація (I18N.md §7) ---
content_revision: 7            # зростає при кожній змістовній правці цього файлу
reconciled_with:               # з якими ревізіями інших мов цей файл узгоджений
  uk: 7

# --- зв'язки ---
see_also: [py-asyncio-0003, py-concurrency-0011]
prerequisites: [py-asyncio-0001]

# --- Anki ---
anki:
  export: true                 # false – сторінка без картки
  # deck НЕ вказується: виводиться з таксономії (ADR-0010 §5)
  # legacy_card_id НЕ існує: GUID детермінований від id (ADR-0011)

# --- джерела (обов'язково >= 1) ---
sources:
  - source_id: py314-asyncio-dev
    title: "Python 3.14: Developing with asyncio"
    url: https://docs.python.org/3.14/library/asyncio-dev.html
    accessed: 2026-09-03
    kind: official             # official | spec | book | community
    version: "3.14"
    applicability: CPython і сумісні реалізації Python з модулем asyncio
---
```

### Нормативні enum

Це **єдине місце**, де оголошено закриті словники `level`, `type` і `status`. Інші документи
описують семантику окремих значень або посилаються сюди, але не оголошують власних списків.

| Поле | Дозволені значення |
|---|---|
| `level` | `junior`, `middle`, `senior` |
| `type` | `concept`, `mechanism`, `comparison`, `pitfall`, `practical`, `coding`, `debugging`, `system-design`, `behavioral` |
| `status` | `draft`, `review`, `published`, `withdrawn` |

### Обов'язкові поля

`id`, `title`, `description`, `track`, `section`, `level`, `type`, `status`, `sources` (≥1),
`updated`, `content_revision`, `reconciled_with`.

`description` обов'язковий, бо його споживають два механізми, у яких немає запасного варіанту:
картка питання в списку на сайті й `og:description`. Без нього обидва беруть перший абзац тіла,
який у ще не написаного питання дорівнює `TODO`. Пишеться мовою файлу.

`content_revision` і `reconciled_with` обов'язкові в **кожному** мовному файлі: на них тримається
симетричний контракт ревізій (`I18N.md` §7) і ворота `lang-reconciliation`. `reconciled_with`
називає всі інші мови, що існують для цього питання, а не лише одну.

У кожному елементі `sources` обов'язкові `source_id`, `title`, `url`, `accessed`, `kind`, `version`
і `applicability`. Для джерела без власної версії `version: null` є явним і валідним значенням;
`applicability` усе одно має назвати межі, у яких джерело доречне. `source_id` унікальний у межах
питання, має формат `kebab-case` і не змінюється, поки те саме джерело підтримує ті самі твердження.

`execution` і `applies_to` необов'язкові. Якщо `execution` присутнє, воно має ключі `language`,
`standard`, `toolchain` і `flags`; не застосовний `standard` записується як `null`, а не
пропускається. `toolchain` має `name` і `version` і називає те, що **фактично виконало або
скомпілювало** приклад: `cpython 3.14.7`, `git 2.52.0`, `gcc 14.2`. `flags` – список прапорців
збірки або запуску, без яких приклад не відтворюється (`-fsanitize=address`); порожній список
є валідним і означає «жодних».

**Ілюстративний фрагмент – не виконуваний приклад.** Блок коду, який не збирається окремо
(без includes, без визначень типів, що згадуються), `execution` не оголошує: ворота
`example-executed` не мали б що запустити, а оголошене середовище стверджувало б перевірку, якої
не було. Такий фрагмент описує застосовність через `applies_to`, а потрібні прапорці – у тексті
секції. На пілотах це саме `cpp-tooling-0001`: два фрагменти на три рядки з `ThreadPool` і
`Session`, яких у файлі немає.

Розділення `language` і `toolchain` не косметичне. На пілотах поле зламалося з двох боків: у
git-задачі `version: "2.52"` описувала **інструмент**, а не мову, а в C++ прикладі з
`-fsanitize=address -fno-omit-frame-pointer -g -O1` для прапорців не було місця взагалі, і вони
лишились тільки в тексті. Ворота `example-executed` не мають runner, поки не знають toolchain.

Кожен елемент `applies_to` має `product` і `version`, де `version: null` означає явно
неверсійовану застосовність.

### Правила

- `id` унікальний глобально; перевіряється по `meta/id-registry.csv`.
- `anki.export: false` – для суто оглядових сторінок, які не стають картками.
- `sources` з `kind: community` **не рахується** як достатнє джерело – потрібне ще одне
  `official`/`spec`/`book`. Це переноситься з `SOURCE_POLICY.md` наявного репозиторію.
- `execution` задає середовище для воріт `example-executed`; воно обов'язкове для будь-якого
  питання з виконуваним або компільованим прикладом, незалежно від `type` – на пілотах це
  виявились `coding`, `practical` і `debugging`.
- `applies_to` задає застосовність питання, а `version` і `applicability` кожного джерела –
  застосовність доказу. Ворота `source-applicability` перевіряють обидва рівні.
- `updated` оновлюється при будь-якій зміні тіла.

---

## 2a. Рішення щодо legacy-фасетів – **підтверджено власником 2026-09-03**

**Критерій для всього блоку:** окремий facet зберігається лише тоді, коли його безпосередньо
споживає принаймні один визначений механізм: quality gate, selector програми, звіт або Anki tag.
Сам факт наявності legacy tag не є споживачем. Якщо зміст уже має точніше поле, міграція переносить
його туди без паралельного facet. Увесь цей блок є одним рішенням, яке власник може переглянути
до freeze схеми.

| Legacy facet | Рішення | Споживач і обґрунтування |
|---|---|---|
| `scope::Core` / `scope::Overview` | Не переносити як facet і не замінювати автоматично тегом | Жодні ворота, програма, звіт або картка не використовують цю дихотомію. `track`/`section`, `type` та `anki.export` уже описують структуру і відвантаження; новий `scope` був би неперевіреним дублем. |
| `runtime::CPython` | Не переносити як facet; перенести значення в `applies_to.product` і, для виконуваного прикладу, в `execution` | `source-applicability` та `example-executed` реально споживають ці точніші поля. Експортер може вивести Anki tag `runtime::cpython` із `applies_to`, не створюючи другого джерела істини. |
| `version::Py3_*` | Не переносити як facet; перенести в `applies_to.version`, `execution.toolchain.version` і `sources[].version` за роллю значення | Версія потрібна воротам застосовності й виконання. Один плоский facet не розрізняє версію питання, runtime прикладу та версію доказу. Anki tag `version::*` за потреби генерується з `applies_to`. |
| `gil::Enabled` / `gil::FreeThreaded` | Не переносити як окремий facet; записувати як кваліфікований `applies_to.product` (`CPython with GIL` або `CPython free-threaded build`) | Немає чинного selector або звіту для `gil`, а застосовність твердження вже перевіряє `source-applicability`. Кваліфікований product зберігає зміст 11 карток без нового словника; generated runtime tag лишається можливим. |
| `ref::TV_*` | Не переносити як facet; community-джерело отримує відповідний стабільний `source_id` | Це provenance, а не класифікація питання. `claim-linked`, `source-applicability` і поле Anki `Sources` споживають source record; окремий `ref` дублював би його. |

---

## 3. Тіло

Схема дискримінована за `type`: валідатор перевіряє повну послідовність заголовків, а не набір
секцій без порядку.

Дві позначки в таблиці, і вони взаємодоповнювальні:

| Позначка | Значення |
|---|---|
| `Evaluation guide*` | обов'язкова секція для `level: middle` і `level: senior`; для `junior` її не має бути |
| `[Follow-up]†` | єдина дозволена необов'язкова секція, і лише для `level: junior` |

Для middle і senior роль follow-up несе виключно підблок `Level-up follow-up` усередині
`Evaluation guide`. Два місця для одного й того самого дали б автору вибір без критерію: на
дев'яти пілотах необов'язкова `Follow-up` знадобилась рівно один раз, і саме там дублювала
`Level-up follow-up`. Для `behavioral` необов'язкова `Follow-up` заборонена на будь-якому рівні –
у цього типу вже є обов'язкова `Follow-up prompts`, і три схожі назви в одному файлі авторові
не пояснити.

| `type` | Повна упорядкована послідовність заголовків |
|---|---|
| `concept` | `Short answer` → `Detailed explanation` → `Evaluation guide*` → [`Follow-up`]† → `Sources` |
| `mechanism` | `Short answer` → `Detailed explanation` → `Evaluation guide*` → [`Follow-up`]† → `Sources` |
| `comparison` | `Short answer` → `Detailed explanation` → `Comparison` → `When to choose which` → `Evaluation guide*` → [`Follow-up`]† → `Sources` |
| `pitfall` | `Short answer` → `Detailed explanation` → `Symptom` → `Why it happens` → `How to avoid` → `Evaluation guide*` → [`Follow-up`]† → `Sources` |
| `coding` | `Task` → `Constraints` → `Short answer` → `Detailed explanation` → `Examples` → `Solution` → `Complexity` → `Edge cases` → `Tests` → `Evaluation guide*` → [`Follow-up`]† → `Sources` |
| `debugging` | `Short answer` → `Detailed explanation` → `Symptom` → `Observations` → [`Reproduction`] → `Hypotheses` → `Diagnosis` → `Fix` → `Prevention` → `Evaluation guide*` → [`Follow-up`]† → `Sources` |
| `system-design` | `Scale prompt` → `Short answer` → `Detailed explanation` → `Requirements` → `Scale assumptions` → `Architecture` → `Alternatives` → `Trade-offs` → `Failure modes` → `Evaluation guide*` → [`Follow-up`]† → `Sources` |
| `behavioral` | `Short answer` → `Detailed explanation` → `Competency assessed` → `STAR outline or illustrative example` → `Follow-up prompts` → `Evaluation guide*` → `Sources` |
| `practical` | `Short answer` → `Detailed explanation` → `Environment` → `Deliverable` → `Acceptance criteria` → `Evaluation guide*` → [`Follow-up`]† → `Sources` |

**`Evaluation guide` стоїть у кінці, а не третім.** Це interviewer guide: він оцінює відповідь,
тож не може передувати секціям, які цю відповідь формулюють. У попередній редакції він стояв
третім, і на пілотах це давало guide, який вимагає «сортує за початком перед проходом» за три
секції до `Task`, хвалить за sanitizer до `Symptom` і згадує ідемпотентність до `Requirements`.

**Для `coding` і `system-design` питання стоїть перед відповіддю.** `Front` цих типів будується
з `Task` + `Constraints` і зі `Scale prompt` (§5), тобто із секцій, які раніше лежали **після**
тієї, що стає `Back`. Файл читався знизу вгору, а експортер мусив читати вперед. Тепер порядок
секцій – це порядок читання, і він збігається з порядком складання картки.

`Short answer` є стабільною технічною назвою секції, яку використовує `LIFECYCLE.md`. Її зміст
і видима назва на картці залежать від `type`:

| `type` | Семантика `Short answer` |
|---|---|
| `coding` | `Solution outline`: стислий алгоритм і complexity, а не повна реалізація |
| `system-design` | `Architecture summary`: архітектурний кістяк і головні guarantees/trade-offs, а не повний design |
| `behavioral` | `Answer framework`: каркас для правдивої особистої історії, а не «правильна відповідь» |
| решта | коротка відповідь на питання |

`Scale prompt` для `system-design` містить не більше трьох числових або якісних припущень, без
розв'язку. Він додається до `Front`, щоб кандидат бачив потрібний масштаб до відповіді.

`Evaluation guide` має рівно три підзаголовки `###`: `Expected signals` (2–4 сигнали),
`Red flags` і `Level-up follow-up`. Навчальне пояснення в `Detailed explanation` не
дублює цей interviewer guide. Для `behavioral` це єдине місце для expected signals і red flags.

### Рівні заголовків

Секції з таблиці вище – рівно `##`. Підблоки `Evaluation guide` – рівно `###`. Інших `##` у тілі
бути не може: валідатор збирає послідовність секцій зі всіх `##`, і зайвий заголовок цього рівня
робить валідний файл невалідним. Заголовки глибше `###` не використовуються.

### Заголовки секцій – ідентифікатори, а не текст

У джерелі заголовки завжди англійські, в усіх мовах. Це структурні ідентифікатори: за ними
працюють `sections`, `lang-structure-parity` і обчислення `completeness`, і перекладений заголовок
зламав би всі три. Видима назва секції на сторінці приходить з `content/i18n/{lang}.json` під час
генерації дзеркала (`I18N.md` §5) – саме тому в шаблонах немає жодного зашитого рядка.

`Reproduction` у `debugging` додається лише для відтворюваного дефекту. Якщо секція присутня, вона
стоїть рівно після `Observations` і задає достатні для повторення кроки, fixture/data та очікуваний
симптом. Не застосовну секцію пропускають, а не заповнюють `TODO`.

`Sources` **завжди присутня в авторському файлі як останній заголовок** з єдиним точним body:

```markdown
## Sources

<!-- generated from frontmatter -->
```

Автор не додає під ним джерела вручну. Генератор замінює comment списком із `sources` для сайту
і формує поле `Sources` для Anki.

---

## 3a. Скелет існує завжди

**Основне правило проєкту:**

> Питання створюється **повністю** – обидві мовні версії, усі обов'язкові для його `type` і `level`
> секції, сторінка на сайті, зарезервоване місце в колоді. Те, що ще не написано, позначається
> явним маркером `TODO`, а не відсутнє.

Необов'язкові `Follow-up` і `Reproduction` додаються лише за потреби, і кожна має власну умову:
`Follow-up` – лише для `level: junior`, `Reproduction` – лише для відтворюваного дефекту в
`debugging`. Якщо їх немає, це не дірка.
Усі інші заголовки з відповідного рядка §3 мусять існувати від створення файлу.

### Маркер `TODO`

Секція, вміст якої ще не написано, містить рівно один рядок:

```markdown
## Detailed explanation

TODO
```

Це секція **з маркером `TODO`**, а не порожня секція. Порожня секція невалідна. Валідатор
розрізняє три стани: заголовка немає (структурна помилка), body дорівнює `TODO` (штатно не
написано), body має інший вміст (написано).

Те саме для мовної версії, текст якої ще не написано: файл створюється з тим самим `id`, тим самим
`slug`, повним frontmatter і `TODO` у всіх обов'язкових текстових секціях. `Sources` зберігає
службовий comment, а не `TODO`.

### Повнота – це проєкція, а не ворота публікації

`completeness` обчислюється лише з обов'язкових секцій відповідного рядка §3; необов'язкові
`Follow-up` і `Reproduction` не враховуються. Точні стани й наслідки задає `LIFECYCLE.md`.

| Рівень | Що вже написано |
|---|---|
| `empty` | `Short answer` дорівнює `TODO` |
| `stub` | `Short answer` написано, решта обов'язкових секцій може бути `TODO` |
| `partial` | `Short answer` і `Detailed explanation` написано, решта обов'язкових може бути `TODO` |
| `complete` | усі обов'язкові для `type` і `level` секції написано |

### Сайт і Anki

Поява сторінки, картки й `Reference` визначається лише `LIFECYCLE.md`. Цей документ не має другої
копії тих правил. `id`, URL і GUID резервуються під час створення, а ненаписані секції на доступній
за lifecycle сторінці рендеряться як «ще не написано».

---

## 3b. Що саме доводять джерела – за типами

`sources` вимагає щонайменше одного не-`community` джерела, а `claim-linked` – прив'язки
нетривіальних тверджень до `source_id`. Для семи типів це працює прямо. Для двох – ні, і на
пілотах це виявилось найгострішою знахідкою: ворота проходили, а прив'язка перетворювалась на
театр, бо токен ставили там, де джерело є, а не там, де твердження потребує доказу.

| `type` | Що доводять джерела | Чим доводиться сама відповідь |
|---|---|---|
| `coding` | твердження про складність, семантику API і гарантії мови | `execution` і секція `Tests`: розв'язання доводиться виконанням, а не цитатою |
| `behavioral` | що цю компетенцію справді так оцінюють – рамки, leadership principles, книги | нічим зовнішнім: `Short answer` є каркасом для правдивої особистої історії, а не твердженням про світ |
| решта сімох | самі твердження відповіді | тим самим |

Практичні наслідки:

- для `coding` citation token обов'язковий на твердженнях про складність та API і **не**
  вимагається на кроках розв'язання. Пілот `py-prac-0001` цитував `listsort.txt` і Sorting HOWTO –
  вони підтримують побічне твердження про складність сортування, і це коректно саме як таке;
- для `behavioral` джерела описують компетенцію, а не відповідь. `kind: community` тут так само
  недостатній: рамка компетенцій або книга – це `book`/`official`, і вони доступні;
- для решти семи типів нічого не змінюється.

Ворота `claim-linked` читають цю таблицю, а не застосовують одне правило до всіх дев'яти типів.

---

## 3c. Прив'язка тверджень до джерел

Нетривіальне перевірне твердження завершується citation token `[^source_id]`, де `source_id`
дорівнює полю одного елемента `sources`:

```markdown
Python evaluates default argument expressions when the function definition executes.[^py-faq-defaults]
```

Визначення footnote вручну не пишеться: генератор матеріалізує його з frontmatter у `Sources`.
Token ставиться одразу після речення або абзацу, який підтримує джерело. Один claim може мати
кілька token, а один token може підтримувати кілька сусідніх речень лише в тому самому абзаці.
URL джерела має вести на точний розділ або anchor, якщо джерело його надає.

Citation token дозволений у `Short answer` і не рахується посиланням або словом для card limits;
експортер прибирає marker з видимого `Back`, але зберігає відповідне джерело в полі `Sources`.

---

## 3d. Наслідки для валідації

- `completeness` рахує лише обов'язкові для `type` і `level` секції;
- обидві мовні версії мають однаковий набір і порядок секцій, включно з однаковим рішенням про
  необов'язкові секції;
- приклади коду виконуються або компілюються в середовищі `execution` – скрізь, де таке
  середовище оголошене;
- `claim-linked` перевіряє citation token за таблицею §3b, а `source-applicability` – метадані
  питання і джерела;
- схема заморожується лише після двомовних пілотів і закриття `SPEC_DEFECTS.md`.

---

## 4. Крос-посилання

Тільки через токен `qid:`:

```markdown
[текст](qid:py-asyncio-0011)
```

**Не** через відносні шляхи до файлів і **не** через готовий URL. Причина остання важлива: сайт
живе на GitHub Pages з base path `/interview-qa/`, тож root-relative `/q/...` вело б на корінь
домену, а не в проєкт (ADR-0010 §2).

Токен матеріалізує споживач:

| Споживач | Результат |
|---|---|
| сайт | `{base}/{lang}/q/{id}/` з урахуванням `base: '/interview-qa'` |
| `questions.json` | `{"qid": "py-asyncio-0011"}` – без URL |
| Anki | абсолютний `https://…/interview-qa/{lang}/q/{id}/` |

Один і той самий Markdown лишається коректним у всіх трьох контекстах, а зміна хоста чи base path
не потребує правки жодного файлу контенту.

Валідатор перевіряє, що кожен `qid:` вказує на існуючий ID.

---

## 5. Обмеження для `Short answer`

Оскільки цей текст рендериться на картці:

- 2–5 речень, не рахуючи code block і citation token;
- понад 90 слів без code block і citation token – м'яке попередження валідатора, а не помилка;
  ліміт **виміряний не на всіх типах**: його брали з legacy-колоди, у якій немає жодного
  `behavioral` чи `system-design`. На пілотах саме ці два типи в нього й не вклалися в першій
  чесній редакції (`behavioral` – 111 слів, `system-design` – 88, `practical` – 91), тож для них
  попередження очікуване і не є сигналом про поганий текст. Рахуйте також, що `.key` і `.warn`
  з'їдають бюджет швидше за звичайний текст: виділений фрагмент читається довше, ніж важить;
- без заголовків, без багаторівневих списків;
- інлайн-код і не більше одного fenced code block дозволені;
- без Markdown-посилань; citation token `[^source_id]` є окремим синтаксисом і не рендериться
  як видиме посилання в `Back`;
- якщо відповідь починається з `**жирного фрагмента**`, експортер рендерить цей перший фрагмент
  як `<span class="key">…</span>`; інший bold лишається звичайним `<strong>`;
- явний inline HTML `<span class="warn">…</span>` дозволений **лише** у `Short answer`;
  інші inline HTML елементи там заборонені, а `.warn` не можна вкладати в `.key`;
- термін мовою оригіналу лишається англійською навіть в українському тексті
  (`event loop`, `GIL`, `move semantics`) – це успадкована політика з наявного репозиторію.

### Type-specific mapping у поля Anki

| `type` | `Front` | `Back` |
|---|---|---|
| `coding` | `title`, потім повний `Task` і compact-rendered `Constraints` | `Short answer`, видима мітка `Solution outline` |
| `system-design` | `title`, потім `Scale prompt` | `Short answer`, видима мітка `Architecture summary` |
| `behavioral` | `title` | `Short answer`, видима мітка `Answer framework` |
| решта | `title` | `Short answer` без додаткової мітки |

Compact rendering змінює лише HTML: прибирає зайві paragraph margins і показує `Constraints`
однорівневим списком. Експортер не скорочує, не переказує і не відкидає authored constraints.
`Reference` і `QID` заповнюються однаково для всіх типів; умови появи картки визначає лише
`LIFECYCLE.md`.

### Рендер поля `Sources`

Поле `Sources` – **приховане provenance** (`.source { display: none }` у шаблоні), а не видимий
блок. Звідси рендер:

- один рядок на джерело, у порядку frontmatter: `title` як текст посилання, `url` як href;
- `version`, `accessed`, `kind` і `applicability` у поле **не йдуть** – вони лишаються на сторінці
  сайту, де є місце і де їх читають;
- ліміту на кількість джерел немає навмисно. Він був би потрібен, якби поле показувалось: пілот
  `py-gil-0001` має чотири джерела з повними метаданими, і в розгорнутому вигляді `Sources`
  вийшло б довшим за `Back`. Але рендер вище зводить кожне джерело до одного рядка, а обрізане
  provenance гірше за довге: саме за ним звіряють твердження.

---

## 6. Мінімальний приклад

Це **український** файл питання: `content/uk/cpp/stl-containers/…md`. Тіло українське, заголовки
секцій англійські (§3), `title` і `description` – мовою файлу, а `reconciled_with` називає іншу
мову, а не власну.

```markdown
---
id: cpp-mem-0012
title: Чому std::vector інвалідує ітератори на push_back?
description: Перевиділення буфера переносить елементи, і всі ітератори на них стають недійсними.
track: cpp
section: stl-containers
level: middle
type: mechanism
tags: [iterator-invalidation, reallocation]
status: published
updated: 2026-09-03
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
applies_to:
  - product: ISO C++
    version: "C++20"
sources:
  - source_id: cppreference-vector-push-back
    title: "cppreference: std::vector::push_back"
    url: https://en.cppreference.com/w/cpp/container/vector/push_back
    accessed: 2026-09-03
    kind: spec
    version: "C++20"
    applicability: std::vector::push_back invalidation rules through C++20
---

## Short answer

**`push_back` може перевищити `capacity` і перевиділити буфер**, перемістивши елементи за новою
адресою. Всі ітератори, вказівники та посилання на елементи стають недійсними; якщо
перевиділення не сталося, недійсним стає лише `end()`.[^cppreference-vector-push-back]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
```
