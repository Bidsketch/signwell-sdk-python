# Source: signwell-sdk-generator/extras/python/overlay/signwell_sdk/embedded.py
# Do not edit the generated SDK copy directly.

from __future__ import annotations

import json
import re
from collections.abc import Mapping, Sequence
from typing import Any
from urllib.parse import urlparse

from signwell_sdk.api.document_api import DocumentApi
from signwell_sdk.api_client import ApiClient
from signwell_sdk.models.document_from_template_request import DocumentFromTemplateRequest
from signwell_sdk.models.document_request import DocumentRequest
from signwell_sdk.models.fields_inner_inner import FieldsInnerInner
from signwell_sdk.models.files_inner import FilesInner
from signwell_sdk.models.recipients_inner import RecipientsInner
from signwell_sdk.models.template_recipients_inner import TemplateRecipientsInner

SCRIPT_URL = "https://static.signwell.com/assets/embedded.js"
SAFE_HANDLER_PATH = re.compile(r"^[$A-Z_][0-9A-Z_$]*(?:\.[$A-Z_][0-9A-Z_$]*)*$", re.IGNORECASE)
BLOCKED_HANDLER_SEGMENTS = {"__proto__", "constructor", "prototype"}
DEFAULT_SIGNWELL_HOSTS = {"www.signwell.com", "signwell.com"}


def create_signing_document(
    *,
    name: str,
    files: Sequence[Mapping[str, Any]],
    recipients: Sequence[Mapping[str, Any]],
    fields: Sequence[Sequence[Mapping[str, Any]]] | None = None,
    test_mode: bool = False,
    send_notifications: bool = False,
    options: Mapping[str, Any] | None = None,
    **attrs: Any,
) -> Any:
    recipient_models = _build_recipients(recipients)
    request_attrs = {
        **attrs,
        "name": name,
        "test_mode": test_mode,
        "files": _build_files(files),
        "recipients": recipient_models,
        "embedded_signing": True,
        "embedded_signing_notifications": send_notifications,
    }
    if fields is not None:
        request_attrs["fields"] = _build_fields(fields, recipient_models)

    request = DocumentRequest(**request_attrs)
    _validate_signing_placement(request, recipient_models)
    return _document_api(options).create_document(request)


def create_requesting_document(
    *,
    name: str,
    files: Sequence[Mapping[str, Any]],
    recipients: Sequence[Mapping[str, Any]],
    test_mode: bool = False,
    options: Mapping[str, Any] | None = None,
    **attrs: Any,
) -> Any:
    request = DocumentRequest(
        **attrs,
        name=name,
        test_mode=test_mode,
        files=_build_files(files),
        recipients=_build_recipients(recipients),
        draft=True,
    )
    return _document_api(options).create_document(request)


def create_signing_document_from_template(
    *,
    recipients: Sequence[Mapping[str, Any]],
    template_id: str | None = None,
    template_ids: Sequence[str] | None = None,
    test_mode: bool = False,
    send_notifications: bool = False,
    options: Mapping[str, Any] | None = None,
    **attrs: Any,
) -> Any:
    if template_id and template_ids:
        raise ValueError("Provide either template_id or template_ids, not both")
    if not template_id and not template_ids:
        raise ValueError("Provide template_id or template_ids")

    request_attrs = {
        **attrs,
        "test_mode": test_mode,
        "recipients": _build_template_recipients(recipients),
        "embedded_signing": True,
        "embedded_signing_notifications": send_notifications,
    }
    if template_id:
        request_attrs["template_id"] = template_id
    if template_ids:
        request_attrs["template_ids"] = list(template_ids)

    request = DocumentFromTemplateRequest(**request_attrs)
    return _document_api(options).create_document_from_template(request)


def embedded_signing_urls(document: Any) -> dict[str, str]:
    recipients = getattr(document, "recipients", None) or []
    urls: dict[str, str] = {}
    for recipient in recipients:
        email = getattr(recipient, "email", None)
        url = getattr(recipient, "embedded_signing_url", None)
        if email and url:
            urls[email] = url
    return urls


def embedded_signing_url(document: Any, recipient_index: int = 0) -> str | None:
    recipients = getattr(document, "recipients", None) or []
    if recipient_index < 0 or recipient_index >= len(recipients):
        return None
    return getattr(recipients[recipient_index], "embedded_signing_url", None)


