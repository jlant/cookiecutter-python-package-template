from click.testing import CliRunner
from {{ cookiecutter.package_name_underscored }}.cli import cli
from {{ cookiecutter.package_name_underscored }}.{{ cookiecutter.package_name_underscored }} import (
    count_words,
)


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


def test_count_words_punctuation_tokens():
    text = "Hello!!! ???"
    result = count_words(text)
    assert "" not in result
    assert result == {"Hello": 1}
