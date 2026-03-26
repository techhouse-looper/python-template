"""CLI entry point for the template package."""

import click

from python_template import __version__

DEFAULT_TASKS = (
    "uv sync --group dev",
    "make check",
    "make build",
)


@click.group(
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Show the template defaults and example commands.",
)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Run the template CLI."""
    if ctx.invoked_subcommand is not None:
        return

    click.echo(f"python-template {__version__}")
    click.echo("Default tasks:")
    for task in DEFAULT_TASKS:
        click.echo(f"- {task}")


@cli.command()
@click.option("--name", default="Yujeong", show_default=True, help="Name to greet.")
def hello(name: str) -> None:
    """Print a tiny example subcommand."""
    click.echo(f"Let's build something fun, {name}.")


def main() -> None:
    """Run the CLI."""
    cli()


if __name__ == "__main__":
    main()
