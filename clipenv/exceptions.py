#######
# Exceptions
######


class ClipenvError(ValueError):
    """Base class for Clipenv exceptions"""


class ClipenvIllegalArgumentError(ClipenvError):
    """Raised when an incorrect parameter is passed to a function"""
    pass


class ClipenvIOError(IOError):
    """Base class for I/O errors"""


class ClipenvFileNotFoundError(ClipenvIOError):
    """Raised when a file requested to be loaded can not be opened"""
    pass


class InvalidConfigFileOption(KeyError):
    """Raise when the user enter an invalid file option"""
