import os
from .. import exceptions


def add(variable_name, variable_value, profile_file_path):
    """
    receives a variable name and a value and stores it on the
    previously selected profile file.
    """
    successfully_added = False
    try:
        exists = os.path.isfile(profile_file_path)  # The profile file most exists
        if exists:
            with open(profile_file_path, "a") as profile_file:
                profile_file.write(F"export {variable_name}='{variable_value}'")
                profile_file.write("\n")
            successfully_added = True
        else:
            raise exceptions.ClipenvFileNotFoundError("File not Found")

    except (exceptions.ClipenvIOError, Exception) as e:
        raise exceptions.ClipenvFileNotFoundError(e)

    return successfully_added
