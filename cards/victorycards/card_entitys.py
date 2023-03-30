import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from cards.utils.base_card import BaseCard, CardCost
from cards.utils.base_card import CardType
from cards.utils.base_card import CardMoney
from cards.utils.base_card import CardVictory
from cards.utils.base_card import CardBuys
from cards.utils.base_card import Cardname
from cards.utils.base_card import Expansion


class Estate(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            Cardname.Estate,
            CardCost.TWO,
            CardType.VICTORYCARD,
            CardMoney.ZERO,
            CardVictory.ONE,
            CardBuys.ZERO,
            Expansion.Dominion,
        )


class Duchy(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            Cardname.Duchy,
            CardCost.FIVE,
            CardType.VICTORYCARD,
            CardMoney.ZERO,
            CardVictory.THREE,
            CardBuys.ZERO,
            Expansion.Dominion,
        )


class Province(BaseCard):
    def __init__(
        self,
    ):
        super().__init__(
            Cardname.Province,
            CardCost.EIGTH,
            CardType.VICTORYCARD,
            CardMoney.ZERO,
            CardVictory.EIGHT,
            CardBuys.ZERO,
            Expansion.Dominion,
        )
