from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import parse_qs, urlparse

import pytest
from pydantic import ValidationError

import signwell_sdk
from signwell_sdk.api.bulk_send_api import BulkSendApi
from signwell_sdk.api.document_api import DocumentApi
from signwell_sdk.api.template_api import TemplateApi
from signwell_sdk.api.regional_api import RegionalApi
from signwell_sdk.models.bulk_send_csv_template_response import (
    BulkSendCsvTemplateResponse,
)
from signwell_sdk.models.completed_pdf_url_response import CompletedPdfUrlResponse
from signwell_sdk.models.nom151_certificate_response import Nom151CertificateResponse
from signwell_sdk.models.nom151_url_response import Nom151UrlResponse
from signwell_sdk.models.update_document_and_send_request import (
    UpdateDocumentAndSendRequest,
)


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

    def call_api(
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ):
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


def api_client_with_responses(responses):
    configuration = signwell_sdk.Configuration(api_key={"api_key": "test_key"})
    api_client = cast(Any, signwell_sdk.ApiClient(configuration))
    calls: list[dict[str, Any]] = []
    response_iter = iter(responses)

    def call_api(
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ):
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
        return next(response_iter)

    api_client.call_api = call_api
    return cast(signwell_sdk.ApiClient, api_client), calls


def url_query(url: str) -> dict[str, list[str]]:
    return parse_qs(urlparse(url).query)


def document_payload(document_id: str, *, status: str | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "test_mode": True,
        "id": document_id,
    }
    if status is not None:
        payload["status"] = status
    return payload


def test_bulk_send_csv_template_defaults_to_binary_mode():
    api_client, calls = api_client_with_response(
        FakeRestResponse(
            body=b"name,email\nJane,jane@example.com\n",
            headers={"Content-Type": "text/csv"},
        )
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

    result = cast(
        CompletedPdfUrlResponse,
        DocumentApi(api_client).get_completed_pdf("doc_123", url_only=True),
    )

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
    result_url = cast(
        Nom151UrlResponse,
        RegionalApi(api_client).get_nom151_certificate("doc_123", url_only=True),
    )
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
        FakeRestResponse(
            body=json.dumps(certificate).encode(),
            headers={"Content-Type": "application/json"},
        )
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
        FakeRestResponse(
            status=403,
            reason="Forbidden",
            body=json.dumps({"message": "Forbidden"}).encode(),
            headers={"Content-Type": "application/json"},
        )
    )
    with pytest.raises(signwell_sdk.Errors.PermissionDeniedError) as permission_exc_info:
        DocumentApi(api_client).get_document("forbidden")
    assert permission_exc_info.value.status == 403
    assert isinstance(permission_exc_info.value, signwell_sdk.ForbiddenError)

    api_client, _calls = api_client_with_response(
        FakeRestResponse(
            status=429,
            reason="Too Many Requests",
            body=json.dumps({"error": "Rate limited"}).encode(),
            headers={
                "x-ratelimit-limit": "100",
                "x-ratelimit-remaining": "0",
                "x-ratelimit-reset": "1893456000",
                "retry-after": "30",
            },
        )
    )
    with pytest.raises(signwell_sdk.Errors.RateLimitError) as rate_limit_exc_info:
        DocumentApi(api_client).get_document("limited")
    rate_limit = rate_limit_exc_info.value.rate_limit
    assert rate_limit is not None
    assert rate_limit.limit == 100
    assert rate_limit.remaining == 0
    assert rate_limit.reset == 1893456000
    assert rate_limit.retry_after == 30

    api_client, _calls = api_client_with_response(
        FakeRestResponse(body=b"plain text", headers={"Content-Type": "text/plain"})
    )
    with pytest.raises(signwell_sdk.Errors.UnsupportedContentTypeError):
        DocumentApi(api_client).get_document("doc_123")


def test_document_api_validates_required_path_and_limit_before_request():
    api_client, calls = api_client_with_response(FakeRestResponse())
    api = DocumentApi(api_client)

    with pytest.raises(ValidationError):
        api.get_document("")
    with pytest.raises(ValidationError):
        api.list_documents(limit=51)

    assert calls == []


def test_list_documents_serializes_raw_query_filter():
    api_client, calls = api_client_with_response(FakeRestResponse())

    DocumentApi(api_client).list_documents_without_preload_content(
        query="name:Classic AND status:completed",
        page=2,
        limit=25,
    )

    params = url_query(calls[0]["url"])
    assert params["query"] == ["name:Classic AND status:completed"]
    assert params["page"] == ["2"]
    assert params["limit"] == ["25"]


