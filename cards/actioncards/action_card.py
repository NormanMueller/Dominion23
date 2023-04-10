from dataclasses import dataclass
from enum import IntFlag
import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from cards.utils.base_card import (
    BaseCard,
)
from abc import ABC, abstractmethod


class Draws(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class Deletes(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class Discards(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class Actions(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class Buys(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3


@dataclass
class ActionCard(BaseCard):
    # standard actions
    DRAWS: Draws = Draws.ZERO
    DELETES: Deletes = Deletes.ZERO
    DISCARDS: Discards = Discards.ZERO
    ACTIONS: Actions = Actions.ZERO
    BUYS: Buys = Buys.ZERO
