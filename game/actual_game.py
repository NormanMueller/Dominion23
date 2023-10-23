from __future__ import annotations
import sys
from typing import TYPE_CHECKING

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from game.phase_handler import PhaseHandler

from cards.victorycards.card_entitys import Estate
from cards.actioncards.card_entitys import Milits, Smithy
from decks import decks
from decks.expansions.base_expansion import BaseExpansionField

from player.base_player import Player

NUMBER_OF_PLAYER = 2


class Game:
    def __init__(
        self, player_one: Player, player_two: Player, field_cards: decks
    ) -> None:
        self.player_one = player_one
        self.player_two = player_two
        self.field_cards = field_cards

    def start_game(self):
        phasen_handler = PhaseHandler(
            self.player_one, self.player_two, self.field_cards
        )

        phasen_handler.intilize_all_phase()
        while True:
            phasen_handler.handle_turn()
            phasen_handler.swap_start_player()


if __name__ == "__main__":
    start_cards = [Milits()] * 7 + [Estate()] * 3
    x = Game(
        Player("Norman", start_cards),
        Player("Nico", start_cards),
        BaseExpansionField(),
    )
    x.start_game()
