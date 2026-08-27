# Quality gates

Усе, що не перевіряє CI, з часом розсинхронізується. **Блокуючі** ворота не пропускають PR;
**звітні** пишуть коментар і не блокують.

Межа проста: плейсхолдер `TODO` звільняє **лише** від наявності тексту. Він не звільняє від
структури, ID, джерел і мовного паритету – саме там борг потім дорого виправляти. `completeness`
не є воротами взагалі: вона обчислюється зі сканування і йде у звіти й теги.

Мовний паритет (`lang-code-identical`, `lang-links-parity`) звіряє **написаний** текст, а не файл
цілком: секція, що дорівнює `TODO` в однієй з мов, не має коду й citation-токенів, які могли б із
чимось збігатися чи розходитися, тож вона виключається з обох порівнянь – з обох боків одразу, коли
`TODO` хоч на одній стороні. Секція, написана **в обох** мовах, порівнюється повністю, як і раніше:
виняток лише прибирає хибне спрацювання «TODO-секція не збігається з написаною», він не послаблює
перевірку двох написаних секцій одна проти одної.

## Контент – блокуючі

| Ворота | Що перевіряє |
|---|---|
| `schema` | frontmatter відповідає `meta/schema/question.schema.json` |
| `id-unique` | `id` не повторюється (звірка з `meta/id-registry.csv`) |
| `id-immutable` | наявний `id` не змінив значення і не перевикористаний після видалення |
| `sections` | усі обов'язкові секції у правильному порядку; секції – рівно `##`, підблоки `Evaluation guide` – рівно `###`, інших `##` немає |
| `sections-by-level` | `Evaluation guide` є для `middle`/`senior` і відсутній для `junior`; необов'язкова `Follow-up` лише для `junior` і ніколи для `behavioral` |
| `short-answer-limits` | 2–5 речень; понад 90 слів – м'яке попередження; без заголовків і готових URL |
| `sources` | ≥1 джерело; якщо всі `kind: community` – відхилити |
| `facets-vocabulary` | `level`, `type`, `status`, `frameworks` – тільки зі словників |
| `xref` | кожен токен `qid:` резолвиться; готових URL у контенті немає |
| `taxonomy` | `track`/`section` існують у `meta/TAXONOMY.md`, і шлях їм відповідає |
| `no-duplicates` | семантичний дублікат (схожість `title` + перетин тегів) – **звітне**, бо потребує ручного підтвердження і не може блокувати unattended CI |

## Паритет мов – блокуючі

| Ворота | Що перевіряє |
|---|---|
| `lang-files-exist` | існують **обидва** мовні файли (вміст може бути `TODO`) |
| `lang-structure-parity` | однаковий набір і порядок секцій |
| `lang-code-identical` | блоки коду побайтово збігаються – переклад не править код; секція `TODO` в одній із мов не порівнюється |
| `lang-links-parity` | однаковий набір `sources` (завжди, з frontmatter); citation-токени і токени `qid:` звіряються лише в секціях, написаних в обох мовах |
| `lang-glossary` | терміни у формі зі словника `meta/vocabulary.yml` |
| `lang-reconciliation` | `content_revision` однієї мови не випереджає `reconciled_with` іншої – **звітне** |

Воріт якості перекладу тут немає і не буде: AI-переклад – це звичайний переклад. Parity ловить
механічні поломки, а семантику не доводить ніщо – і це прийнята ціна, а не дірка.

## Anki – блокуючі

| Ворота | Що перевіряє |
|---|---|
| `anki-guid-stability` | жоден GUID не змінився відносно попереднього релізу |
| `anki-identity-stable` | жоден `qid` не змінив свій GUID відносно останнього release manifest |
| `anki-notetype-stable` | `notetype_fingerprint` не змінився відносно базової лінії релізу |
| `anki-tsv-format` | рівно N табуляцій, один фізичний рядок на картку, UTF-8 |
| `anki-no-silent-removal` | питання, що зникло з джерела, має явний `withdrawn` |
| `anki-reference-url` | поле `Reference` збігається з реально згенерованим `/uk/q/{id}/` |
| `anki-import-smoke` | імпорт у чисту колекцію + повторний імпорт не створює дублікатів |
| `anki-edit-preserves-progress` | правка полів і тегів + повторний імпорт – розклад не змінився |

`anki-guid-stability` і повторний імпорт – два найважливіші тести в проєкті. Помилка тут
виявляється не в CI, а у втраченому прогресі, і виправити її вже неможливо.

## Сайт і збірка – блокуючі

| Ворота | Що перевіряє |
|---|---|
| `build` | сайт збирається без помилок для обох локалей |
| `permalink-coverage` | для кожного опублікованого питання є `/q/{id}/` кожною мовою |
| `internal-links` | немає битих внутрішніх посилань – на **production-збірці** з `base=/interview-qa` |
| `production-base` | усі `href` у зібраному HTML коректні під base path |
| `canonical-hreflang` | кожна сторінка має `canonical`, обидві мови – `hreflang` |
| `sitemap-robots` | `sitemap.xml` і `robots.txt` згенеровані й валідні |
| `a11y-smoke` | базова перевірка доступності на репрезентативних сторінках |
| `lockfiles` | Python lock і Node lock присутні й актуальні |
| `pinned-actions` | GitHub Actions запінені за immutable commit SHA, не за тегом |
| `dependency-audit` | аудит вразливостей і ліцензій; `THIRD_PARTY_NOTICES` актуальний |
| `release-checksums` | контрольні суми артефактів релізу |
| `no-em-dash` | у жодному `.md` немає U+2014 |

