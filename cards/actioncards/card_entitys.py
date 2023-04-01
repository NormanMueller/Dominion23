import sys

from player.base_player import Player

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from cards.utils.base_card import CardCost
from cards.utils.base_card import CardType
from cards.utils.base_card import CardMoney
from cards.utils.base_card import CardVictory
from cards.utils.base_card import CardBuys
from cards.utils.base_card import Cardname
from cards.utils.base_card import Expansion
from cards.actioncards.action_card import ActionCard, Draws, Discards, Deletes
from cards.utils.base_card import BaseCard


class Smithy(ActionCard):
    def __init__(
        self,
    ):
        super().__init__(
            Cardname.Smithy,
            CardCost.FOUR,
            CardType.ACTIONCARD,
            CardMoney.ZERO,
            CardVictory.ZERO,
            CardBuys.ZERO,
            Expansion.Dominion,
            Draws.THREE,
        )

    def __call__(self, player: Player):
        player.deck.draw(self.DRAWS)
