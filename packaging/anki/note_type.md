# Note type: Interview QA Basic

Єдиний note type проєкту. Створюється білдером одразу в цільовому вигляді; **структура
заморожується з першого пакета, що потрапить комусь у руки** (ADR-0010 §1).

Predecessor-модель `Python Interview Basic` (`model_id 1788409800655`) не успадковується. Spike
M0.4 виміряв, що її нотаток немає в жодній колекції: у реальному профілі нуль нотаток на цій
моделі й жодного predecessor-GUID, а сам `.apkg` не мав каналу розповсюдження. Успадковувати
двопольову структуру не було для кого, і це був останній момент, коли тип можна обрати вільно.

Після першого релізу міняти `model_id`, поля чи кількість шаблонів не можна. Причина виміряна на
spike M0.4, а не взята з документації: пакет із тим самим GUID, але іншим `model_id`, не дає
помилки й не дублює нотатки – Anki переводить нотатку на об'єднаний тип, зсуває поля на інші ord,
додає другий template і **створює зайві картки** (392 → 395 на трьох нотатках). Тиха структурна
корупція гірша за явну помилку. Деталі: `meta/migration/anki-compatibility-report.md`,
експеримент J.

## Fingerprint

| Елемент | Значення |
|---|---|
| `model_id` | `1600000000001` |
| назва | `Interview QA Basic` |
| `Front` | `ord 0`, field id `1600000001001` |
| `Back` | `ord 1`, field id `1600000001002` |
| `Reference` | `ord 2`, field id `1600000001003` |
| `Sources` | `ord 3`, field id `1600000001004` |
| `QID` | `ord 4`, field id `1600000001005` |
| template | `Card 1`, `ord 0`, id `1600000001101` |

Fingerprint для CI: `sha256(model_id + [field id, name, ord]* + [template id, ord]*)`.
Це визначення – канонічне; `QUALITY_GATES.md` і ADR-0009 §3 посилаються на нього.

**Усі ідентифікатори задані явно.** `model_id` і базу `1600000001###` навмисно взято з минулого,
щоб timestamp-генератор Anki ніколи не видав такі самі й не сталося колізії. Оскільки `genanki`
приймає field і template ids у моделі, повний fingerprint відомий **до** першого релізу, а не
після нього: базова лінія діфів фіксується першою ж збіркою CI, без ручного кроку.

### Перевірено на spike M0.4 і довимірюванні F

- `genanki 0.13.1` створює тип із явними `model_id`, field ids, ord, template id і GUID нотаток;
  імпорт у порожню колекцію дав рівно очікувану структуру, оновлення наявних нотаток – без
  дублікатів (експеримент G).
- Схема ids `1600000000001` / `1600000001001–1005` / `1600000001101` уже відпрацьована на живій
  фікстурі довимірювання F (`meta/migration/anki-tag-refresh.md`,
  `packaging/anki/spike/run_tag_refresh.py`).
- Редагування `Front`, `Back`, `Reference`, `Sources`, `QID` на 20 картках із реальною історією
  повторень **не змінило жодного з дев'яти scheduling-значень** (експеримент B).

## Що змінюється відносно попередньої версії

| Було | Стало |
|---|---|
| посилання «Розгорнуте пояснення» – **константа в шаблоні** з `https://example.com/...` | поле `Reference`, своє для кожної картки |
| джерела – `<div class="source">` **всередині `Back`** | поле `Sources` |
| стабільний ID – **тег** `card::PYI_01_001` | поле `QID` (тег `qid::` лишається для пошуку) |
| системний шрифт (Segoe UI / SF / Roboto) | Literata + Golos Text + JetBrains Mono, вбудовані в `collection.media` |

Візуальна композиція збережена без змін: градієнтна смуга, білий контейнер, надпис-мітка,
великий фронт, роздільник, синій `.key`, червоний `.warn`, посилання внизу.

## Шрифти

Обрані за відгуками, з підтвердженою кирилицею (Google Fonts CSS2 віддає підмножину
`U+0301, U+0400-045F, U+0490-0491`, що покриває `і ї є ґ`).

| Роль | Шрифт | Чому саме він |
|---|---|---|
| Питання | **Literata** (OFL) | зроблений для Google Play Books; за відгуками читачів – один з найкращих екранних серифів, «тепліший і граційніший» за системні. Дає картці редакційний вигляд замість інтерфейсного |
| Текст відповіді | **Golos Text** (OFL, Paratype) | спроєктований саме під екранне читання кирилицею: висока x-height, вільний трекінг. Має **засічку на `l` і `1`**, що важливо в тексті про код |
| Код | **JetBrains Mono** (OFL) | зроблений для коду, розрізняє `0/O` і `l/1/I`, має кирилицю |

Manrope розглядався і відхилений: типографічні рецензії вказують на неоднорідні гліфи й
спотворені переходи від прямих до округлих сегментів.

