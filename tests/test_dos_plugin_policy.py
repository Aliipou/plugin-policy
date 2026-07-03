from dos_plugin_policy import DemoCompiler, PolicyCompiler


def test_compiler_matches_protocol_and_defaults_deny():
    c = DemoCompiler()
    assert isinstance(c, PolicyCompiler)
    pol = c.compile("package x")
    assert pol["default"] == "deny"
