from __future__ import annotations

import signwell_sdk
from signwell_sdk.api.document_api import DocumentApi
from signwell_sdk.models.document_response import DocumentResponse


def test_root_exports_and_namespaces():
    assert signwell_sdk.Resources.DocumentApi is DocumentApi
    assert signwell_sdk.Models.DocumentResponse is DocumentResponse
    assert signwell_sdk.Errors.NotFoundError is signwell_sdk.NotFoundError
    assert signwell_sdk.Errors.PermissionDeniedError is signwell_sdk.PermissionDeniedError
    assert signwell_sdk.ForbiddenError is signwell_sdk.PermissionDeniedError
    assert signwell_sdk.Errors.ApiConnectionError is signwell_sdk.ApiConnectionError
    assert signwell_sdk.TransportError is signwell_sdk.ApiConnectionError
    assert issubclass(signwell_sdk.ApiTimeoutError, signwell_sdk.ApiConnectionError)
    assert issubclass(signwell_sdk.FetchError, signwell_sdk.ApiConnectionError)
    assert signwell_sdk.Errors.RequiredError is signwell_sdk.RequiredError
    assert signwell_sdk.RequiredError("id").field == "id"
    assert signwell_sdk.Embedded.SCRIPT_URL == "https://static.signwell.com/assets/embedded.js"
    assert signwell_sdk.create_signing_document is signwell_sdk.Embedded.create_signing_document
    assert signwell_sdk.create_requesting_document is signwell_sdk.Embedded.create_requesting_document
    assert (
        signwell_sdk.create_signing_document_from_template
        is signwell_sdk.Embedded.create_signing_document_from_template
    )
    assert signwell_sdk.embedded_signing_url is signwell_sdk.Embedded.embedded_signing_url
    assert signwell_sdk.embedded_signing_urls is signwell_sdk.Embedded.embedded_signing_urls
    assert signwell_sdk.script_tag is signwell_sdk.Embedded.script_tag
    assert signwell_sdk.signing_iframe is signwell_sdk.Embedded.signing_iframe
    assert signwell_sdk.requesting_iframe is signwell_sdk.Embedded.requesting_iframe
    assert hasattr(signwell_sdk.Webhook, "verify_event")
