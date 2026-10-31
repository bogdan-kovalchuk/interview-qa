# Quality gates

Перевіряється лише те, що дешево ловить реальну поломку: структуру файлу, ID, мовний паритет,
посилання й межі картки. Плейсхолдер `TODO` звільняє **лише** від наявності тексту, а не від
структури, ID чи паритету.

Усі ворота нижче блокуючі, крім позначених як попередження. Кожні мають негативну фікстуру в
`tests/fixtures/negative/`; реалізація – `tools/iqa/validate.py`.

## Контент

| Ворота | Що перевіряє |
|---|---|
| `schema` | frontmatter відповідає моделі (`meta/question.schema.json` згенеровано з `tools/iqa/model.py` і не застарів): лише `id`, `title`, `track`, `section`, необов'язкові `sources`; у тексті немає em dash U+2014 і стрілок U+2190/U+2192 |
| `id-unique` | `id` не повторюється в межах мови й веде на один шлях |
| `id-immutable` | кожен `id` є в `meta/id-registry.csv` зі `status: published` і тим самим шляхом; префікс секції збігається з `section_prefixes` або `section_prefix_aliases`; `retired` має причину; рядок `published` без файлів – помилка |
| `sections` | `[Question code] -> Short answer -> Detailed explanation`, без інших `##`; `###` лише в `Detailed explanation`; жодних `#` чи `####`; порожня секція – помилка; `Question code` – рівно один блок коду й не `TODO` |
| `short-answer-limits` | 2–5 речень; не більше одного блока коду; без заголовків, вкладених списків і посилань; `.warn` лише тут і не всередині жирного фрагмента; **понад 90 слів – попередження** |
| `sources` | кожен `[^source_id]` називає джерело з `sources`; виносок `[^x]:` немає |
| `xref` | кожен `qid:` резолвиться і не стоїть в інлайн-коді; готових URL і Markdown-посилань немає |
| `taxonomy` | `track/section` є в `meta/taxonomy.md`, шлях файлу їм відповідає, у треку й секції є видимі мітки й префікс ID; секція в `meta/order.yml` перелічує рівно свої питання, кожне один раз |

**Пошук URL не бачить коду.** `short-answer-limits` і `xref` шукають `[текст](ціль)` і голий
`http://` у тексті без fenced-блоків і без інлайн-коду: `` `table[opcode](ctx, frame)` `` – масив
вказівників на функції в C, а не посилання. Лічильники речень і слів не залежать від форми
розмітки: `<code>x</code>` і `` `x` ``, `<span class="key">` і `**…**` рахуються однаково, а `<` в
коді не читається як тег.

## Паритет мов

| Ворота | Що перевіряє |
|---|---|
| `lang-files-exist` | існують обидва мовні файли з однаковим шляхом |
| `lang-structure-parity` | однакові трек, секція, набір і порядок секцій; у секції, написаній обома мовами, однакова кількість `###` |
| `lang-code-identical` | блоки коду побайтово збігаються в секціях, написаних в обох мовах |
| `lang-links-parity` | однаковий набір `sources`; у написаних в обох мовах секціях – однакові citation-токени й `qid:` |
| `lang-glossary` | терміни у формі зі словника `meta/vocabulary.yml:glossary` |
| `lang-script` | в англійському `title` і тексті поза кодом немає кирилиці; код однаковий в обох мовах, а назви джерел лишаються мовою джерела |

Секція, що дорівнює `TODO` хоча б в одній мові, з порівнянь коду й токенів виключається: їй
нема з чим збігатися. Дві написані секції порівнюються повністю. Якості перекладу ці ворота не
доводять, і це прийнята ціна.

## Anki

`tests/test_anki_build.py`: формула GUID збігається із замороженими векторами, мовні простори GUID
і корені колод не перетинаються, трековий пакет – підмножина Full Library з тими самими GUID,
картка їде рівно тоді, коли написано `Short answer`, шаблони не розбирають QID, поля пишуться за
іменем, `Question code` іде на `Front`.

## Сайт

`tools/iqa/verify_build.py` після production-збірки з `base=/interview-qa`: набір сторінок
питань збігається з моделлю (ні зайвих, ні відсутніх), кожна внутрішня адреса має base і веде на
наявну сторінку, resolver-сторінки мають canonical і fallback-посилання, є `hreflang` обох мов,
немає сирих `[^token]` і англійських заголовків секцій на `/uk/`, є корінь, `robots.txt` і sitemap.

## Пайплайни

| Тригер | Workflow | Що виконується |
|---|---|---|
| PR у `main` і push у `main` | `ci.yml` | `check-pinned-actions`, `iqa validate`, `pytest`, `iqa build` |
| ручний запуск | `deploy.yml` | той самий build path, потім деплой на GitHub Pages |
| тег `deck-v*` або ручний запуск з версією | `release.yml` | `iqa validate`, `pytest`, `iqa build`, вісім `.apkg` з `.sha256`, GitHub Release |

Кожен `uses:` запінений за commit SHA; це перевіряє `python -m iqa check-pinned-actions`.

**Деплой навмисно не на `push`**: власник не давав дозволу на автопублікацію. Коли дасть, у
`deploy.yml` додається тригер `push: branches: [main]`.

**Реліз колоди – з коміту тега**, а не з поточного `main`, щоб реліз відтворювався з незмінної
точки. Ручний запуск з версією (`v2026.10.1`) ставить тег `deck-<version>` на коміт, який зібрано.

**Lockfiles.** `requirements/python-lock.txt` (`pip-compile --generate-hashes`) і
`site/package-lock.json` комітяться; CI ставить залежності лише з них. Регенерація Python-лока:

```
pip install pip-tools
pip-compile --extra test --generate-hashes -o requirements/python-lock.txt pyproject.toml
```

Аудиту вразливостей і ліцензій у CI немає – свідомо відкладено.

## Локальний запуск, ідентичний CI

```
pip install --require-hashes -r requirements/python-lock.txt
pip install --no-deps -e .
cd site && npm ci && cd ..
python -m iqa check-pinned-actions
python -m iqa validate
python -m pytest --basetemp=<writable dir поза репозиторієм>
python -m iqa build
```

`npm ci` і `iqa build` створюють тисячі файлів, тож повну збірку запускають у копії репозиторію
поза синхронізованими теками.
