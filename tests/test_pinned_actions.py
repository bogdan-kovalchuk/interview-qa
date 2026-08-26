from __future__ import annotations

from pathlib import Path

from iqa.__main__ import main as iqa_main
from iqa.pinned_actions import find_violations, main


ROOT = Path(__file__).resolve().parents[1]


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def test_real_workflows_have_no_violations() -> None:
    # The actual workflows this repository ships. If this starts failing, an
    # action was added or re-pinned to something other than a commit SHA.
    violations = find_violations(ROOT / ".github" / "workflows")
    assert violations == [], "\n".join(str(v) for v in violations)


def test_real_workflows_directory_is_not_empty() -> None:
    # A guard against the check silently passing because the directory does
    # not exist or has no workflow files - `find_violations` returns an empty
    # list in both cases, which would otherwise look identical to "all pinned".
    workflows_dir = ROOT / ".github" / "workflows"
    assert workflows_dir.is_dir()
    assert list(workflows_dir.glob("*.yml")), "expected at least one workflow file"


def test_tag_pin_is_a_violation(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    _write(
        workflows / "bad.yml",
        """\
name: bad
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
""",
    )
    violations = find_violations(workflows)
    assert len(violations) == 1
    assert "actions/checkout@v4" in violations[0].uses or violations[0].uses == "actions/checkout@v4"
    assert "not a 40-hex commit SHA" in violations[0].reason


def test_branch_pin_is_a_violation(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    _write(
        workflows / "bad.yml",
        """\
name: bad
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
""",
    )
    violations = find_violations(workflows)
    assert len(violations) == 1


def test_missing_ref_is_a_violation(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    _write(
        workflows / "bad.yml",
        """\
name: bad
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout
""",
    )
    violations = find_violations(workflows)
    assert len(violations) == 1
    assert "no `@ref`" in violations[0].reason


def test_sha_pin_passes(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    _write(
        workflows / "good.yml",
        """\
name: good
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
""",
    )
    assert find_violations(workflows) == []


def test_local_action_reference_is_not_flagged(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    _write(
        workflows / "good.yml",
        """\
name: good
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: ./.github/actions/local-thing
""",
    )
    assert find_violations(workflows) == []


def test_invalid_yaml_is_a_violation(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    _write(workflows / "broken.yml", "name: [unterminated\n")
    violations = find_violations(workflows)
    assert len(violations) == 1
    assert "not valid YAML" in violations[0].reason


def test_missing_workflows_directory_has_no_violations(tmp_path: Path) -> None:
    assert find_violations(tmp_path / "does-not-exist") == []


def test_cli_exits_nonzero_on_violations(tmp_path: Path, capsys) -> None:
    workflows = tmp_path / ".github" / "workflows"
    _write(
        workflows / "bad.yml",
        """\
name: bad
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
""",
    )
    exit_code = main(["--workflows", str(workflows)])
    assert exit_code == 1
    captured = capsys.readouterr()
    assert "FAIL [pinned-actions]" in captured.out


def test_module_cli_check_pinned_actions_command_exists() -> None:
    # `python -m iqa check-pinned-actions` (no --workflows) must resolve against
    # the real .github/workflows/ using the process's own working directory -
    # this is what CI actually invokes.
    import os

    previous_cwd = Path.cwd()
    try:
        os.chdir(ROOT)
        assert iqa_main(["check-pinned-actions"]) == 0
    finally:
        os.chdir(previous_cwd)


def test_cli_exits_zero_when_clean(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    _write(
        workflows / "good.yml",
        """\
name: good
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
""",
    )
    assert main(["--workflows", str(workflows)]) == 0