def script_tag() -> str:
    return f'<script src="{SCRIPT_URL}"></script>'


def signing_iframe(
    *,
    url: str,
    allowed_embed_hosts: Sequence[str] | None = None,
    allowed_redirect_hosts: Sequence[str] | None = None,
    container_id: str | None = None,
    allow_decline: bool | None = None,
    allow_close: bool | None = None,
    show_header: bool | None = None,
    allow_download: bool | None = None,
    redirect_url: str | None = None,
    decline_redirect_url: str | None = None,
    events: Mapping[str, str] | None = None,
    auto_open: bool = True,
) -> str:
    options = _build_iframe_options(
        url=url,
        allowed_embed_hosts=allowed_embed_hosts,
        allowed_redirect_hosts=allowed_redirect_hosts,
        values={"containerId": container_id},
        booleans={
            "allowDecline": allow_decline,
            "allowClose": allow_close,
            "showHeader": show_header,
            "allowDownload": allow_download,
        },
        redirects={"redirectUrl": redirect_url, "declineRedirectUrl": decline_redirect_url},
    )
    return _build_embed_script(options, events or {}, auto_open)


def requesting_iframe(
    *,
    url: str,
    allowed_embed_hosts: Sequence[str] | None = None,
    allowed_redirect_hosts: Sequence[str] | None = None,
    container_id: str | None = None,
    allow_close: bool | None = None,
    show_header: bool | None = None,
    allow_download: bool | None = None,
    show_send_button: bool | None = None,
    redirect_url: str | None = None,
    events: Mapping[str, str] | None = None,
    auto_open: bool = True,
) -> str:
    options = _build_iframe_options(
        url=url,
        allowed_embed_hosts=allowed_embed_hosts,
        allowed_redirect_hosts=allowed_redirect_hosts,
        values={"containerId": container_id},
        booleans={
            "allowClose": allow_close,
            "showHeader": show_header,
            "allowDownload": allow_download,
            "showSendButton": show_send_button,
        },
        redirects={"redirectUrl": redirect_url},
    )
    return _build_embed_script(options, events or {}, auto_open)


def _document_api(options: Mapping[str, Any] | None) -> Any:
    options = options or {}
    if options.get("document_api") is not None:
        return options["document_api"]
    if options.get("api_client") is not None:
        return DocumentApi(options["api_client"])
    if options.get("configuration") is not None:
        return DocumentApi(ApiClient(options["configuration"]))
    return DocumentApi()


def _build_recipients(recipients: Sequence[Mapping[str, Any]]) -> list[RecipientsInner]:
    return [RecipientsInner(**_recipient_attrs(recipient, index)) for index, recipient in enumerate(recipients)]


def _build_template_recipients(recipients: Sequence[Mapping[str, Any]]) -> list[TemplateRecipientsInner]:
    built = []
    for index, recipient in enumerate(recipients):
        attrs = _recipient_attrs(recipient, index)
        placeholder_name = _mapping_value(recipient, "placeholder_name")
        if placeholder_name:
            attrs["placeholder_name"] = placeholder_name
        built.append(TemplateRecipientsInner(**attrs))
    return built


def _build_files(files: Sequence[Mapping[str, Any]]) -> list[FilesInner]:
    built = []
    for file_input in files:
        name = _mapping_value(file_input, "name")
        file_url = _mapping_value(file_input, "file_url")
        file_base64 = _mapping_value(file_input, "file_base64")
        has_url = _present(file_url)
        has_base64 = _present(file_base64)

        if not _present(name):
            raise ValueError("Each file must include name")
        if has_url == has_base64:
            raise ValueError("Each file must include exactly one of file_url or file_base64")

        attrs = {"name": name}
        attrs["file_url" if has_url else "file_base64"] = file_url if has_url else file_base64
        built.append(FilesInner(**attrs))
    return built


def _build_fields(
    fields: Sequence[Sequence[Mapping[str, Any]]],
    recipients: Sequence[RecipientsInner],
) -> list[list[FieldsInnerInner]]:
    default_recipient_id = recipients[0].id if recipients else None
    built = []
    for file_fields in fields:
        file_field_models = []
        for field_input in file_fields:
            attrs = dict(field_input)
            attrs.setdefault("recipient_id", default_recipient_id)
            attrs.setdefault("required", True)
            if not attrs.get("recipient_id"):
                raise ValueError("Each field must include recipient_id when no default recipient exists")
            file_field_models.append(FieldsInnerInner(**attrs))
        built.append(file_field_models)
    return built


