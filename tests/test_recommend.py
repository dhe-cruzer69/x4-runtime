from x4_runtime.hardware import recommend

def test_low():
    r = recommend({"ram_gb": 4, "gpu_vram_gb": 0})
    assert "1B" in r["recommended_model"] or "3B" in r["recommended_model"]

def test_high():
    r = recommend({"ram_gb": 32, "gpu_vram_gb": 24})
    assert "13B" in r["recommended_model"] or "34B" in r["recommended_model"]
