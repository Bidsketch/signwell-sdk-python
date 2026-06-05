from __future__ import annotations

import hmac

import pytest

from signwell_sdk import Webhook


def signed_event(webhook_id: str, event_type: str = "document_completed", event_time: str | int = "1710000000"):
    signature = hmac.new(str(webhook_id).encode(), f"{event_type}@{event_time}".encode(), "sha256").hexdigest()
    return {"type": event_type, "time": event_time, "hash": signature}


def test_verifies_valid_event():
    event = signed_event("whk_123")

    assert Webhook.verify_event(event=event, webhook_id="whk_123") is True
    assert Webhook.verify_event_or_raise(event=event, webhook_id="whk_123") is True


def test_rejects_invalid_signature():
    event = {"type": "document_completed", "time": "1710000000", "hash": "0" * 64}

    assert Webhook.verify_event(event=event, webhook_id="whk_123") is False
    with pytest.raises(ValueError, match="signature is invalid"):
        Webhook.verify_event_or_raise(event=event, webhook_id="whk_123")


def test_requires_string_hash_and_event_object():
    with pytest.raises(TypeError, match=r"event\.hash must be a string"):
        Webhook.verify_event_or_raise(
            event={"type": "document_completed", "time": "1710000000", "hash": 123},
            webhook_id="whk_123",
        )

    with pytest.raises(ValueError, match=r"payload\['event'\]"):
        Webhook.verify_event_or_raise(event={"event": {"type": "document_completed"}}, webhook_id="whk_123")


def test_optionally_enforces_timestamp_freshness():
    event = signed_event("whk_123")

    assert (
        Webhook.verify_event(
            event=event,
            webhook_id="whk_123",
            tolerance_seconds=60,
            now=lambda: 1_710_000_030,
        )
        is True
    )
    assert (
        Webhook.verify_event(
            event=event,
            webhook_id="whk_123",
            tolerance_seconds=60,
            now=lambda: 1_710_000_100,
        )
        is False
    )

    with pytest.raises(ValueError, match="outside the allowed tolerance"):
        Webhook.verify_event_or_raise(
            event=event,
            webhook_id="whk_123",
            tolerance_seconds=60,
            now=lambda: 1_710_000_100,
        )


def test_rejects_replayed_events():
    event = signed_event("whk_123", event_time=1_710_000_000)
    replay_store = Webhook.MemoryReplayStore(now=lambda: 1_710_000_000)

    assert (
        Webhook.verify_event_once_or_raise(
            event=event,
            webhook_id="whk_123",
            tolerance_seconds=60,
            now=lambda: 1_710_000_000,
            replay_store=replay_store,
        )
        is True
    )

    with pytest.raises(ValueError, match="already been processed"):
        Webhook.verify_event_once_or_raise(
            event=event,
            webhook_id="whk_123",
            tolerance_seconds=60,
            now=lambda: 1_710_000_000,
            replay_store=replay_store,
        )

    assert (
        Webhook.verify_event_once(
            event=event,
            webhook_id="whk_123",
            tolerance_seconds=60,
            now=lambda: 1_710_000_000,
            replay_store=replay_store,
        )
        is False
    )


def test_invalid_signature_is_not_stored():
    replay_store = Webhook.MemoryReplayStore(now=lambda: 1_710_000_000)
    invalid = {"type": "document_completed", "time": 1_710_000_000, "hash": "0" * 64}
    valid = signed_event("whk_123", event_time=1_710_000_000)

    assert (
        Webhook.verify_event_once(
            event=invalid,
            webhook_id="whk_123",
            tolerance_seconds=60,
            now=lambda: 1_710_000_000,
            replay_store=replay_store,
        )
        is False
    )
    assert (
        Webhook.verify_event_once(
            event=valid,
            webhook_id="whk_123",
            tolerance_seconds=60,
            now=lambda: 1_710_000_000,
            replay_store=replay_store,
        )
        is True
    )


def test_replay_key_is_stable():
    assert Webhook.replay_key({"type": "document_completed", "time": 1710000000, "hash": "a" * 64}) == (
        f"signwell:document_completed:1710000000:{'a' * 64}"
    )
