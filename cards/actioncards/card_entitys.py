from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from player.base_player import Player

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from cards.utils.base_card import CardCost
from cards.utils.base_card import CardType
from cards.utils.base_card import CardMoney
from cards.utils.base_card import CardVictory
from cards.utils.base_card import Cardname
from cards.utils.base_card import Expansion
from cards.actioncards.action_card import ActionCard, Actions, Draws, Discards, Deletes

if TYPE_CHECKING:
    from game.phase.turn import Turn


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
            Expansion.Dominion,
            Draws.THREE,
        )

    def __call__(self, player: Player, turn: Turn):
        player.deck.draw(self.DRAWS)


class Village(ActionCard):
    def __init__(
        self,
    ):
        super().__init__(
            Cardname.Village,
            CardCost.THREE,
            CardType.ACTIONCARD,
            CardMoney.ZERO,
            CardVictory.ZERO,
            Expansion.Dominion,
            Draws.ONE,
            Actions.TWO,
        )

    def __call__(self, player: Player, turn: Turn):
        player.deck.draw(self.DRAWS)
        turn.add_actions(nr=2)
