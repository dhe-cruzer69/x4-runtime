from __future__ import annotations
import argparse, json
from .hardware import detect_hardware, recommend

def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="x4-runtime")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("detect")
    r = sub.add_parser("recommend"); r.add_argument("--ram", type=float); r.add_argument("--gpu-vram", type=float)
    a = p.parse_args(argv)
    if a.cmd == "detect":
        print(json.dumps(detect_hardware(), indent=2)); return 0
    if a.cmd == "recommend":
        hw = detect_hardware()
        if a.ram is not None: hw["ram_gb"] = a.ram
        if a.gpu_vram is not None: hw["gpu_vram_gb"] = a.gpu_vram
        print(json.dumps(recommend(hw), indent=2)); return 0
    return 1

if __name__ == "__main__": raise SystemExit(main())
