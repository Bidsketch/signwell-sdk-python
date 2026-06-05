from __future__ import annotations

import signwell_sdk
from signwell_sdk.api.document_api import DocumentApi
from signwell_sdk.models.document_response import DocumentResponse


def test_root_exports_and_namespaces():
    assert signwell_sdk.Resources.DocumentApi is DocumentApi
    assert signwell_sdk.Models.DocumentResponse is DocumentResponse
    assert signwell_sdk.Errors.NotFoundError is signwell_sdk.NotFoundError
    assert signwell_sdk.Embedded.SCRIPT_URL == "https://static.signwell.com/assets/embedded.js"
    assert hasattr(signwell_sdk.Webhook, "verify_event")
