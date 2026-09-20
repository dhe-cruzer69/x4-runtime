from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .hardware import detect_hardware, recommend
from .policy import Policy, gate


@dataclass
class RouteResult:
    allowed: bool
    reason: str
    provider: str | None
    model: str | None
    dry_run: bool
    meta: dict[str, Any]


def route(
    prompt: str,
    *,
    policy: Policy | None = None,
    dry_run: bool = True,
    provider: str | None = None,
) -> RouteResult:
    """Select provider/model under policy. v0.1 is dry-run by default (no network)."""
    policy = policy or Policy()
    hw = detect_hardware()
    rec = recommend(hw)

    req = {
        "requires_network": provider not in (None, "ollama", "local"),
        "shell": False,
        "max_tokens": policy.max_tokens,
        "prompt_len": len(prompt),
    }
    allowed, reason = gate(policy, req)
    if not allowed:
        return RouteResult(False, reason, None, None, dry_run, {"hardware": hw})

    chosen_provider = provider or "ollama"
    chosen_model = rec["recommended_model"]
    return RouteResult(
        allowed=True,
        reason="ok",
        provider=chosen_provider,
        model=chosen_model,
        dry_run=dry_run,
        meta={"hardware": hw, "recommend": rec, "prompt_preview": prompt[:80]},
    )
