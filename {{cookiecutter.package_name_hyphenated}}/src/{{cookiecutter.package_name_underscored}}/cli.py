"""Command line interface for {{ cookiecutter.package_name_underscored }}

Notes
-----
Click is a great Python package for creating command line interfaces.

Please see `Click documentation <https://click.palletsprojects.com/en/stable/>`_.
"""
import click

import {{ cookiecutter.package_name_underscored }}


@click.command()
@click.option("--verbose", is_flag=True, help="Print additional details.")
@click.version_option({{ cookiecutter.package_name_underscored }}.__version__)
def cli(verbose):
    """Command line interface for {{ cookiecutter.package_name_hyphenated }}

    {{ cookiecutter.package_short_description }}
    """
    click.echo(
        "This is the command line interface for "
        "{{ cookiecutter.package_name_hyphenated }}"
    )
    click.echo("View help using option --help")
    click.echo("Check version using option --version")
    click.echo(
        "Add Click commands and groups to the command line interface at "
        "src/{{ cookiecutter.package_name_underscored }}/cli.py"
    )
    click.echo("See Click documentation at https://click.palletsprojects.com/en/stable/")
    click.echo(
        "Add your code as your see fit to the module at "
        "src/{{ cookiecutter.package_name_underscored }}/{{ cookiecutter.package_name_underscored }}.py"
    )
    if verbose:
        click.secho("VERBOSE mode is on", fg="green")


if __name__ == "__main__":
    cli()
