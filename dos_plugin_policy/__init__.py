"""Policy-language adapter (OPA/Rego, Cedar) -> kernel policy dict.

INTERFACE ONLY (with a trivial demo compiler). The kernel stays the single
authority and its policy stays a deterministic dict; this plugin lets teams AUTHOR
that policy in OPA/Cedar and compile it down. It never evaluates at decision time —
that would make it a second authority.
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class PolicyCompiler(Protocol):
    language: str

    def compile(self, source: str) -> dict[str, Any]:
        """Translate a policy in `language` into a kernel policy dict."""
        ...


class DemoCompiler:
    """A stand-in that shows the shape. Real Rego/Cedar compilers replace it."""

    language = "demo"

    def compile(self, source: str) -> dict[str, Any]:
        # A real compiler parses OPA/Cedar; this only proves the seam.
        return {"grants": {}, "default": "deny", "_compiled_from": self.language}
