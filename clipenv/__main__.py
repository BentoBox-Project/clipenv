import click
from colored import fg, attr

from clipenv import get_existing_config_files, filepath_from_option
from clipenv import show_config_file_options, enter_variable_name
from clipenv import enter_variable_value
from clipenv.filesystem_utilities import is_valid_var_name
from clipenv.cli import commands


@click.group()
def clipenv():
    pass


@clipenv.command()
def add():
    """
    Adds a new environment variable to a chosen config file hosted in the user
    home directory.
    """
    existing_config_files = get_existing_config_files()
    show_config_file_options(file_options=existing_config_files)
    file_option = click.prompt(f"{fg(2)}Enter the option: {attr(0)}", type=int)
    filepath = filepath_from_option(file_option, existing_config_files)
    variable_name = click.prompt(enter_variable_name())
    if is_valid_var_name(variable_name):
        variable_value = click.prompt(enter_variable_value())
        commands.add_env_var(variable_name, variable_value, filepath)
        click.echo(filepath)
        click.echo(f'export {variable_name}="{variable_value}"')
    else:
        click.echo(f'{fg(1)}The variable name {attr(0)}"{variable_name}" '
                   f'{fg(1)}is not valid \n'
                   f'It can\'t have spaces or symbols like "="')


if __name__ == "__main__":
    clipenv()
