from enum import Enum


class UserInputException(Exception):
    """User Interrupt"""

    pass


class BoardError(Enum):
    Empty = "No error"
    NoMatch = "No matching Card found"
    NotAvailable = "Card Pile is Empty"


def get_user_input(txt: str = "Name Card") -> str:
    user_input = input(txt)
    if len(user_input.strip()) > 0 and isinstance(user_input, str):
        return user_input
    else:
        raise UserInputException
