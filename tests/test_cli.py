from testfixtures import TempDirectory
import pytest
from clipenv.cli import commands
from clipenv import exceptions
import re

PROFILE_FILE_NAME = "profile"


@pytest.fixture()
def test_dir():
    with TempDirectory() as test_dir:
        yield test_dir


@pytest.fixture()
def default_profile_file(test_dir):
    profile_file_path = commands.os.path.join(test_dir.path, PROFILE_FILE_NAME)
    open(profile_file_path, "a").close()
    return profile_file_path


def added_venv_exists(default_profile_file, variable_name, variable_value):
    all_vars = ""
    variable_line = F"export {variable_name}='{variable_value}'"
    with open(default_profile_file, "r") as profile_file:
        all_vars = profile_file.read()
    return check_if_string_in_text(variable_line, all_vars)


def check_if_string_in_text(needed_string, text):
    return re.search(needed_string, text)


def test_add_venv(default_profile_file):
    variable_name = "TOKEN"
    variable_value = "12345"
    if commands.add_env_var(variable_name=variable_name,
                            variable_value=variable_value,
                            profile_file_path=default_profile_file):
        assert added_venv_exists(
            default_profile_file=default_profile_file,
            variable_name=variable_name,
            variable_value=variable_value
        )
    else:
        assert False


def test_profile_not_found(test_dir):
    variable_name = "TOKEN"
    variable_value = "12345"
    wrong_profile_file = "wrong_file"
    profile_file_path = commands.os.path.join(
        test_dir.path, wrong_profile_file)
    with pytest.raises(exceptions.ClipenvFileNotFoundError):
        if commands.add_env_var(variable_name=variable_name,
                                variable_value=variable_value,
                                profile_file_path=profile_file_path):
            assert not added_venv_exists(
                default_profile_file=profile_file_path,
                variable_name=variable_name,
                variable_value=variable_value
            )


def test_list_all_venvs(default_profile_file):
    variable_name = "TOKEN"
    variable_value = "12345"
    variable_line = F"export {variable_name}='{variable_value}'"
    successfully_added = commands.add_env_var(
        variable_name=variable_name,
        variable_value=variable_value,
        profile_file_path=default_profile_file)
    assert successfully_added
    all_vars = commands.list_all_env_vars(default_profile_file)
    assert check_if_string_in_text(variable_line, all_vars)


def test_list_venvs_missing(default_profile_file):
    variable_name = "TOKEN"
    variable_value = "12345"
    variable_line = F"export {variable_name}='{variable_value}'"
    with pytest.raises(exceptions.ClipenvFileNotFoundError):
        all_vars = commands.list_all_env_vars("non_existent_file")
        assert check_if_string_in_text(variable_line, all_vars)
