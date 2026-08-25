"""Build the manual-test Anki packages for the Interview QA note type.

Produces two packages so the owner can verify, by hand, on desktop and AnkiDroid:

  v1 - six cards, the full styling, embedded fonts
  v2 - the same deck with one card removed and one card edited

Run:  python packaging/anki/test-deck/build_test_deck.py
"""

from __future__ import annotations

import hashlib
import pathlib
import sys

import genanki

ROOT = pathlib.Path(__file__).resolve().parents[3]
FONTS = ROOT / "packaging" / "anki" / "fonts"
OUT = ROOT / "packaging" / "anki" / "test-deck"

# Deliberately fixed ids in the past, so Anki's own timestamp-based id generation
# can never produce them again and collide. The full set is the frozen fingerprint;
# see packaging/anki/note_type.md.
MODEL_ID = 1600000000001
DECK_ID_BASE = 1600000000100

FIELDS = [
    {"name": "Front", "ord": 0, "id": 1600000001001},
    {"name": "Back", "ord": 1, "id": 1600000001002},
    {"name": "Reference", "ord": 2, "id": 1600000001003},
    {"name": "Sources", "ord": 3, "id": 1600000001004},
    {"name": "QID", "ord": 4, "id": 1600000001005},
]
TEMPLATE_ID = 1600000001101

SITE = "https://bogdan-kovalchuk.github.io/interview-qa"
GUID_SALT = "iqa:v1:"

BASE91 = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
          "!#$%&()*+,-./:;<=>?@[]^_`{|}~")


def guid_for(qid: str) -> str:
    """Deterministic note GUID, per ADR-0006. Never change this function."""
    digest = hashlib.sha256((GUID_SALT + qid).encode("utf-8")).digest()[:8]
    n = int.from_bytes(digest, "big")
    out = []
    while n:
        n, rem = divmod(n, len(BASE91))
        out.append(BASE91[rem])
    return "".join(reversed(out)) or BASE91[0]


LABEL_JS = """
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
"""

FRONT_TMPL = """<div class="card-wrap">
  <div class="top-bar"></div>
  <main class="card-body">
    <div class="deck-label" id="deck-label">Interview QA</div>
    <section class="prompt">{{Front}}</section>
  </main>
</div>
""" + LABEL_JS

BACK_TMPL = """<div class="card-wrap">
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
""" + LABEL_JS


def font_face_css() -> str:
    """One @font-face per family/weight/subset, with the Google unicode-range."""
    import json
    faces = json.loads((FONTS / "fonts.json").read_text(encoding="utf-8"))
    out = []
    for f in faces:
        out.append(
            "@font-face {\n"
            f'  font-family: "{f["family"]}";\n'
            f'  src: url("{f["file"]}") format("woff2");\n'
            f'  font-weight: {f["weight"]};\n'
            "  font-style: normal;\n"
            "  font-display: swap;\n"
            f'  unicode-range: {f["unicode_range"]};\n'
            "}"
        )
    return "\n".join(out)


STYLING_BODY = """
.card {
  --page-bg: #f4f5f7;
  --surface: #ffffff;
  --text: #1c2330;
  --muted: #98a1b3;
  --line: #eceef2;
  --accent: #3776ab;
  --accent-strong: #245b88;
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

.top-bar { height: 8px; background: linear-gradient(90deg, #3776ab 0%, #5aa7d6 55%, #ffd343 100%); }
.card-body { padding: 26px 34px 30px; }

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

.answer { margin: 0; }
.separator { margin: 24px 0 20px; border: 0; border-top: 1px solid var(--line); }

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

.key { color: var(--accent-strong); font-weight: 700; }
.warn { color: var(--warning); font-weight: 700; }
.source { display: none; }

.learn-more { margin-top: 22px; font-size: 0.84em; }
.learn-more a { color: var(--accent-strong); font-weight: 700; text-decoration: none; }

.nightMode.card {
  --page-bg: #15181d;
  --surface: #1e232b;
  --text: #e7ebf2;
  --muted: #778294;
  --line: #2b313b;
  --accent: #65a9dc;
  --accent-strong: #78b8e6;
  --code-bg: #232935;
  --code-line: #354052;
  --warning: #ff8f92;
}

.nightMode .card-wrap { box-shadow: none; }
.nightMode .learn-more a { color: #8bc8f2; }

.mobile .card-wrap { margin: 0; border-radius: 0; box-shadow: none; }
.mobile .card-body { padding: 22px 18px 26px; }
.mobile .prompt { font-size: 25px; }
.mobile.card { font-size: 17px; }
"""


def make_model() -> genanki.Model:
    return genanki.Model(
        MODEL_ID,
        "Interview QA Basic",
        fields=[dict(field) for field in FIELDS],
        templates=[{"name": "Card 1", "ord": 0, "id": TEMPLATE_ID,
                    "qfmt": FRONT_TMPL, "afmt": BACK_TMPL}],
        css=font_face_css() + "\n" + STYLING_BODY,
    )


def src(title: str, url: str) -> str:
    return f'Джерело: <a href="{url}">{title}</a>'


