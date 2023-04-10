from __future__ import annotations
import sys
from typing import TYPE_CHECKING
sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from game.phase.action_phase import ActionPhase
from cards.victorycards.card_entitys import Estate

from game.phase.buy_phase import BuyPhase
from game.phase.turn import Turn
from expansions.base_expansion import BaseExpansionField
from player.base_player import Player
from cards.actioncards.card_entitys import Smithy, Village


if TYPE_CHECKING:
    from expansions.utils.field import Field

turn = Turn()        
action_phase = ActionPhase()
buy_phase = BuyPhase()


class Game:
    def __init__(
        self, player_one: Player, player_two: Player, field_cards: Field
    ) -> None:
        self.player_one = player_one
        self.player_two = player_two
        self.field_cards = field_cards

    def start_game(self):

        for player in (self.player_one, self.player_two):
            # start turn
            turn.new_turn()
            turn.start_turn(player)

            # action phase
            if player.deck.hand_cards.player_has_action_cards():
                action_phase.start_action_phase(player, turn)

            # buy phase
            buy_phase.start_buy_phase(player, self.field_cards, turn)

            # end turn
            turn.end_turn(player)


if __name__ == "__main__":
    start_cards = [Village()] * 7 + [Estate()] * 3
    x = Game(
        Player("Norman", start_cards),
        Player("Nico", start_cards),
        BaseExpansionField,
    )
    x.start_game()
