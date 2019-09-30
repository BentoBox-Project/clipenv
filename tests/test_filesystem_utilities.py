import contextlib
from pathlib import Path
import os
import tempfile
import shutil

from clipenv import CONFIG_FILES
from clipenv import get_existing_config_files, filepath_from_option


@contextlib.contextmanager
def get_temp_dir():
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


def test_get_existing_config_files():
    with get_temp_dir() as root:
        for config_file in CONFIG_FILES:
            Path(os.path.join(root, config_file)).touch()
        assert len(get_existing_config_files(root=root)) == len(CONFIG_FILES)


def test_get_the_first_config_file():
    with get_temp_dir() as root:
        Path(os.path.join(root, CONFIG_FILES[0])).touch()
        assert len(get_existing_config_files(root=root)) == 1


def test_filepath_from_option():
    filename = ".bashrc"
    config_files_dict = {1: filename}
    with get_temp_dir() as root:
        filepath = filepath_from_option(1, config_files_dict, root=root)
        assert filepath == os.path.join(root, filename)
