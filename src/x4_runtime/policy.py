from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Policy:
    offline: bool = True
    cloud_fallback: bool = False  # opt-in only
    max_tokens: int = 2048
    timeout_s: float = 60.0
    allow_shell: bool = False


def gate(policy: Policy, request: dict[str, Any]) -> tuple[bool, str]:
    """Return (allowed, reason)."""
    if policy.offline and request.get("requires_network"):
        if not policy.cloud_fallback:
            return False, "offline mode: network providers blocked (enable cloud_fallback explicitly)"
    if request.get("shell") and not policy.allow_shell:
        return False, "shell execution denied by policy"
    tokens = int(request.get("max_tokens") or 0)
    if tokens > policy.max_tokens:
        return False, f"max_tokens {tokens} exceeds policy limit {policy.max_tokens}"
    return True, "ok"
