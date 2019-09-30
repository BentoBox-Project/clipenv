import click
from colored import fg, attr

from clipenv import get_existing_config_files


def show_config_file_options(file_options=get_existing_config_files()):
    click.echo(f"{fg(2)}Choose the config file to edit: {attr(0)}")
    for index, config_file in file_options.items():
        click.echo(f"{index}.- {config_file}")


def enter_variable_name():
    """Asks for the environment variable name"""
    return f"{fg(2)}Enter the environment variable name: {attr(0)}"


def enter_variable_value():
    """Asks for the environment variable value"""
    return f"{fg(2)}Enter the environment variable value: {attr(0)}"
