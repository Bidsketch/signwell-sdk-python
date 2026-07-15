from __future__ import annotations

from types import SimpleNamespace
from typing import Any, cast

import pytest

from signwell_sdk import Embedded
from signwell_sdk.models.additional_fields_inner_inner_value import (
    AdditionalFieldsInnerInnerValue,
)
from signwell_sdk.models.field_type import FieldType
from signwell_sdk.models.fields_inner_inner import FieldsInnerInner


class FakeDocumentApi:
    def __init__(self):
        self.created_document: Any | None = None
        self.created_template_document: Any | None = None

    def create_document(self, request):
        self.created_document = request
        return SimpleNamespace(
            recipients=[
                SimpleNamespace(
                    email="jane@example.com",
                    embedded_signing_url="https://www.signwell.com/docs/abc",
                )
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
            files=[
                {
                    "name": "nda.pdf",
                    "file_url": "https://example.com/nda.pdf",
                    "file_base64": "ZGF0YQ==",
                }
            ],
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

    with pytest.raises(ValueError, match="dot-separated"):
        Embedded.signing_iframe(
            url="https://www.signwell.com/docs/abc",
            events={"completed": ""},
        )

    with pytest.raises(ValueError, match="dot-separated"):
        Embedded.signing_iframe(
            url="https://www.signwell.com/docs/abc",
            events={"completed": "  "},
        )


def test_iframe_helpers_escape_json_for_script_tag_context():
    html = Embedded.signing_iframe(
        url="https://www.signwell.com/docs/abc",
        container_id='signwell"></script><img src=x onerror=alert(1)>',
        events={"completed</script><img src=x onerror=alert(1)>": "App.signWell.completed"},
    )

    script_body = html.removeprefix("<script>\n").removesuffix("\n</script>")

    assert "</script>" not in script_body.lower()
    assert "\\u003c/script\\u003e" in html
    assert "\\u003cimg src=x onerror=alert(1)\\u003e" in html


def test_redirect_urls_require_explicit_allowed_hosts():
    with pytest.raises(ValueError, match="allowed_redirect_hosts"):
        Embedded.signing_iframe(
            url="https://www.signwell.com/docs/abc",
            redirect_url="https://app.example.com/done",
        )

    with pytest.raises(ValueError, match="Redirect URL host"):
        Embedded.requesting_iframe(
            url="https://www.signwell.com/docs/abc",
            redirect_url="https://evil.example.com/done",
            allowed_redirect_hosts=["app.example.com"],
        )

    html = Embedded.requesting_iframe(
        url="https://www.signwell.com/docs/abc",
        redirect_url="https://APP.EXAMPLE.COM/done",
        allowed_redirect_hosts=["app.example.com"],
    )

    assert "https://APP.EXAMPLE.COM/done" in html


def test_checkbox_field_values_normalize_to_api_values():
    true_checkbox = FieldsInnerInner(
        x=20,
        y=60,
        page=1,
        recipient_id="1",
        type=FieldType.CHECKBOX,
        value=AdditionalFieldsInnerInnerValue(True),
    )
    assert true_checkbox.value is not None
    assert true_checkbox.value.actual_instance == "t"
    assert true_checkbox.to_dict()["value"] == "t"

    false_checkbox = FieldsInnerInner(
        x=20,
        y=60,
        page=1,
        recipient_id="1",
        type=FieldType.CHECKBOX,
        value=AdditionalFieldsInnerInnerValue("false"),
    )
    assert false_checkbox.value is not None
    assert false_checkbox.value.actual_instance == "f"
    assert false_checkbox.to_dict()["value"] == "f"

    for raw_value, expected in [(True, "t"), (False, "f"), ("true", "t"), ("t", "t"), ("false", "f"), ("f", "f")]:
        checkbox = FieldsInnerInner(
            x=20,
            y=60,
            page=1,
            recipient_id="1",
            type=FieldType.CHECKBOX,
            value=cast(Any, raw_value),
        )
        assert checkbox.value is not None
        assert checkbox.value.actual_instance == expected
        assert checkbox.to_dict()["value"] == expected

    for raw_value in ["yes", "1"]:
        with pytest.raises(ValueError, match="Checkbox field values"):
            FieldsInnerInner(
                x=20,
                y=60,
                page=1,
                recipient_id="1",
                type=FieldType.CHECKBOX,
                value=cast(Any, raw_value),
            )

    text = FieldsInnerInner(
        x=20,
        y=60,
        page=1,
        recipient_id="1",
        type=FieldType.TEXT,
        value=AdditionalFieldsInnerInnerValue("true"),
    )
    assert text.value is not None
    assert text.value.actual_instance == "true"


def test_embedded_helper_normalizes_checkbox_field_values():
    api = FakeDocumentApi()

    Embedded.create_signing_document(
        name="Checklist",
        files=[{"name": "checklist.pdf", "file_base64": "ZGF0YQ=="}],
        recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
        fields=[[{"x": 20, "y": 60, "page": 1, "type": "checkbox", "value": "true"}]],
        test_mode=True,
        options={"document_api": api},
    )

    created_document = api.created_document
    assert created_document is not None
    checkbox = created_document.fields[0][0]
    assert checkbox.value is not None
    assert checkbox.value.actual_instance == "t"
    assert checkbox.to_dict()["value"] == "t"
