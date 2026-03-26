"""CLI entry point for the template package."""

import click

from python_template import __version__

DEFAULT_TASKS = (
    "uv sync --group dev",
    "make check",
    "make build",
)


@click.command(help="Show the template version and default tasks.")
def cli() -> None:
    """Print the template version and recommended first commands."""
    click.echo(f"python-template {__version__}")
    click.echo("Default tasks:")
    for task in DEFAULT_TASKS:
        click.echo(f"- {task}")


def main() -> None:
    """Run the CLI."""
    cli()


if __name__ == "__main__":
    main()
