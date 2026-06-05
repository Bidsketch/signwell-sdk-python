from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest

from signwell_sdk import Embedded


class FakeDocumentApi:
    def __init__(self):
        self.created_document: Any | None = None
        self.created_template_document: Any | None = None

    def create_document(self, request):
        self.created_document = request
        return SimpleNamespace(
            recipients=[
                SimpleNamespace(email="jane@example.com", embedded_signing_url="https://www.signwell.com/docs/abc")
            ]
        )

    def create_document_from_template(self, request):
        self.created_template_document = request
        return SimpleNamespace(recipients=[])


def test_create_signing_document_builds_embedded_request():
    api = FakeDocumentApi()

    document = Embedded.create_signing_document(
        name="NDA",
        files=[{"name": "nda.pdf", "file_base64": "ZGF0YQ=="}],
        recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
        fields=[[{"x": 20, "y": 60, "page": 1, "type": "signature"}]],
        test_mode=True,
        options={"document_api": api},
    )

    created_document = api.created_document
    assert created_document is not None
    assert created_document.embedded_signing is True
    assert created_document.embedded_signing_notifications is False
    assert created_document.test_mode is True
    assert created_document.files[0].file_base64 == "ZGF0YQ=="
    assert created_document.fields[0][0].recipient_id == "1"
    assert Embedded.embedded_signing_url(document) == "https://www.signwell.com/docs/abc"
    assert Embedded.embedded_signing_urls(document) == {"jane@example.com": "https://www.signwell.com/docs/abc"}


def test_rejects_fieldless_signing_without_signature_page_or_text_tags():
    with pytest.raises(ValueError, match="with_signature_page=True"):
        Embedded.create_signing_document(
            name="NDA",
            files=[{"name": "nda.pdf", "file_base64": "ZGF0YQ=="}],
            recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
            options={"document_api": FakeDocumentApi()},
        )


def test_allows_signature_page_or_text_tags_without_fields():
    Embedded.create_signing_document(
        name="NDA",
        files=[{"name": "nda.pdf", "file_base64": "ZGF0YQ=="}],
        recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
        with_signature_page=True,
        options={"document_api": FakeDocumentApi()},
    )

    Embedded.create_signing_document(
        name="NDA",
        files=[{"name": "nda.pdf", "file_base64": "ZGF0YQ=="}],
        recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
        text_tags=True,
        options={"document_api": FakeDocumentApi()},
    )


def test_validates_file_inputs():
    with pytest.raises(ValueError, match="exactly one"):
        Embedded.create_requesting_document(
            name="NDA",
            files=[{"name": "nda.pdf", "file_url": "https://example.com/nda.pdf", "file_base64": "ZGF0YQ=="}],
            recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
            options={"document_api": FakeDocumentApi()},
        )


def test_template_selector_validation():
    with pytest.raises(ValueError, match="not both"):
        Embedded.create_signing_document_from_template(
            template_id="tmpl_1",
            template_ids=["tmpl_2"],
            recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
            options={"document_api": FakeDocumentApi()},
        )

    with pytest.raises(ValueError, match="Provide template_id or template_ids"):
        Embedded.create_signing_document_from_template(
            recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
            options={"document_api": FakeDocumentApi()},
        )


def test_iframe_helpers_validate_urls_and_handlers():
    assert Embedded.script_tag() == '<script src="https://static.signwell.com/assets/embedded.js"></script>'
    html = Embedded.signing_iframe(
        url="https://www.signwell.com/docs/abc",
        redirect_url="https://app.example.com/done",
        allowed_redirect_hosts=["app.example.com"],
        events={"completed": "App.signWell.completed"},
    )

    assert "new SignWellEmbed" in html
    assert "App.signWell.completed" in html

    with pytest.raises(ValueError, match="HTTPS"):
        Embedded.signing_iframe(url="http://www.signwell.com/docs/abc")

    with pytest.raises(ValueError, match="blocked"):
        Embedded.signing_iframe(
            url="https://www.signwell.com/docs/abc",
            events={"completed": "constructor.alert"},
        )