## Достовірність тверджень

Три різні твердження – «джерело є», «джерело підтверджує це твердження» і «приклад виконано» –
розділені навмисно: перше нічого не каже про друге.

| Ворота | Що перевіряє | Тип |
|---|---|---|
| `source-present` | ≥1 джерело, не лише `community` | автоматичне |
| `claim-linked` | наявність `source_id` на нетривіальних твердженнях, **за таблицею типів** у `QUESTIONS.md` §6 | блокує лише наявність; доречність – звіт авторові, не ворота |
| `source-applicability` | у джерела є версія, дата доступу і межі застосовності | автоматичне |
| `example-executed` | приклад компілюється або виконується в оголошеному `execution`: `toolchain` як runner, `flags` обов'язкові | автоматичне |
| `review-invalidated` | змістовна правка тіла скидає позначку пройденого рев'ю | автоматичне |

`claim-linked` читає таблицю типів, а не застосовує одне правило до всіх дев'яти: для `coding`
розв'язання доводить `execution` і `Tests`, а не цитата; для `behavioral` джерела документують
компетенцію, а не правильність відповіді.

## Звітні

| Звіт | Навіщо |
|---|---|
| `translation-coverage` | скільки перекладено; що потребує узгодження |
| `external-links` | мертві зовнішні URL – щотижневим cron, не на PR |
| `track-coverage` | розподіл по треках, рівнях, типах – видно перекоси |
| `program-coverage` | наскільки готова кожна програма |
| `orphans` | питання без вхідних посилань і без жодної програми |

## Пайплайни

CI написаний і реально блокує: три workflow у `.github/workflows/`, кожен `uses:` у них запінений
за commit SHA, перевіреним GitHub API і `git ls-remote` окремо (не вигаданим – **`pinned-actions`
тепер реальна перевірка**, `tools/iqa/pinned_actions.py`, викликається як
`python -m iqa check-pinned-actions`, тест `tests/test_pinned_actions.py` з негативним кейсом на
`@v4`). Жоден із трьох файлів нічого не реалізує заново: усі викликають `tools/iqa/`,
`tools/verify_build.py` і `packaging/anki/build.py`, які вже працювали до цього кроку.

| Тригер | Workflow | Що виконується |
|---|---|---|
| PR у `main` і push у `main` | `ci.yml` | `check-pinned-actions`, `iqa validate`, `pytest`, `iqa build` (validate -> export -> mirror -> astro build -> verify) |
| ручний запуск (`workflow_dispatch`) | `deploy.yml` | той самий build path, потім `configure-pages` -> `upload-pages-artifact` -> `deploy-pages` |
| тег `deck-v*` | `release.yml` | `iqa validate`, `pytest`, `iqa build`, збірка `.apkg`, sha256, GitHub Release |
| щотижневий cron | – | **не реалізовано в цьому кроці** – `external-links` і звіт застарілих перекладів лишаються ручним запуском; окремий workflow – майбутня робота, не обіцяна тут |

### Деплой навмисно не на `push`

`deploy.yml` тригериться лише `workflow_dispatch`. Власник не давав дозволу на автопублікацію
(`AGENTS.md`: «Не публікувати нічого назовні без прямого дозволу»), а деплой на GitHub Pages –
саме зовнішня публікація. Це рішення, не недогляд: коли власник дозволить, у файлі один рядок,
позначений коментарем на початку `deploy.yml`, вмикає деплой на кожен merge у `main`:

```yaml
on:
  workflow_dispatch:
  push:
    branches: [main]
```

### Реліз колоди – з тега, не з `main`

`release.yml` тригериться на push тега `deck-v*` і збирає **комміт, на який вказує тег**
(`actions/checkout` за замовчуванням бере `github.ref`, для тега це сам тег), а не поточний
`main`. Реліз мусить відтворюватись з незмінної точки: якби збірка йшла з `main`, два запуски
одного тега могли б дати різну колоду, якщо `main` встиг змінитися між ними.

`.apkg` називається `Interview QA - Full Library-<version>.apkg`, де `<version>` – хвіст тега
після `deck-` (тег `deck-v2026.09.1` дає файл `...-v2026.09.1.apkg`), у форматі версії з
`meta/ANKI.md`. Поруч – `<...>.apkg.sha256` (`release-checksums`).