### Файли в `collection.media`

Завантажити woff2 (підмножини `latin` + `cyrillic`) і покласти у `collection.media`
**з підкресленням на початку** – інакше Anki видалить їх як невикористані:

```
_literata-700.woff2
_golos-400.woff2
_golos-500.woff2
_golos-700.woff2
_jetbrains-mono-400.woff2
```

Ім'я файлу має збігатися з `src` до символу, включно з регістром.

## Front Template

```html
<div class="card-wrap">
  <div class="top-bar"></div>
  <main class="card-body">
    <div class="deck-label" id="deck-label">Interview QA</div>
    <section class="prompt">{{Front}}</section>
  </main>
</div>

<script>
(function () {
  var qid = "{{text:QID}}";
  var map = { py: "Python", cpp: "C / C++", emb: "Embedded", cs: "Computer science",
              sys: "Systems", db: "Databases", eng: "Engineering", sd: "System design",
              ds: "Data science", ml: "Machine learning", de: "Data engineering",
              be: "Backend", ops: "DevOps", qa: "QA automation", bhv: "Behavioral" };
  var el = document.getElementById("deck-label");
  var key = qid.split("-")[0];
  if (el && map[key]) { el.textContent = map[key] + " interview"; }
})();
</script>
```

Мітка виводиться з префікса `QID`. Якщо скрипт не спрацює, лишається статичний текст –
поведінка не ламається.

## Back Template

```html
<div class="card-wrap">
  <div class="top-bar"></div>
  <main class="card-body">
    <div class="deck-label" id="deck-label">Interview QA</div>
    <section class="prompt">{{Front}}</section>
    <hr id="answer" class="separator">
    <section class="answer">{{Back}}</section>
    {{#Reference}}
    <div class="learn-more"><a href="{{text:Reference}}">Розгорнуте пояснення</a></div>
    {{/Reference}}
    {{#Sources}}<div class="source">{{Sources}}</div>{{/Sources}}
  </main>
</div>

<script>
(function () {
  var qid = "{{text:QID}}";
  var map = { py: "Python", cpp: "C / C++", emb: "Embedded", cs: "Computer science",
              sys: "Systems", db: "Databases", eng: "Engineering", sd: "System design",
              ds: "Data science", ml: "Machine learning", de: "Data engineering",
              be: "Backend", ops: "DevOps", qa: "QA automation", bhv: "Behavioral" };
  var el = document.getElementById("deck-label");
  var key = qid.split("-")[0];
  if (el && map[key]) { el.textContent = map[key] + " interview"; }
})();
</script>
```

`{{#Reference}}` – умовна секція: якщо поле порожнє, блок не рендериться взагалі.
`Sources` лишається в DOM для provenance, але приховані через CSS (`.source { display: none }`),
як і раніше.

## Styling

