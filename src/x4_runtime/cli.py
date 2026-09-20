from __future__ import annotations

import argparse
import json

from . import __version__
from .hardware import detect_hardware, recommend
from .policy import Policy
from .router import route


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="x4-runtime", description="Local-first model runtime")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("detect", help="Detect local hardware")

    r = sub.add_parser("recommend", help="Recommend model size")
    r.add_argument("--ram", type=float)
    r.add_argument("--gpu-vram", type=float)

    rt = sub.add_parser("route", help="Route a prompt under policy")
    rt.add_argument("--prompt", required=True)
    rt.add_argument("--provider", default=None)
    rt.add_argument("--dry-run", action="store_true", default=True)
    rt.add_argument("--allow-cloud", action="store_true", help="Opt-in cloud fallback")

    args = p.parse_args(argv)

    if args.cmd == "detect":
        print(json.dumps(detect_hardware(), indent=2))
        return 0

    if args.cmd == "recommend":
        hw = detect_hardware()
        if args.ram is not None:
            hw["ram_gb"] = args.ram
        if args.gpu_vram is not None:
            hw["gpu_vram_gb"] = args.gpu_vram
        print(json.dumps(recommend(hw), indent=2))
        return 0

    if args.cmd == "route":
        policy = Policy(cloud_fallback=bool(args.allow_cloud), offline=not args.allow_cloud)
        result = route(
            args.prompt,
            policy=policy,
            dry_run=True,  # v0.1 never calls network
            provider=args.provider,
        )
        print(
            json.dumps(
                {
                    "allowed": result.allowed,
                    "reason": result.reason,
                    "provider": result.provider,
                    "model": result.model,
                    "dry_run": result.dry_run,
                    "meta": result.meta,
                },
                indent=2,
            )
        )
        return 0 if result.allowed else 1

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
