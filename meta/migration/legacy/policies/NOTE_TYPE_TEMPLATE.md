# Anki note type: Python Interview Basic

## Створення

1. В Anki відкрити `Tools → Manage Note Types`.
2. Клонувати `Basic`.
3. Назвати тип `Python Interview Basic`.
4. Залишити рівно два поля в такому порядку: `Front`, `Back`.
5. Вставити наведені нижче Front Template, Back Template і Styling.

Такий тип сумісний з усіма TSV у цьому проєкті.

## Front Template

```html
<div class="card-wrap">
  <div class="top-bar"></div>
  <main class="card-body">
    <div class="deck-label">Python interview</div>
    <section class="prompt">{{Front}}</section>
  </main>
</div>
```

## Back Template

```html
<div class="card-wrap">
  <div class="top-bar"></div>
  <main class="card-body">
    <div class="deck-label">Python interview</div>
    <section class="prompt">{{Front}}</section>
    <hr id="answer" class="separator">
    <section class="answer">{{Back}}</section>
    <div class="learn-more"><a href="https://example.com/python-interview-details">Розгорнуте пояснення</a></div>
  </main>
</div>
```

## Styling

```css
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
  margin: 0;
  padding: 0;
  background: var(--page-bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
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
  font-size: 30px;
  font-weight: 700;
  line-height: 1.25;
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
  font-family: "SFMono-Regular", "Cascadia Code", "JetBrains Mono", Consolas, monospace;
  font-size: 0.88em;
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
  font-size: 0.84em;
  line-height: 1.5;
}

.key {
  color: var(--accent-strong);
  font-weight: 750;
}

.warn {
  color: var(--warning);
  font-weight: 750;
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

## Принцип дизайну

- Композицію адаптовано з колоди `Extra Spanish`: компактний контейнер, верхня градієнтна
  смуга, великий фронт, виразний роздільник і приглушений footer.
- Синьо-жовтий акцент пов’язує оформлення з Python, але не кодує тему, рівень чи тип картки.
- Тема й рівень не показуються до відповіді, щоб не давати контекстну підказку.
- Максимальну ширину збільшено від мовного зразка до `680px`, щоб уміщувати Python-код.
- Код має моноширинний шрифт, зберігає відступи й прокручується горизонтально.
- CSS працює без зовнішніх шрифтів і підтримує Anki night mode.
- Посилання на джерело з даних картки зберігається для provenance, але не показується
  користувачу; шаблон приховує блок `.source`.
- Після відповіді виводиться одне посилання-заглушка «Розгорнуте пояснення». Адресу
  `https://example.com/python-interview-details` потрібно замінити URL майбутнього сайту.
- Теги не виводяться: це службові дані для пошуку, фільтрації, валідації та стабільних ID.
