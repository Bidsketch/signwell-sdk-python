from __future__ import annotations

from pathlib import Path


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
    docs = Path("docs/DocumentApi.md").read_text()

    assert 'os.environ["SIGNWELL_API_KEY"]' in docs
    assert 'os.environ["API_KEY"]' not in docs
    assert "import os" in docs
