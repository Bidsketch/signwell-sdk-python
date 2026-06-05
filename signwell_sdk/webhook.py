# Source: signwell-sdk-generator/extras/python/overlay/signwell_sdk/webhook.py
# Do not edit the generated SDK copy directly.

from __future__ import annotations

import hmac
import time as time_module
from collections.abc import Callable, Mapping
from threading import Lock
from typing import Any, Protocol


class ReplayStore(Protocol):
    def add(self, key: str, expires_at_unix_seconds: float) -> bool:
        """Atomically store key until expires_at_unix_seconds if it does not exist."""


class MemoryReplayStore:
    """Small replay store for local development and single-process apps."""

    def __init__(
        self,
        *,
        max_entries: int = 10_000,
        now: Callable[[], float] | None = None,
    ) -> None:
        if not isinstance(max_entries, int) or max_entries <= 0:
            raise ValueError("max_entries must be a positive integer")

        self._max_entries = max_entries
        self._now = now or _current_unix_time
        self._entries: dict[str, float] = {}
        self._lock = Lock()

    def add(self, key: str, expires_at_unix_seconds: float) -> bool:
        with self._lock:
            current_time = self._now()
            expired = [entry_key for entry_key, expires_at in self._entries.items() if expires_at < current_time]
            for entry_key in expired:
                del self._entries[entry_key]

            if key in self._entries:
                return False

            while len(self._entries) >= self._max_entries:
                oldest = next(iter(self._entries))
                del self._entries[oldest]

            self._entries[key] = float(expires_at_unix_seconds)
            return True


def verify_event(
    *,
    event: Mapping[str, Any],
    webhook_id: str,
    tolerance_seconds: float | None = None,
    now: Callable[[], float] | None = None,
) -> bool:
    try:
        verify_event_or_raise(
            event=event,
            webhook_id=webhook_id,
            tolerance_seconds=tolerance_seconds,
            now=now,
        )
    except (TypeError, ValueError):
        return False
    return True


def verify_event_once(
    *,
    event: Mapping[str, Any],
    webhook_id: str,
    replay_store: ReplayStore,
    tolerance_seconds: float,
    now: Callable[[], float] | None = None,
) -> bool:
    try:
        verify_event_once_or_raise(
            event=event,
            webhook_id=webhook_id,
            replay_store=replay_store,
            tolerance_seconds=tolerance_seconds,
            now=now,
        )
    except (TypeError, ValueError):
        return False
    return True


def verify_event_once_or_raise(
    *,
    event: Mapping[str, Any],
    webhook_id: str,
    replay_store: ReplayStore,
    tolerance_seconds: float,
    now: Callable[[], float] | None = None,
) -> bool:
    if tolerance_seconds is None:
        raise ValueError("tolerance_seconds is required for replay protection")
    if replay_store is None or not callable(getattr(replay_store, "add", None)):
        raise TypeError("replay_store with an atomic add method is required")

    parsed = _verify_event_data(
        event=event,
        webhook_id=webhook_id,
        tolerance_seconds=tolerance_seconds,
        now=now,
    )
    expires_at = float(parsed["time"]) + float(tolerance_seconds)
    if not replay_store.add(_replay_key_from_parsed(parsed), expires_at):
        raise ValueError("webhook event has already been processed")
    return True


def verify_event_or_raise(
    *,
    event: Mapping[str, Any],
    webhook_id: str,
    tolerance_seconds: float | None = None,
    now: Callable[[], float] | None = None,
) -> bool:
    _verify_event_data(
        event=event,
        webhook_id=webhook_id,
        tolerance_seconds=tolerance_seconds,
        now=now,
    )
    return True


def replay_key(event: Mapping[str, Any]) -> str:
    return _replay_key_from_parsed(_parse_event(event))


def _verify_event_data(
    *,
    event: Mapping[str, Any],
    webhook_id: str,
    tolerance_seconds: float | None,
    now: Callable[[], float] | None,
) -> dict[str, Any]:
    if not isinstance(webhook_id, str) or not webhook_id:
        raise ValueError("webhook_id must be a non-empty string")

    parsed = _parse_event(event)
    if tolerance_seconds is not None:
        _verify_fresh_timestamp(parsed["time"], tolerance_seconds, now or _current_unix_time)

    signed_data = f"{parsed['type']}@{parsed['time']}".encode()
    calculated = hmac.new(webhook_id.encode(), signed_data, "sha256").hexdigest()
    if not hmac.compare_digest(calculated, parsed["hash"]):
        raise ValueError("webhook signature is invalid")

    return parsed


def _parse_event(event: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(event, Mapping):
        raise TypeError("event must be a mapping")

    event_type = event.get("type")
    event_time = event.get("time")
    event_hash = event.get("hash")
    missing = [
        key
        for key, value in (("type", event_type), ("time", event_time), ("hash", event_hash))
        if value is None or value == ""
    ]
    if missing:
        raise ValueError(
            "event is missing required keys: "
            + ", ".join(missing)
            + ". Make sure you pass payload['event'], not the full webhook payload"
        )
    if not isinstance(event_hash, str):
        raise TypeError("event.hash must be a string")

    return {"type": event_type, "time": event_time, "hash": event_hash}


def _verify_fresh_timestamp(
    event_time: Any,
    tolerance_seconds: float,
    now: Callable[[], float],
) -> None:
    if not isinstance(tolerance_seconds, int | float) or tolerance_seconds < 0:
        raise ValueError("tolerance_seconds must be a non-negative number")

    try:
        timestamp = float(event_time)
        current_time = float(now())
    except (TypeError, ValueError) as exc:
        raise ValueError("event.time must be a Unix timestamp when tolerance_seconds is provided") from exc

    if abs(current_time - timestamp) > float(tolerance_seconds):
        raise ValueError("webhook timestamp is outside the allowed tolerance")


def _replay_key_from_parsed(event: Mapping[str, Any]) -> str:
    return f"signwell:{event['type']}:{event['time']}:{event['hash']}"


def _current_unix_time() -> float:
    return float(int(time_module.time()))
