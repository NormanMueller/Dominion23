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
            description="It produces $1 when played.",
            name=Cardname.Copper,
            price=CardCost.ZERO,
            type=CardType.TREASURECARD,
            money=CardMoney.ONE,
            victory_points=CardVictory.ZERO,
            expansion=Expansion.Dominion,
        )


class Silver(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            description="It produces $2 when played.",
            name=Cardname.Silver,
            price=CardCost.THREE,
            type=CardType.TREASURECARD,
            money=CardMoney.TWO,
            victory_points=CardVictory.ZERO,
            expansion=Expansion.Dominion,
        )


class Gold(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            description="It produces $3 when played.",
            name=Cardname.Gold,
            price=CardCost.SIX,
            type=CardType.TREASURECARD,
            money=CardMoney.THREE,
            victory_points=CardVictory.ZERO,
            expansion=Expansion.Dominion,
        )
