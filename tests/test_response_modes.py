from __future__ import annotations

import json
from typing import Any, cast

import pytest

import signwell_sdk
from signwell_sdk.api.bulk_send_api import BulkSendApi
from signwell_sdk.api.document_api import DocumentApi
from signwell_sdk.api.regional_api import RegionalApi
from signwell_sdk.models.bulk_send_csv_template_response import BulkSendCsvTemplateResponse
from signwell_sdk.models.completed_pdf_url_response import CompletedPdfUrlResponse
from signwell_sdk.models.nom151_certificate_response import Nom151CertificateResponse
from signwell_sdk.models.nom151_url_response import Nom151UrlResponse


class FakeRestResponse:
    def __init__(self, *, status=200, body=b"", headers=None, reason="OK"):
        self.status = status
        self.reason = reason
        self._body = body
        self.data = None
        self.headers = headers or {}
        self.response = self

    def read(self):
        self.data = self._body
        return self.data

    def getheader(self, name, default=None):
        for key, value in self.headers.items():
            if key.lower() == name.lower():
                return value
        return default

    def getheaders(self):
        return self.headers


def api_client_with_response(response):
    configuration = signwell_sdk.Configuration(api_key={"api_key": "test_key"})
    api_client = cast(Any, signwell_sdk.ApiClient(configuration))
    calls: list[dict[str, Any]] = []

    def call_api(method, url, header_params=None, body=None, post_params=None, _request_timeout=None):
        calls.append(
            {
                "method": method,
                "url": url,
                "headers": header_params or {},
                "body": body,
                "post_params": post_params,
                "timeout": _request_timeout,
            }
        )
        return response

    api_client.call_api = call_api
    return cast(signwell_sdk.ApiClient, api_client), calls


def test_bulk_send_csv_template_defaults_to_binary_mode():
    api_client, calls = api_client_with_response(
        FakeRestResponse(body=b"name,email\nJane,jane@example.com\n", headers={"Content-Type": "text/csv"})
    )

    result = cast(
        bytes,
        BulkSendApi(api_client).get_bulk_send_csv_template(["00000000-0000-0000-0000-000000000000"]),
    )

    assert result.startswith(b"name,email")
    assert calls[0]["headers"]["Accept"] == "application/octet-stream"


def test_bulk_send_csv_template_uses_json_for_base64_mode():
    api_client, calls = api_client_with_response(
        FakeRestResponse(
            body=json.dumps({"data": "ZGF0YQ=="}).encode(),
            headers={"Content-Type": "application/json"},
        )
    )

    result = cast(
        BulkSendCsvTemplateResponse,
        BulkSendApi(api_client).get_bulk_send_csv_template(
            ["00000000-0000-0000-0000-000000000000"],
            var_base64=True,
        ),
    )

    assert result.data == "ZGF0YQ=="
    assert calls[0]["headers"]["Accept"] == "application/json"


def test_completed_pdf_defaults_to_binary_mode():
    api_client, calls = api_client_with_response(
        FakeRestResponse(body=b"%PDF-1.7\n", headers={"Content-Type": "application/pdf"})
    )

    result = cast(bytes, DocumentApi(api_client).get_completed_pdf("doc_123"))

    assert result == b"%PDF-1.7\n"
    assert calls[0]["headers"]["Accept"] == "application/octet-stream"


def test_completed_pdf_uses_json_for_url_mode():
    api_client, calls = api_client_with_response(
        FakeRestResponse(
            body=json.dumps({"file_url": "https://example.com/signed.pdf"}).encode(),
            headers={"Content-Type": "application/json"},
        )
    )

    result = cast(CompletedPdfUrlResponse, DocumentApi(api_client).get_completed_pdf("doc_123", url_only=True))

    assert result.file_url == "https://example.com/signed.pdf"
    assert calls[0]["headers"]["Accept"] == "application/json"


def test_nom151_response_modes_and_conflict_validation():
    api_client, calls = api_client_with_response(
        FakeRestResponse(body=b"zip-data", headers={"Content-Type": "application/zip"})
    )
    result_bytes = cast(bytes, RegionalApi(api_client).get_nom151_certificate("doc_123"))

    assert result_bytes == b"zip-data"
    assert calls[0]["headers"]["Accept"] == "application/octet-stream"

    api_client, calls = api_client_with_response(
        FakeRestResponse(
            body=json.dumps({"file_url": "https://example.com/nom151.zip"}).encode(),
            headers={"Content-Type": "application/json"},
        )
    )
    result_url = cast(Nom151UrlResponse, RegionalApi(api_client).get_nom151_certificate("doc_123", url_only=True))
    assert result_url.file_url == "https://example.com/nom151.zip"
    assert calls[0]["headers"]["Accept"] == "application/json"

    certificate = {
        "nom151": {
            "status": "issued",
            "transactionId": "txn_123",
            "hash": "sha256:abc123",
            "folio": "folio_123",
            "issuedAt": "2026-01-01T00:00:00Z",
            "provider": "nom151",
            "validationUrl": "https://example.com/validate",
            "constancia": "base64-constancia",
        }
    }
    api_client, calls = api_client_with_response(
        FakeRestResponse(body=json.dumps(certificate).encode(), headers={"Content-Type": "application/json"})
    )
    result_certificate = cast(
        Nom151CertificateResponse,
        RegionalApi(api_client).get_nom151_certificate("doc_123", object_only=True),
    )
    assert result_certificate.nom151.status == "issued"
    assert calls[0]["headers"]["Accept"] == "application/json"

    with pytest.raises(ValueError, match="url_only and object_only"):
        RegionalApi(api_client).get_nom151_certificate("doc_123", url_only=True, object_only=True)


def test_status_and_content_type_errors_are_typed():
    api_client, _calls = api_client_with_response(
        FakeRestResponse(
            status=404,
            reason="Not Found",
            body=json.dumps({"message": "Not found"}).encode(),
            headers={"Content-Type": "application/json"},
        )
    )

    with pytest.raises(signwell_sdk.Errors.NotFoundError) as exc_info:
        DocumentApi(api_client).get_document("missing")
    assert exc_info.value.status == 404
    assert exc_info.value.data.message == "Not found"

    api_client, _calls = api_client_with_response(
        FakeRestResponse(body=b"plain text", headers={"Content-Type": "text/plain"})
    )
    with pytest.raises(signwell_sdk.Errors.UnsupportedContentTypeError):
        DocumentApi(api_client).get_document("doc_123")
