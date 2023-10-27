from __future__ import annotations
from enum import Enum, IntEnum
import sys


sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from typing import TYPE_CHECKING


from cards.utils.base_card import CardCost
from cards.utils.base_card import CardType
from cards.utils.base_card import CardMoney
from cards.utils.base_card import CardVictory
from cards.utils.base_card import Cardname
from cards.utils.base_card import Expansion
from cards.actioncards.action_card import ActionCard, ActionImpacts, ActionInstruction

if TYPE_CHECKING:
    from player.base_player import Player
    from decks.expansions.base_expansion import BaseExpansionField


class SmithyDrawProperties(IntEnum):
    DRAW_THREE = 3


class Smithy(ActionCard):
    def __init__(
        self,
    ):
        super().__init__(
            description="Draw Three Cards",
            name=Cardname.Smithy,
            price=CardCost.FOUR,
            type=CardType.ACTIONCARD,
            money=CardMoney.ZERO,
            victory_points=CardVictory.ZERO,
            expansion=Expansion.Dominion,
            action_instructions=ActionInstruction(
                impact=ActionImpacts.PLAYER,
                player_method="draw",
                properties=SmithyDrawProperties.DRAW_THREE,
            ),
        )

    def execute(self, player: Player, opponent: Player, board: BaseExpansionField):
        getattr(player, self.action_instructions.player_method)(
            self.action_instructions.properties
        )


class MititsDiscardProperty(IntEnum):
    DISCARD_TWO = 2


class Milits(ActionCard):
    def __init__(
        self,
    ):
        super().__init__(
            description="Draw Three Cards",
            name=Cardname.Milits,
            price=CardCost.FOUR,
            type=CardType.ACTIONCARD,
            money=CardMoney.ZERO,
            victory_points=CardVictory.ZERO,
            expansion=Expansion.Dominion,
            action_instructions=ActionInstruction(
                impact=ActionImpacts.OPPONENTS,
                player_method="discard_spectific_card",
                properties=MititsDiscardProperty.DISCARD_TWO,
            ),
        )

    def execute(self, player: Player, opponent: Player, board: BaseExpansionField):
        getattr(opponent, self.action_instructions.player_method)(
            self.action_instructions.properties
        )
