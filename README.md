# x4-runtime

[![CI](https://github.com/dhe-cruzer69/x4-runtime/actions/workflows/ci.yml/badge.svg)](https://github.com/dhe-cruzer69/x4-runtime/actions)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

**Local-first model runtime with hardware-aware routing and policy gate.**

```text
Provider → Model Router → Policy Gate → Execution → Receipt → Fallback
```

## 30-second demo

```bash
pip install -e ".[dev]"
x4-runtime detect
x4-runtime recommend --ram 8
x4-runtime route --prompt "hello" --dry-run
```

## Scope (v0.1)

- Hardware detection (RAM, arch, OS)
- Model size recommendations
- Provider health stubs (Ollama / OpenAI-compatible)
- Policy gate (offline mode, cloud fallback **opt-in only**)
- Cost / latency placeholders for future metering
- Integrates with **x4-obs** receipts (optional import)

Not an agent framework — focused orchestration layer.

## License

Apache-2.0
