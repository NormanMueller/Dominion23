import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from cards.utils.base_card import CardCost
from cards.utils.base_card import CardType
from cards.utils.base_card import CardMoney
from cards.utils.base_card import CardVictory
from cards.utils.base_card import Cardname
from cards.utils.base_card import Expansion
from cards.utils.base_card import BaseCard


class Copper(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            Cardname.Copper,
            CardCost.ZERO,
            CardType.TREASURECARD,
            CardMoney.ONE,
            CardVictory.ZERO,
            Expansion.Dominion,
        )


class Silver(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            Cardname.Silver,
            CardCost.THREE,
            CardType.TREASURECARD,
            CardMoney.TWO,
            CardVictory.ZERO,
            Expansion.Dominion,
        )


class Gold(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            Cardname.Gold,
            CardCost.SIX,
            CardType.TREASURECARD,
            CardMoney.THREE,
            CardVictory.ZERO,
            Expansion.Dominion,
        )