**Ворота Anki, які реально виконуються, і які ні:** `anki-guid-stability`, `anki-identity-stable`,
`anki-notetype-stable`, `anki-no-silent-removal`, `anki-edit-preserves-progress` – це діфи проти
`packaging/anki/releases/<попередня-версія>.json`. Такого файлу ще немає: перший release manifest
з'являється в `PLAN.md`, крок 4, чекпойнт 4 (базова лінія), і діфитись поки нема з чим. Жоден
скрипт цей діф не рахує – `release.yml` його не вигадує. Реально виконується: `iqa validate`,
повний `pytest` (включно з `tests/test_anki_build.py` – формула GUID збігається з еталонною
реалізацією, шаблони не парсять QID, кожен пілот віддає картку, поля пишуться за іменем), і
`iqa build`, який валить збірку, якщо `Reference`-URL картки не відповідає сторінці, яку
production-збірка реально видає. Дописати діф-ворота – робота того, хто в кроці 4 напише
`packaging/anki/releases/<version>.json`.

### Lockfiles

`requirements-lock.txt` (корінь репозиторію) – Python, згенерований `pip-compile --generate-hashes`
з `pyproject.toml` (`[project] dependencies` + `[project.optional-dependencies] test`); CI ставить
залежності лише командою `pip install --require-hashes -r requirements-lock.txt`, без резолву з
PyPI під час збірки. `site/package-lock.json` – Node, як і раніше; CI ставить `npm ci`. Обидва
файли комітяться. Регенерація Python-лока (коли зміниться `pyproject.toml`):

```
pip install pip-tools
pip-compile --extra test --generate-hashes -o requirements-lock.txt pyproject.toml
```

Під час цього кроку виявилось, що `genanki` – реальна залежність (`packaging/anki/build.py`,
`tests/test_anki_build.py`), яка не була в `pyproject.toml`. Додано до `[project] dependencies`;
без цього лок і `pip install --no-deps -e .` не покривали б пакет, який тести й реліз реально
імпортують.

### `dependency-audit` – відкладено, явно

CI цього кроку **не запускає** жодного аудитора вразливостей чи ліцензій. Ні `pip-audit`, ні
`npm audit`, ні звірка `THIRD_PARTY_NOTICES` нікуди не викликаються – рядок у таблиці вище
залишається цільовим дизайном, не описом того, що виконується. `THIRD_PARTY_NOTICES` – предмет
`PLAN.md` кроку 4, чекпойнта 4 (реліз, OFL-тексти шрифтів). Додати `dependency-audit` в CI –
майбутня робота: не зроблено зараз, і це навмисно сказано тут, а не замовчано.

### Раннер, версії, кеш, дозволи

Усі три workflow – `ubuntu-latest`: дефолтний, найдешевший і найшвидший клас раннерів GitHub
Actions, і `astro`/`pagefind`/`genanki` не мають нічого, що вимагає саме Windows чи macOS. Окремо
виміряно на робочій Windows-машині: повторний локальний запуск `iqa build` без очищення
попереднього дзеркала періодично ловив `WinError 5` від `shutil.rmtree` (файловий вотчер –
VS Code чи антивірус – тримає щойно створений файл частку секунди). У CI кожен запуск – чистий
checkout, дзеркала з попереднього разу там немає, тож цей конкретний рейс там не відтворюється
незалежно від ОС раннера; це спостереження, а не причина вибору `ubuntu-latest`, і тому винесено
окремо, а не видано за обґрунтування. Python `3.14` (те, що вимагає `pyproject.toml` і що реально
протестовано локально). Node `24` (задовольняє `astro` `engines.node: >=22.0.0`, і це версія, з
якою сайт реально збирався локально при написанні цього кроку).

Кеш: `actions/setup-python` кешує `pip` за `requirements-lock.txt`; `actions/setup-node` кешує
`npm` за `site/package-lock.json`. Дозволи – за принципом найменших прав: `ci.yml` –
`contents: read` (нічого не публікує); `deploy.yml` – `contents: read`, `pages: write`,
`id-token: write` (потрібно `actions/deploy-pages`); `release.yml` – `contents: write` (створити
Release й додати asset), без `pages` і без `id-token`. Конкурентність: `ci.yml` скасовує
попередній запуск на тому самому ref (`cancel-in-progress: true` – новий пуш робить старий
запуск нерелевантним); `deploy.yml` – групою `pages`, без скасування (не перебивати живий
деплой); `release.yml` – групою за тегом.

### Один локальний запуск, ідентичний CI

```
pip install --require-hashes -r requirements-lock.txt
pip install --no-deps -e .
cd site && npm ci && cd ..
python -m iqa check-pinned-actions
python -m iqa validate
python -m pytest --basetemp=<writable dir>
python -m iqa build
```

Той самий порядок, ті самі команди, що й у `ci.yml` – «проходить локально» і «проходить у CI»
означають одне й те саме. `<writable dir>` – будь-яка тека, куди процес точно може писати:
дефолтна тимчасова тека pytest на цій машині періодично виявляється недоступною для запису.

## Що перевіряє рев'ю, а не CI

- питання справді ставлять на інтерв'ю, а не «цікавий факт»;
- одне питання перевіряє одну ідею;
- відповідь не переказує джерело дослівно;
- приклад мінімальний і відтворюваний;
- канонічна домівка обрана за правилом найвужчого треку, а не за зручністю;
- версійні твердження мають кваліфікатор (Python 3.14, C++20, GCC 13).
