from fastapi import HTTPException

class UserNotFound(HTTPException):
    pass


class AdminNotFound(UserNotFound):
    pass


class DeletedUserWarning(HTTPException):
    pass


class IncorrectPlay(HTTPException):
    pass