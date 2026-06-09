from __future__ import annotations

import re
from pathlib import Path

import pytest


def test_project_declares_license_files() -> None:
    pyproject = Path("pyproject.toml").read_text()

    assert 'license = "MIT"' in pyproject
    assert 'license-files = ["LICENSE"]' in pyproject
    assert Path("LICENSE").is_file()


def test_public_gitignore_excludes_local_validation_and_build_artifacts() -> None:
    gitignore = Path(".gitignore").read_text().splitlines()

    for pattern in [
        ".validation/",
        "validation_assets/",
        ".openapi-generator/",
        "dist/",
        "openapi.yaml",
        ".venv/",
        ".mypy_cache/",
        ".pytest_cache/",
        ".ruff_cache/",
    ]:
        assert pattern in gitignore


def test_generated_api_docs_use_signwell_api_key_environment_name() -> None:
    docs_path = Path("docs/DocumentApi.md")
    if not docs_path.exists():
        pytest.skip("generated API docs are not present in this checkout")

    docs = docs_path.read_text()

    assert 'os.environ["SIGNWELL_API_KEY"]' in docs
    assert 'os.environ["API_KEY"]' not in docs
    assert "import os" in docs


def test_api_client_does_not_rewrap_or_dead_raise_exceptions() -> None:
    source = Path("signwell_sdk/api_client.py").read_text()

    assert "raise e" not in source
    assert "except ApiException as e" not in source
    assert "raise ApiException.from_response" not in source


def test_generated_api_modules_do_not_duplicate_imported_symbols() -> None:
    import_pattern = re.compile(r"^from (?P<module>[\w.]+) import (?P<names>.+)$")

    for path in Path("signwell_sdk/api").glob("*_api.py"):
        imported_symbols: dict[tuple[str, str], str] = {}
        for line in path.read_text().splitlines():
            match = import_pattern.match(line)
            if not match or match.group("module") == "__future__":
                continue

            module_name = match.group("module")
            for import_name in match.group("names").split(","):
                imported_name = import_name.strip()
                local_name = imported_name.split(" as ")[-1].strip()
                key = (module_name, local_name)
                assert key not in imported_symbols, (
                    f"{path} duplicates import {local_name!r} from {module_name!r}: "
                    f"{imported_symbols[key]!r} and {line!r}"
                )
                imported_symbols[key] = line