def _validate_signing_placement(request: DocumentRequest, recipients: Sequence[RecipientsInner]) -> None:
    if request.with_signature_page is True or request.text_tags is True:
        return

    field_groups = request.fields or []
    fields = [field for file_fields in field_groups for field in file_fields]
    assigned_recipient_ids = {str(field.recipient_id) for field in fields if getattr(field, "recipient_id", None)}
    missing_recipients = [
        recipient for recipient in recipients if recipient.id and recipient.id not in assigned_recipient_ids
    ]

    if not fields or missing_recipients:
        raise ValueError(
            "Embedded signing documents must include fields for every recipient, "
            "set with_signature_page=True, or set text_tags=True"
        )


def _recipient_attrs(recipient: Mapping[str, Any], index: int) -> dict[str, Any]:
    attrs = {
        "id": _mapping_value(recipient, "id") or str(index + 1),
        "name": _mapping_value(recipient, "name"),
        "email": _mapping_value(recipient, "email"),
    }
    passcode = _optional_string(_mapping_value(recipient, "passcode"))
    if passcode:
        attrs["passcode"] = passcode
    return attrs


def _build_iframe_options(
    *,
    url: str,
    allowed_embed_hosts: Sequence[str] | None,
    allowed_redirect_hosts: Sequence[str] | None,
    values: Mapping[str, str | None],
    booleans: Mapping[str, bool | None],
    redirects: Mapping[str, str | None],
) -> dict[str, Any]:
    options: dict[str, Any] = {"url": _validate_embed_url(url, allowed_embed_hosts)}
    for value_key, string_value in values.items():
        if string_value is not None:
            options[value_key] = string_value
    for boolean_key, boolean_value in booleans.items():
        if boolean_value is not None:
            options[boolean_key] = boolean_value
    for redirect_key, redirect_value in redirects.items():
        if redirect_value is not None:
            options[redirect_key] = _validate_redirect_url(redirect_value, allowed_redirect_hosts)
    return options


def _build_embed_script(options: Mapping[str, Any], events: Mapping[str, str], auto_open: bool) -> str:
    options_json = json.dumps(options, separators=(",", ":"))
    lines = [f"var signwellEmbed = new SignWellEmbed({options_json});"]
    for event_name, handler_path in events.items():
        if handler_path:
            safe_event = json.dumps(event_name)
            lines.append(f"signwellEmbed.on({safe_event}, {_validate_handler_path(handler_path)});")
    if auto_open:
        lines.append("signwellEmbed.open();")
    body = "\n".join(lines)
    return f"<script>\n{body}\n</script>"


def _validate_embed_url(url: str, allowed_hosts: Sequence[str] | None) -> str:
    parsed = _parse_https_url(url)
    host = parsed.hostname or ""
    allowed = set(allowed_hosts or ())
    if host not in DEFAULT_SIGNWELL_HOSTS and not host.endswith(".signwell.com") and host not in allowed:
        raise ValueError("Embedded URLs must be SignWell-hosted unless explicitly allowed")
    return url


def _validate_redirect_url(url: str, allowed_hosts: Sequence[str] | None) -> str:
    parsed = _parse_https_url(url)
    if allowed_hosts is not None and parsed.hostname not in set(allowed_hosts):
        raise ValueError("Redirect URL host is not allowed")
    return url


def _parse_https_url(url: str):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        raise ValueError("URL must use HTTPS")
    if not parsed.hostname:
        raise ValueError("URL must include a host")
    if parsed.username or parsed.password:
        raise ValueError("URL must not include credentials")
    return parsed


def _validate_handler_path(path: str) -> str:
    if not SAFE_HANDLER_PATH.fullmatch(path):
        raise ValueError("Event handler must be a dot-separated JavaScript identifier path")
    if any(segment in BLOCKED_HANDLER_SEGMENTS for segment in path.split(".")):
        raise ValueError("Event handler path contains a blocked segment")
    return path


def _mapping_value(mapping: Mapping[str, Any], key: str) -> Any:
    return mapping.get(key)


def _optional_string(value: Any) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip()
    return normalized or None


def _present(value: Any) -> bool:
    return value is not None and (not hasattr(value, "__len__") or len(value) > 0)
