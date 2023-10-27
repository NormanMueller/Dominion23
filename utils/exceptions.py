from enum import Enum
import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")


class UserSkipPhaseException(Exception):
    def __init__(self, message="User want to skip"):
        self.message = message
        super().__init__(self.message)


class UserInputCardValidationError(Exception):
    def __init__(self, message="User want to skip"):
        self.message = message
        super().__init__(self.message)


class BoardErrorEmpty(Exception):
    def __init__(self, message="Card is no longer available"):
        self.message = message
        super().__init__(self.message)


class BoardErrorNoMatch(Exception):
    def __init__(self, message="Card is not in stock"):
        self.message = message
        super().__init__(self.message)


class HandErrorNoMatch(Exception):
    def __init__(self, message="Card is not in hand"):
        self.message = message
        super().__init__(self.message)
