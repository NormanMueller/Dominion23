import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from cards.utils.base_card import BaseCard, CardCost
from cards.utils.base_card import CardType
from cards.utils.base_card import CardMoney
from cards.utils.base_card import CardVictory
from cards.utils.base_card import Cardname
from cards.utils.base_card import Expansion


class Estate(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            description="It produces 1 vp when the game ends.",
            name=Cardname.Estate,
            price=CardCost.TWO,
            type=CardType.VICTORYCARD,
            money=CardMoney.ZERO,
            victory_points=CardVictory.ONE,
            expansion=Expansion.Dominion,
        )


class Duchy(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            description="It produces 3 vp when the game ends.",
            name=Cardname.Duchy,
            price=CardCost.FIVE,
            type=CardType.VICTORYCARD,
            money=CardMoney.ZERO,
            victory_points=CardVictory.THREE,
            expansion=Expansion.Dominion,
        )


class Province(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            description="It produces 6 vp when the game ends.",
            name=Cardname.Province,
            price=CardCost.EIGTH,
            type=CardType.VICTORYCARD,
            money=CardMoney.ZERO,
            victory_points=CardVictory.SIX,
            expansion=Expansion.Dominion,
        )
