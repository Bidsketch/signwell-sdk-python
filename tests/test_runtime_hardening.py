from __future__ import annotations

import http.client as httplib
import logging
import os
from pathlib import Path
from typing import Any, NoReturn, cast, get_type_hints

import pytest

import signwell_sdk
from signwell_sdk import rest


class FakeRestResponse:
    def __init__(
        self,
        *,
        status: int = 200,
        body: bytes | None = b"",
        headers: dict[str, str] | None = None,
        reason: str = "OK",
    ) -> None:
        self.status = status
        self.reason = reason
        self.data = body
        self.headers = headers or {}
        self.response = self

    def getheader(self, name: str, default: Any = None) -> Any:
        for key, value in self.headers.items():
            if key.lower() == name.lower():
                return value
        return default

    def getheaders(self) -> dict[str, str]:
        return self.headers


class FakePoolManager:
    def __init__(self) -> None:
        self.cleared = False

    def clear(self) -> None:
        self.cleared = True


@pytest.mark.parametrize(
    "content_disposition",
    [
        'attachment; filename="../../evil.pdf"',
        'attachment; filename="subdir\\\\evil.pdf"',
        'attachment; filename="my document.pdf"',
        "attachment; filename*=UTF-8''my%20doc.pdf",
    ],
)
def test_file_downloads_stay_confined_to_temp_dir(tmp_path: Path, content_disposition: str) -> None:
    configuration = cast(Any, signwell_sdk.Configuration())
    configuration.temp_folder_path = str(tmp_path)
    api_client = signwell_sdk.ApiClient(configuration)
    response = FakeRestResponse(
        body=b"download-data",
        headers={"Content-Disposition": content_disposition},
    )

    result = api_client.response_deserialize(cast(rest.RESTResponse, response), {"200": "file"}).data

    assert isinstance(result, str)
    result_path = Path(result).resolve()
    assert result_path.parent == tmp_path.resolve()
    assert result_path.read_bytes() == b"download-data"
    assert ".." not in result_path.name
    assert os.sep not in result_path.name


def test_content_disposition_filename_supports_spaces_and_rfc6266_filename_star(tmp_path: Path) -> None:
    configuration = cast(Any, signwell_sdk.Configuration())
    configuration.temp_folder_path = str(tmp_path)
    api_client = signwell_sdk.ApiClient(configuration)

    spaced_response = FakeRestResponse(
        body=b"download-data",
        headers={"Content-Disposition": 'attachment; filename="my document.pdf"'},
    )
    encoded_response = FakeRestResponse(
        body=b"download-data",
        headers={"Content-Disposition": "attachment; filename*=UTF-8''signed%20copy.pdf"},
    )

    spaced_path = Path(api_client.response_deserialize(cast(rest.RESTResponse, spaced_response), {"200": "file"}).data)
    encoded_path = Path(
        api_client.response_deserialize(cast(rest.RESTResponse, encoded_response), {"200": "file"}).data
    )

    assert spaced_path.name.startswith("my_document-")
    assert spaced_path.name.endswith(".pdf")
    assert encoded_path.name.startswith("signed_copy-")
    assert encoded_path.name.endswith(".pdf")


def test_unread_response_data_raises_sdk_value_error() -> None:
    api_client = signwell_sdk.ApiClient(signwell_sdk.Configuration())
    response = FakeRestResponse(body=None)

    with pytest.raises(signwell_sdk.ApiValueError, match="RESTResponse.read"):
        api_client.response_deserialize(cast(rest.RESTResponse, response), {"200": "str"})


def test_error_response_deserialization_errors_are_not_replaced_by_status_errors() -> None:
    api_client = signwell_sdk.ApiClient(signwell_sdk.Configuration())
    response = FakeRestResponse(
        status=400,
        reason="Bad Request",
        body=b"not-json",
        headers={"content-type": "application/octet-stream"},
    )

    with pytest.raises(signwell_sdk.UnsupportedContentTypeError, match="Unsupported content type"):
        api_client.response_deserialize(cast(rest.RESTResponse, response), {"400": "ErrorResponse"})


def test_api_exception_from_response_is_typed_as_no_return() -> None:
    hints = get_type_hints(signwell_sdk.ApiException.from_response)

    assert hints["return"] is NoReturn


def test_invalid_http_method_raises_sdk_value_error() -> None:
    client = rest.RESTClientObject(signwell_sdk.Configuration())

    with pytest.raises(signwell_sdk.ApiValueError, match="Unsupported HTTP method"):
        client.request("TRACE", "https://example.com")


def test_exception_strings_redact_sensitive_headers() -> None:
    response = FakeRestResponse(
        status=401,
        reason="Unauthorized",
        body=b'{"error":"bad","token":"body-secret"}',
        headers={
            "Authorization": "Bearer secret-token",
            "Cookie": "session=secret-cookie",
            "Set-Cookie": "session=secret-cookie",
            "X-Api-Key": "secret-api-key",
            "X-Request-Id": "req_123",
        },
    )

    text = str(signwell_sdk.ApiException(http_resp=response))

    assert "secret-token" not in text
    assert "secret-cookie" not in text
    assert "secret-api-key" not in text
    assert "body-secret" not in text
    assert cast(bytes, response.data).decode("utf-8") == signwell_sdk.ApiException(http_resp=response).body
    assert "req_123" in text
    assert text.count("[REDACTED]") == 4
    assert "HTTP response body/data omitted" in text


def test_debug_mode_does_not_enable_global_httplib_wire_logging() -> None:
    original_debuglevel = httplib.HTTPConnection.debuglevel
    try:
        httplib.HTTPConnection.debuglevel = 0
        configuration = signwell_sdk.Configuration()

        configuration.debug = True

        assert httplib.HTTPConnection.debuglevel == 0
    finally:
        httplib.HTTPConnection.debuglevel = original_debuglevel


def test_api_client_context_manager_clears_pool() -> None:
    api_client = signwell_sdk.ApiClient(signwell_sdk.Configuration())
    fake_pool = FakePoolManager()
    cast(Any, api_client.rest_client).pool_manager = fake_pool

    with api_client:
        pass

    assert fake_pool.cleared is True


def test_logger_file_reassignment_replaces_existing_handler(tmp_path: Path) -> None:
    configuration = signwell_sdk.Configuration()
    package_logger = configuration.logger["package_logger"]
    first_log = tmp_path / "first.log"
    second_log = tmp_path / "second.log"

    try:
        configuration.logger_file = str(first_log)
        first_handler = configuration.logger_file_handler
        assert isinstance(first_handler, logging.FileHandler)
        assert first_handler in package_logger.handlers

        configuration.logger_file = str(second_log)
        second_handler = configuration.logger_file_handler

        assert isinstance(second_handler, logging.FileHandler)
        assert second_handler is not first_handler
        assert first_handler not in package_logger.handlers
        assert second_handler in package_logger.handlers
        assert package_logger.handlers.count(second_handler) == 1
    finally:
        configuration.logger_file = None
