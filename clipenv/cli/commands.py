import os
from .. import exceptions


def add_env_var(variable_name, variable_value, profile_file_path):
    """
    receives a variable name and a value and stores it on the
    previously selected profile file.
    """
    successfully_added = False
    try:
        # The profile file most exists
        exists = os.path.isfile(profile_file_path)
        if exists:
            with open(profile_file_path, "a") as profile_file:
                env_var = f"export {variable_name}='{variable_value}'"
                profile_file.write(env_var)
                profile_file.write("\n")
            successfully_added = True
        else:
            raise exceptions.ClipenvFileNotFoundError("File not Found")

    except (exceptions.ClipenvIOError, Exception) as e:
        raise exceptions.ClipenvFileNotFoundError(e)

    return successfully_added
