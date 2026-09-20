from x4_runtime.hardware import recommend
from x4_runtime.policy import Policy, gate
from x4_runtime.router import route
from x4_runtime.cli import main


def test_low_ram():
    r = recommend({"ram_gb": 4, "gpu_vram_gb": 0})
    assert "1B" in r["recommended_model"] or "3B" in r["recommended_model"]


def test_high_vram():
    r = recommend({"ram_gb": 32, "gpu_vram_gb": 24})
    assert "13B" in r["recommended_model"] or "34B" in r["recommended_model"]


def test_policy_blocks_network():
    ok, reason = gate(Policy(offline=True, cloud_fallback=False), {"requires_network": True})
    assert ok is False
    assert "offline" in reason


def test_route_dry_run():
    result = route("hello", dry_run=True)
    assert result.allowed is True
    assert result.dry_run is True


def test_cli_detect():
    assert main(["detect"]) == 0
