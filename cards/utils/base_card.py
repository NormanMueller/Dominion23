from dataclasses import dataclass
from enum import Enum, auto, IntFlag


class CardType(Enum):
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


class Cardname(Enum):
    Copper = "Copper"
    Silver = "Silver"
    Gold = "Gold"
    Estate = "Estate"
    Duchy = "Duchy"
    Province = "Province"
    Smithy = "Smithy"
    Cellar = "Cellar"
    Village = "Village"


class Expansion(Enum):
    Dominion = "Dominion"
    Intrigue = "Intrigue"
    Seaside = "Seaside"


@dataclass
class BaseCard:
    """Base Card Image"""

    NAME: Cardname
    PRICE: CardCost
    TYPE: CardType
    MONEY: CardMoney
    VICTORY: CardVictory
    EXPANSION: Expansion

    def __post_init__(self):
        """Card types have different quantitys on the board"""
        if self.TYPE == CardType.ACTIONCARD:
            self.QUANTITY = 10
        elif self.TYPE == CardType.VICTORYCARD and self.NAME != Cardname.Province:
            self.QUANTITY = 20
        elif self.NAME == Cardname.Province:
            self.QUANTITY = 10
        elif self.TYPE == CardType.TREASURECARD:
            self.QUANTITY = 30
