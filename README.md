# plugin-policy

**Status: INTERFACE-ONLY** — a Decision OS plugin. Separate, private, and OPTIONAL: it
is a *consumer* of `decision-os-min`, and the core is never modified by it.

## What it plugs into

Seam: **Policy adapter (OPA/Cedar/Rego)**.

Compile external policy languages (OPA/Rego, Cedar) INTO the kernel's deterministic policy dict — reuse mature policy tooling without letting it become a second authority.

## Maturity, honestly

- **REFERENCE** — a real, working implementation you can use/extend.
- **INTERFACE-ONLY** — the plug-seam (Protocol) is defined + a demo/stub; the real
  backend must be wired against actual infrastructure (HSM, OIDC, OPA, …).
- **EXPERIMENTAL** — a modest, clearly-hedged helper; may never graduate.

This one is **INTERFACE-ONLY**. It is promoted into the core ecosystem only if real
usage or evidence proves its value — never merged into the kernel.

## Install

```bash
pip install -e .        # needs decision-os-min on the path
pytest -q
```
