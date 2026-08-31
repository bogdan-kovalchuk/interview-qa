"""Build the manual-test Anki packages, and serve as the reference deck builder.

The real builder (packaging/anki/build.py) does not exist yet; this script is the
worked example of how to assemble a package: it reads the note type from
packaging/anki/notetype/, derives GUIDs from question ids, and embeds the font
subsets from packaging/anki/fonts/.

Produces two packages for hand-verification on desktop and AnkiDroid:

  v1 - six cards, full styling, embedded fonts
  v2 - the same deck with one card removed and one card edited

The procedure: import v1, study a few cards so they have a real interval, delete
py-test-0001, then import v2 and confirm three things - the deleted card did not
come back, the intervals did not reset, and the edited card shows the new text.
That run was done on 2026-09-03 and all three held; see meta/measurements.md.
The deck root is `Interview QA Test`, separate from the real deck, so it can be
deleted whole afterwards. Keep the fonts in collection.media - they are reused.

Run:  python packaging/anki/test-deck/build_test_deck.py
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys

import genanki

ROOT = pathlib.Path(__file__).resolve().parents[3]
FONTS = ROOT / "packaging" / "anki" / "fonts"
OUT = ROOT / "packaging" / "anki" / "test-deck"

# The note type lives in packaging/anki/notetype/ and nowhere else: ids in fingerprint.json,
# markup in front.html / back.html, styling in card.css. Ids are deliberately taken from the
# past so Anki's timestamp-based generation can never produce them again and collide.
NOTETYPE = ROOT / "packaging" / "anki" / "notetype"
FINGERPRINT = json.loads((NOTETYPE / "fingerprint.json").read_text(encoding="utf-8"))
MODEL_ID = FINGERPRINT["model_id"]
DECK_ID_BASE = 1600000000100

SITE = "https://bogdan-kovalchuk.github.io/interview-qa"
GUID_SALT = "iqa:v1:"

BASE91 = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
          "!#$%&()*+,-./:;<=>?@[]^_`{|}~")


def guid_for(qid: str) -> str:
    """Deterministic note GUID. Never change this function."""
    digest = hashlib.sha256((GUID_SALT + qid).encode("utf-8")).digest()[:8]
    n = int.from_bytes(digest, "big")
    out = []
    while n:
        n, rem = divmod(n, len(BASE91))
        out.append(BASE91[rem])
    return "".join(reversed(out)) or BASE91[0]


def font_face_css() -> str:
    """One @font-face per family/weight/subset, with the Google unicode-range."""
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


def make_model() -> genanki.Model:
    read = lambda name: (NOTETYPE / name).read_text(encoding="utf-8")
    return genanki.Model(
        MODEL_ID,
        FINGERPRINT["model_name"],
        fields=[dict(field) for field in FINGERPRINT["fields"]],
        templates=[dict(FINGERPRINT["templates"][0],
                        qfmt=read("front.html"), afmt=read("back.html"))],
        css=font_face_css() + "\n" + read("card.css"),
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
