# SignWell Python SDK

Python SDK for the SignWell API.

This package is generated from the SignWell OpenAPI spec by
`Bidsketch/signwell-sdk-generator`. Do not edit generated SDK runtime files
directly; make durable changes in the generator repo.

## Installation

```bash
pip install signwell-sdk-python
```

With uv:

```bash
uv add signwell-sdk-python
```

## Quick Start

```python
import os

import signwell_sdk
from signwell_sdk.api.document_api import DocumentApi

configuration = signwell_sdk.Configuration(
    api_key={"api_key": os.environ["SIGNWELL_API_KEY"]}
)

with signwell_sdk.ApiClient(configuration) as api_client:
    documents = DocumentApi(api_client)
    document = documents.get_document("document-id")
    print(document.id)
```

The SDK sends the API key in the `X-Api-Key` header. The default host is
`https://www.signwell.com`.

## Resources, Models, And Errors

The generated resource clients are available from their generated modules and
from the parity namespace:

```python
documents = signwell_sdk.Resources.DocumentApi(api_client)
model_cls = signwell_sdk.Models.DocumentResponse
not_found_cls = signwell_sdk.Errors.NotFoundError
```

Status-specific errors inherit from `signwell_sdk.ApiException`:

```python
try:
    documents.get_document("missing")
except signwell_sdk.Errors.NotFoundError as exc:
    print(exc.status)
    print(exc.data or exc.body)
```

## Binary And JSON Responses

Some endpoints can return either JSON or binary data. The SDK selects the
correct `Accept` header from the mode parameters.

```python
from signwell_sdk.api.bulk_send_api import BulkSendApi
from signwell_sdk.api.regional_api import RegionalApi

bulk_send = BulkSendApi(api_client)
csv_bytes = bulk_send.get_bulk_send_csv_template(
    ["00000000-0000-0000-0000-000000000000"]
)
csv_json = bulk_send.get_bulk_send_csv_template(
    ["00000000-0000-0000-0000-000000000000"],
    var_base64=True,
)

documents = DocumentApi(api_client)
pdf_bytes = documents.get_completed_pdf("doc_123")
pdf_url = documents.get_completed_pdf("doc_123", url_only=True)

regional = RegionalApi(api_client)
certificate_bytes = regional.get_nom151_certificate("doc_123")
certificate_url = regional.get_nom151_certificate("doc_123", url_only=True)
certificate_object = regional.get_nom151_certificate("doc_123", object_only=True)
```

## Embedded Helpers

```python
doc = signwell_sdk.Embedded.create_signing_document(
    name="NDA",
    files=[{"name": "nda.pdf", "file_base64": "JVBERi0xLjQK"}],
    recipients=[{"name": "Jane Doe", "email": "jane@example.com"}],
    fields=[[{"x": 20, "y": 60, "page": 1, "type": "signature"}]],
    options={"api_client": api_client},
)

url = signwell_sdk.Embedded.embedded_signing_url(doc)
```

Embedded signing documents must include fields for every recipient, set
`with_signature_page=True`, or set `text_tags=True`.

## Webhook Verification

```python
payload = request.json()
event = payload["event"]

signwell_sdk.Webhook.verify_event_or_raise(
    event=event,
    webhook_id=os.environ["SIGNWELL_WEBHOOK_ID"],
    tolerance_seconds=300,
)
```

For side-effecting handlers, use replay-aware verification with an atomic store:

```python
store = signwell_sdk.Webhook.MemoryReplayStore()

signwell_sdk.Webhook.verify_event_once_or_raise(
    event=event,
    webhook_id=os.environ["SIGNWELL_WEBHOOK_ID"],
    tolerance_seconds=300,
    replay_store=store,
)
```

`MemoryReplayStore` is intended for local development and single-process apps.
Production apps should use a shared atomic store such as Redis or a database
table with a uniqueness constraint.

## Local Package Build

```bash
uv sync --dev
uv run pytest
uv build --no-sources
```

`uv build --no-sources` verifies that the source distribution and wheel can be
built from publishable package metadata.