def test_list_templates_serializes_raw_query_filter():
    api_client, calls = api_client_with_response(FakeRestResponse())

    TemplateApi(api_client).list_templates_without_preload_content(
        query="name:Classic AND status:Available",
        page=3,
        limit=10,
    )

    params = url_query(calls[0]["url"])
    assert params["query"] == ["name:Classic AND status:Available"]
    assert params["page"] == ["3"]
    assert params["limit"] == ["10"]


def test_document_and_template_pagination_iterators_yield_pages_and_items():
    api_client, calls = api_client_with_responses(
        [
            FakeRestResponse(
                body=json.dumps(
                    {
                        "documents": [document_payload("doc_1")],
                        "current_page": 1,
                        "next_page": 2,
                        "total_count": 2,
                        "total_pages": 2,
                    }
                ).encode(),
                headers={"Content-Type": "application/json"},
            ),
            FakeRestResponse(
                body=json.dumps(
                    {
                        "documents": [document_payload("doc_2")],
                        "current_page": 2,
                        "next_page": None,
                        "total_count": 2,
                        "total_pages": 2,
                    }
                ).encode(),
                headers={"Content-Type": "application/json"},
            ),
            FakeRestResponse(
                body=json.dumps(
                    {
                        "documents": [document_payload("doc_1")],
                        "current_page": 1,
                        "next_page": 2,
                        "total_count": 2,
                        "total_pages": 2,
                    }
                ).encode(),
                headers={"Content-Type": "application/json"},
            ),
            FakeRestResponse(
                body=json.dumps(
                    {
                        "documents": [document_payload("doc_2")],
                        "current_page": 2,
                        "next_page": None,
                        "total_count": 2,
                        "total_pages": 2,
                    }
                ).encode(),
                headers={"Content-Type": "application/json"},
            ),
        ]
    )
    documents = DocumentApi(api_client)

    pages = list(documents.iterate_document_pages(query="status:Completed"))
    items = list(documents.iterate_documents(query="status:Completed"))

    assert [page.current_page for page in pages] == [1, 2]
    assert [item.id for item in items] == ["doc_1", "doc_2"]
    assert [url_query(call["url"])["page"][0] for call in calls] == ["1", "2", "1", "2"]

    api_client, _calls = api_client_with_responses(
        [
            FakeRestResponse(
                body=json.dumps(
                    {
                        "templates": [{"id": "tpl_1"}],
                        "current_page": 1,
                        "next_page": 2,
                        "total_count": 2,
                        "total_pages": 2,
                    }
                ).encode(),
                headers={"Content-Type": "application/json"},
            ),
            FakeRestResponse(
                body=json.dumps(
                    {
                        "templates": [{"id": "tpl_2"}],
                        "current_page": 2,
                        "next_page": None,
                        "total_count": 2,
                        "total_pages": 2,
                    }
                ).encode(),
                headers={"Content-Type": "application/json"},
            ),
        ]
    )

    template_items = list(TemplateApi(api_client).iterate_templates(query="name:NDA"))
    assert [item.id for item in template_items] == ["tpl_1", "tpl_2"]


def test_update_document_alias_uses_send_document_operation():
    api_client, calls = api_client_with_response(
        FakeRestResponse(
            status=201,
            body=json.dumps(document_payload("doc_123")).encode(),
            headers={"Content-Type": "application/json"},
        )
    )

    result = DocumentApi(api_client).update_document(
        "doc_123",
        UpdateDocumentAndSendRequest(subject="Updated"),
    )

    assert result.id == "doc_123"
    assert calls[0]["url"].endswith("/api/v1/documents/doc_123/send")


def test_wait_for_completion_returns_terminal_document_and_times_out():
    from signwell_sdk.api.document_api import WaitForCompletionTimeoutError

    api_client, _calls = api_client_with_responses(
        [
            FakeRestResponse(
                body=json.dumps(document_payload("doc_123", status="In Progress")).encode(),
                headers={"Content-Type": "application/json"},
            ),
            FakeRestResponse(
                body=json.dumps(document_payload("doc_123", status="Completed")).encode(),
                headers={"Content-Type": "application/json"},
            ),
        ]
    )

    result = DocumentApi(api_client).wait_for_completion("doc_123", interval=0, max_attempts=3)
    assert result.status == "Completed"

    api_client, _calls = api_client_with_response(
        FakeRestResponse(
            body=json.dumps(document_payload("doc_123", status="In Progress")).encode(),
            headers={"Content-Type": "application/json"},
        )
    )
    with pytest.raises(WaitForCompletionTimeoutError) as exc_info:
        DocumentApi(api_client).wait_for_completion("doc_123", interval=0, max_attempts=1)
    assert exc_info.value.last_document is not None
