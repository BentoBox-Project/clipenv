#######
# Exceptions
######


class ClipenvError(Exception):
    """Base class for Clipenv exceptions"""


class ClipenvIllegalArgumentError(ValueError, ClipenvError):
    """Raised when an incorrect parameter is passed to a function"""
    pass


class ClipenvIOError(IOError, ClipenvError):
    """Base class for Mastodon.py I/O errors"""


class ClipenvFileNotFoundError(ValueError, ClipenvIOError):
    """Raised when a file requested to be loaded can not be opened"""
    pass
