from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto, IntFlag

class StrEnum(str, Enum):
    def __str__(self) -> str:
        return self.value

class CardType(StrEnum):
    ACTIONCARD = "Action_Card"
    TREASURECARD = "Treasure_Card"
    VICTORYCARD = "Victory_Card"


class CardCost(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGTH = 8
    NINE = 9


class CardMoney(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4


class CardVictory(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8


class Cardname(StrEnum):
    Copper = "Copper"
    Silver = "Silver"
    Gold = "Gold"
    Estate = "Estate"
    Duchy = "Duchy"
    Province = "Province"
    Smithy = "Smithy"
    Cellar = "Cellar"
    Village = "Village"
    Milits = "Milits"


class Expansion(StrEnum):
    Dominion = "Dominion"
    Intrigue = "Intrigue"
    Seaside = "Seaside"


@dataclass
class BaseCard:
    """Base Card Image"""
    description: str
    name: Cardname
    price: CardCost
    type: CardType
    money: CardMoney
    victory_points: CardVictory
    expansion: Expansion

    def __post_init__(self):
        """Card types have different quantitys on the board"""
        if self.type == CardType.ACTIONCARD:
            self.quantity = 10
        elif self.type == CardType.VICTORYCARD and self.name != Cardname.Province:
            self.quantity = 20
        elif self.name == Cardname.Province:
            self.quantity = 10
        elif self.type == CardType.TREASURECARD:
            self.quantity = 30

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value