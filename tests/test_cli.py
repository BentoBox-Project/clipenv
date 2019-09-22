from testfixtures import TempDirectory
import pytest
from clipenv.cli import commands
from clipenv import exceptions

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


def added_venv_exists(default_profile_file):
    variable_name = "TOKEN"
    variable_value = "12345"
    all_vars = ""
    variable_line = F"{variable_name}='{variable_value}'"
    with open(default_profile_file, "r") as profile_file:
        all_vars = profile_file.read()
    return variable_line in all_vars


def test_add_venv(default_profile_file):
    variable_name = "TOKEN"
    variable_value = "12345"
    if commands.add(variable_name, variable_value, default_profile_file):
        assert added_venv_exists(default_profile_file)
    else:
        assert False


def test_profile_not_found(test_dir):
    variable_name = "TOKEN"
    variable_value = "12345"
    wrong_profile_file = "wrong_file"
    profile_file_path = commands.os.path.join(test_dir.path, wrong_profile_file)
    with pytest.raises(exceptions.ClipenvFileNotFoundError):
        if commands.add(variable_name, variable_value, profile_file_path):
            assert added_venv_exists(profile_file_path)
        else:
            assert True
