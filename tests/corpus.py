"""The size of the real corpus, declared once.

Seven assertions across four test files used to carry these numbers as
literals. They are a tripwire worth keeping - a build that silently loses or
gains questions should fail - but repeating the same number in seven places
made every content import edit seven assertions in four files, which is the
"two live descriptions of one behaviour" AGENTS.md warns about.

Update these four numbers when the corpus grows, and the whole suite follows.
`python -m iqa validate` prints FILES and QUESTIONS; `python anki/build.py
--language {uk,en}` prints the card counts.
"""

# Every Markdown file under content/, both languages.
FILES = 2508

# Questions, counted once rather than once per language.
QUESTIONS = 1254

# Cards that ship in each package: a question ships when its Short answer is
# written in that language and `anki.export` is not false (meta/anki.md).
UK_CARDS = 1241
EN_CARDS = 998
