"""CLI regression tests."""

from __future__ import annotations

import subprocess
import sys

from python_template import __version__


def test_module_cli_runs() -> None:
    """Run the module entry point and verify the default guidance output."""
    result = subprocess.run(
        [sys.executable, "-m", "python_template"],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "python-template" in result.stdout
    assert "make check" in result.stdout


def test_module_cli_help_runs() -> None:
    """Run the module help command."""
    result = subprocess.run(
        [sys.executable, "-m", "python_template", "--help"],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Show the template version and default tasks." in result.stdout
    assert "Usage:" in result.stdout


def test_package_exports_version() -> None:
    """Expose the package version at the top level."""
    assert __version__ == "0.1.0"
