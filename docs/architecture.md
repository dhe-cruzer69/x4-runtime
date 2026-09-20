# Architecture

```text
Provider → Model Router → Policy Gate → Execution → Receipt → Fallback
```

v0.1 implements detect, recommend, policy, dry-run route. Execution backends are intentionally not claimed until tested.