```css
@font-face {
  font-family: "Literata";
  src: url("_literata-700.woff2") format("woff2");
  font-weight: 700;
  font-display: swap;
}
@font-face {
  font-family: "Golos Text";
  src: url("_golos-400.woff2") format("woff2");
  font-weight: 400;
  font-display: swap;
}
@font-face {
  font-family: "Golos Text";
  src: url("_golos-500.woff2") format("woff2");
  font-weight: 500;
  font-display: swap;
}
@font-face {
  font-family: "Golos Text";
  src: url("_golos-700.woff2") format("woff2");
  font-weight: 700;
  font-display: swap;
}
@font-face {
  font-family: "JetBrains Mono";
  src: url("_jetbrains-mono-400.woff2") format("woff2");
  font-weight: 400;
  font-display: swap;
}

.card {
  --page-bg: #f4f5f7;
  --surface: #ffffff;
  --text: #1c2330;
  --muted: #98a1b3;
  --line: #eceef2;
  --accent: #3776ab;
  --accent-strong: #245b88;
  --accent-soft: #eef6fc;
  --code-bg: #f7f9fc;
  --code-line: #dce4ec;
  --warning: #c43d4b;

  --font-display: "Literata", Georgia, "Times New Roman", serif;
  --font-text: "Golos Text", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
  --font-mono: "JetBrains Mono", "SFMono-Regular", "Cascadia Code", Consolas, monospace;

  margin: 0;
  padding: 0;
  background: var(--page-bg);
  color: var(--text);
  font-family: var(--font-text);
  font-size: 19px;
  line-height: 1.58;
  text-align: left;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

.card-wrap {
  box-sizing: border-box;
  max-width: 680px;
  margin: 18px auto;
  border-radius: 16px;
  background: var(--surface);
  box-shadow: 0 2px 14px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.top-bar {
  height: 8px;
  background: linear-gradient(90deg, #3776ab 0%, #5aa7d6 55%, #ffd343 100%);
}

.card-body {
  padding: 26px 34px 30px;
}

.deck-label {
  margin-bottom: 12px;
  color: var(--muted);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.prompt {
  margin: 4px 0 8px;
  font-family: var(--font-display);
  font-size: 29px;
  font-weight: 700;
  line-height: 1.28;
  letter-spacing: -0.005em;
}

.answer {
  margin: 0;
}

.separator {
  margin: 24px 0 20px;
  border: 0;
  border-top: 1px solid var(--line);
}

code {
  padding: 0.08em 0.32em;
  border: 1px solid var(--code-line);
  border-radius: 5px;
  background: var(--code-bg);
  color: var(--text);
  font-family: var(--font-mono);
  font-size: 0.86em;
  overflow-wrap: anywhere;
}

.code-block {
  margin: 14px 0;
  padding: 16px 18px;
  border: 1px solid var(--code-line);
  border-left: 4px solid var(--accent);
  border-radius: 8px;
  background: var(--code-bg);
  overflow-x: auto;
  tab-size: 4;
}

.code-block code {
  display: block;
  padding: 0;
  border: 0;
  background: transparent;
  white-space: pre;
  overflow-wrap: normal;
  font-size: 0.82em;
  line-height: 1.5;
}

.key {
  color: var(--accent-strong);
  font-weight: 700;
}

.warn {
  color: var(--warning);
  font-weight: 700;
}

.source {
  display: none;
}

.learn-more {
  margin-top: 22px;
  font-size: 0.84em;
}

.learn-more a {
  color: var(--accent-strong);
  font-weight: 700;
  text-decoration: none;
}

.nightMode.card {
  --page-bg: #15181d;
  --surface: #1e232b;
  --text: #e7ebf2;
  --muted: #778294;
  --line: #2b313b;
  --accent: #65a9dc;
  --accent-strong: #78b8e6;
  --accent-soft: #232d38;
  --code-bg: #232935;
  --code-line: #354052;
  --warning: #ff8f92;
}

.nightMode .card-wrap {
  box-shadow: none;
}

.nightMode .learn-more a {
  color: #8bc8f2;
}

.mobile .card-wrap {
  margin: 0;
  border-radius: 0;
  box-shadow: none;
}

.mobile .card-body {
  padding: 22px 18px 26px;
}

.mobile .prompt {
  font-size: 25px;
}

.mobile.card {
  font-size: 17px;
}
```

## Принципи, які зберігаються з попередньої версії

- Композиція: компактний контейнер, верхня градієнтна смуга, великий фронт, виразний
  роздільник, приглушений footer.
- Синьо-жовтий акцент пов'язує оформлення з Python, але не кодує тему, рівень чи тип картки.
- Тема й рівень не показуються до відповіді, щоб не давати контекстну підказку.
- Ширина `680px` уміщує рядок коду.
- Працює без мережі й підтримує night mode.
- Теги не виводяться: це службові дані.

## Що змінилось у типографіці

- Питання – серифом Literata замість системного sans. Це головна візуальна зміна: картка
  читається як редакційна сторінка, а не як діалог інтерфейсу.
- Кегль питання зменшено з `30px` до `29px`, `line-height` піднято з `1.25` до `1.28`:
  у Literata більші виносні елементи, і при старих значеннях рядки злипалися.
- Тіло – Golos Text, спроєктований під екранну кирилицю.
- Код – JetBrains Mono замість системного моноширинного.

## Порядок застосування

Ручних кроків у Anki немає: тип, поля, шаблон і CSS створює білдер із цього документа. Робочий
зразок – `packaging/anki/test-deck/build_test_deck.py`.

1. Покласти п'ять `woff2` у `collection.media` з підкресленням на початку – це робить пакувальник,
   складаючи `.apkg`.
2. Білдер оголошує модель `1600000000001` з п'ятьма полями і одним шаблоном, з ідентифікаторами
   з таблиці fingerprint вище.
3. Front Template, Back Template і Styling беруться звідси без змін.
4. Перевірити візуально на десктопі й один раз на телефоні. Вбудовані шрифти –
   **офіційно підтримуваний спосіб**: посібник AnkiDroid прямо відсилає до розділу
   «Installing fonts» десктопного посібника як до рекомендованого методу. Два практичні
   застереження з того ж посібника: файли мають доїхати на пристрій (якщо вимкнено
   «Fetch media on sync», їх треба скопіювати в `AnkiDroid/collection.media` вручну), і дуже
   великі шрифти можуть вичерпати пам'ять на старих пристроях – для наших `woff2`-підмножин
   `latin + cyrillic` по кілька десятків кілобайт це неактуально.
   Fallback-стек лишається як страховка, а не як очікуваний режим роботи.
5. Зафіксувати fingerprint першої збірки як базову лінію для діфів (ADR-0009 §3).

Після кроку 5 структура заморожена, і будь-яка її зміна – окрема міграція, а не побічний ефект.
