# Electronics Basic Anki Template

Use this with `Section_1_anki_cards.txt` through `Section_4_anki_cards.txt`.
The matching `.apkg` files install this note type automatically.

Import settings:
- Note type: clone `Basic` and name it `Electronics Basic`
- Fields: `Front`, `Back`
- Tags column: column 3
- HTML: enabled (`#html:true` is already in the file)
- Create the `Electronics Basic` note type before importing, or choose it manually in the import dialog.

Front Template:

```html
<div class="card-shell">
  <div class="label">Question</div>
  <div class="front">{{Front}}</div>
</div>
```

Back Template:

```html
<div class="card-shell">
  <div class="label">Question</div>
  <div class="front">{{Front}}</div>
  <hr id="answer">
  <div class="label">Answer</div>
  <div class="answer">{{Back}}</div>
</div>
```

Styling:

```css
.card {
  font-family: "Manrope", "IBM Plex Sans", "Segoe UI Variable Text", "Segoe UI", sans-serif;
  font-size: 21px;
  line-height: 1.52;
  text-align: left;
  color: black;
  background: white;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

.card-shell {
  max-width: 820px;
  margin: 0 auto;
  padding: 24px 26px;
}

.label {
  margin-bottom: 8px;
  font-family: "JetBrains Mono", "Cascadia Mono", "IBM Plex Mono", "Consolas", monospace;
  color: #555;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.front {
  font-family: "IBM Plex Sans", "Manrope", "Segoe UI Variable Display", "Segoe UI", sans-serif;
  font-size: 26px;
  line-height: 1.28;
  font-weight: 750;
  color: black;
}

.answer {
  margin-top: 16px;
  font-weight: 450;
  color: black;
}

hr {
  border: 0;
  border-top: 1px solid #ddd;
  margin: 24px 0;
}

code {
  font-family: "JetBrains Mono", "Cascadia Code", "Cascadia Mono", "IBM Plex Mono", "Consolas", monospace;
  font-size: 0.9em;
  background: #eee;
  color: black;
  padding: 2px 5px;
  border-radius: 4px;
  white-space: normal;
  overflow-wrap: anywhere;
}

.code-block {
  margin: 14px 0 4px;
  padding: 12px 14px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: #f6f8fa;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.code-block code {
  display: block;
  padding: 0;
  background: transparent;
  color: #111;
  font-size: 0.82em;
  line-height: 1.45;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
}

.code-kw {
  color: #005cc5;
  font-weight: 700;
}

.code-type {
  color: #6f42c1;
  font-weight: 700;
}

.code-fn {
  color: #22863a;
  font-weight: 700;
}

.code-num {
  color: #b31d28;
}

.code-str {
  color: #032f62;
}

.code-comment {
  color: #6a737d;
  font-style: italic;
}

.formula {
  display: inline-block;
  margin: 2px 3px;
  color: black;
  font-weight: 650;
}

.key {
  color: black;
  font-weight: 800;
}

.warn {
  color: #b00020;
  font-weight: 800;
}

.example-label {
  display: inline-block;
  margin-top: 8px;
  color: #333;
  font-weight: 700;
}

.mobile .card {
  font-size: 19px;
}

.mobile .front {
  font-size: 23px;
}

.mobile .card-shell {
  padding: 18px 14px;
}

.mobile .code-block {
  margin-top: 12px;
  padding: 10px 11px;
}

.mobile .code-block code {
  font-size: 0.76em;
}
```
