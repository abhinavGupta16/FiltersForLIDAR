class Error(Exception):
    """Base class for other exceptions"""
    pass


class LengthTooSmallError(Error):
    """Raised when the input measurement length is smaller than min"""
    msg = ""
    pass


class LengthTooLargeError(Error):
    """Raised when the input measurement length is greater than max"""
    msg = ""
    pass