# qid, deck, front, back, sources
CARDS = [
    (
        "py-fund-0001", "Python::Fundamentals",
        "Яку проблему вирішує кешований файл <code>.pyc</code> і чому його наявність "
        "не означає компіляцію Python-коду в native machine code?",
        '<span class="key"><code>.pyc</code> дозволяє повторно використати скомпільований '
        "bytecode незміненого імпортованого модуля й не витрачати час на повторну компіляцію "
        "source code.</span> Він містить bytecode для Python VM, а не інструкції процесора. "
        "Формат bytecode є деталлю реалізації CPython і може змінюватися між версіями.",
        src("Python 3.14: import system", "https://docs.python.org/3.14/reference/import.html"),
    ),
    (
        "py-gil-0001", "Python::Concurrency and GIL",
        "Чому <code>threading</code> не пришвидшує CPU-bound обчислення у CPython зі "
        "ввімкненим GIL?",
        '<span class="key">GIL дозволяє виконувати bytecode лише одному потоку одночасно, '
        "тому CPU-bound робота не паралелиться між ядрами.</span> Потоки все одно корисні для "
        'I/O-bound задач, бо GIL відпускається на час очікування. <span class="warn">Типова '
        "помилка: додати потоки й очікувати прискорення обчислень.</span>",
        src("Python 3.14: GIL", "https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock"),
    ),
    (
        "py-async-0001", "Python::Asyncio",
        "Чому блокуючий виклик підвішує весь event loop asyncio?",
        '<span class="key">Event loop працює в одному потоці й передає керування лише на '
        "<code>await</code>.</span> Блокуючий виклик не віддає керування, тому всі інші задачі "
        "чекають на його завершення."
        '<pre class="code-block"><code>async def bad():\n'
        "    time.sleep(2)          # блокує loop на 2 секунди\n\n"
        "async def good():\n"
        "    await asyncio.to_thread(time.sleep, 2)</code></pre>",
        src("Python 3.14: Developing with asyncio",
            "https://docs.python.org/3.14/library/asyncio-dev.html"),
    ),
    (
        "cpp-mem-0001", "C++::Memory",
        "Чому <code>std::vector</code> інвалідує ітератори при <code>push_back</code>?",
        '<span class="key"><code>push_back</code> може перевищити <code>capacity</code> і '
        "перевиділити буфер, перемістивши елементи за новою адресою.</span> Тоді всі ітератори, "
        "вказівники та посилання на елементи стають недійсними. Якщо перевиділення не сталося, "
        "недійсним стає лише <code>end()</code>.",
        src("cppreference: std::vector::push_back",
            "https://en.cppreference.com/w/cpp/container/vector/push_back"),
    ),
    (
        "emb-rtos-0001", "Embedded::RTOS",
        "Що таке priority inversion і чим її лікує priority inheritance?",
        '<span class="key">Низькопріоритетна задача тримає м\'ютекс, потрібний '
        "високопріоритетній, і середньопріоритетна задача витісняє її, через що високопріоритетна "
        'чекає невизначено довго.</span> Priority inheritance тимчасово піднімає пріоритет '
        "власника м'ютекса до пріоритету того, хто чекає. "
        '<span class="warn">Саме ця помилка спричинила збої Mars Pathfinder у 1997.</span>',
        src("FreeRTOS: Mutexes and priority inheritance",
            "https://www.freertos.org/Real-time-embedded-RTOS-mutexes.html"),
    ),
    (
        "py-test-0001", "Python::Testing",
        "ТЕСТОВА КАРТКА ДЛЯ ВИДАЛЕННЯ — чим <code>fixture</code> у pytest відрізняється "
        "від <code>setUp</code> в unittest?",
        '<span class="key">Ця картка існує лише для перевірки видалення.</span> Видаліть її в '
        "Anki, потім імпортуйте пакет v2 і переконайтесь, що вона не повернулась, а прогрес на "
        'решті карток лишився. <span class="warn">Її QID: py-test-0001</span>',
        src("pytest: fixtures", "https://docs.pytest.org/en/stable/explanation/fixtures.html"),
    ),
]

# In v2 this card gets edited text, to prove an edit keeps the schedule.
EDITED = {
    "py-gil-0001": (
        "ВІДРЕДАГОВАНО У v2. Чому <code>threading</code> не пришвидшує CPU-bound обчислення "
        "у CPython зі ввімкненим GIL?",
        '<span class="key">ВІДРЕДАГОВАНО У v2. GIL дозволяє виконувати bytecode лише одному '
        "потоку одночасно, тому CPU-bound робота не паралелиться між ядрами.</span> "
        "Якщо ви бачите цей текст і інтервал повторення не скинувся — правка вмісту безпечна.",
    ),
}


def build(name: str, qids: list[str], edits: dict) -> pathlib.Path:
    model = make_model()
    decks: dict[str, genanki.Deck] = {}
    for i, (qid, deck_name, front, back, sources) in enumerate(CARDS):
        if qid not in qids:
            continue
        if qid in edits:
            front, back = edits[qid]
        full = f"Interview QA Test::{deck_name}"
        if full not in decks:
            decks[full] = genanki.Deck(DECK_ID_BASE + len(decks), full)
        track = qid.split("-")[0]
        decks[full].add_note(genanki.Note(
            model=model,
            fields=[front, back, f"{SITE}/uk/q/{qid}/", sources, qid],
            tags=[f"qid::{qid}", f"topic::{track}", "level::middle", "iqa::test"],
            guid=guid_for(qid),
        ))
    pkg = genanki.Package(list(decks.values()))
    pkg.media_files = [str(p) for p in sorted(FONTS.glob("_iqa-*.woff2"))]
    path = OUT / name
    pkg.write_to_file(str(path))
    return path


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    all_qids = [c[0] for c in CARDS]
    v1 = build("Interview QA Test v1.apkg", all_qids, {})
    v2_qids = [q for q in all_qids if q != "py-test-0001"]
    v2 = build("Interview QA Test v2.apkg", v2_qids, EDITED)
    for p, n in ((v1, len(all_qids)), (v2, len(v2_qids))):
        print(f"{p.name:32s} {p.stat().st_size:8d} B  {n} notes")
    print("\nGUIDs:")
    for qid in all_qids:
        print(f"  {qid:16s} {guid_for(qid)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
