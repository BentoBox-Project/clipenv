from pathlib import Path
import os

from clipenv import CONFIG_FILES
from .exceptions import InvalidConfigFileOption


def get_existing_config_files(root=Path.home(), config_files=CONFIG_FILES):
    existing_config_files = {}
    index = 0
    for config_file in config_files:
        if _file_exists(root, config_file):
            index += 1
            existing_config_files[index] = config_file
    return existing_config_files


def filepath_from_option(option, existing_config_files, root=Path.home()):
    try:
        filename = existing_config_files[option]
    except KeyError:
        message = "Invalid option, choose an existing option from the menu"
        raise InvalidConfigFileOption(message)

    return os.path.join(root, filename)


def _file_exists(root, config_file):
    filepath = os.path.join(root, config_file)
    return os.path.isfile(filepath)


def is_valid_var_name(venv_name):
    return False if ' ' in venv_name or '=' in venv_name else True
