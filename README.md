# plugin-policy

Policy-language adapter for the Decision OS / AuthGate stack.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Plugins are advisory only and hold
> **no authority**; the kernel remains the single authority.

**Status: interface-only (Protocol + demo compiler).**

## What it does

Defines the `PolicyCompiler` seam: author policy in a mature external language
(OPA/Rego, Cedar) and **compile it down** to the kernel's deterministic policy
dict at build/deploy time. A `DemoCompiler` shows the shape; real Rego/Cedar
compilers replace it.

## Authority

This plugin holds **no authority**. It compiles policy ahead of time and never
evaluates at decision time — doing so would make it a second authority. The kernel
stays the single authority, and its policy stays a plain deterministic dict.

## Install

```bash
pip install "decision-os-min @ git+https://github.com/Aliipou/decision-os-min.git"
pip install -e . --no-deps
pytest -q          # AUTHGATE_BACKEND=python
```

## Usage

```python
from dos_plugin_policy import DemoCompiler
policy = DemoCompiler().compile("package x")
# policy["default"] == "deny"
```

## Status and limitations

- **Interface only.** `DemoCompiler` emits a fixed deny-by-default dict — it does
  not parse Rego or Cedar. A real compiler is required to be useful and is not
  implemented here.
