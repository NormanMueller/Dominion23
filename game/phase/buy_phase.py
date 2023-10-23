from __future__ import annotations
from dataclasses import dataclass
import sys
from typing import TYPE_CHECKING


sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from game.phase.base_phase import BasePhase
from utils.exceptions import UserInputException
from utils.helper import phasen_decorator, player_phasen_information, user_input_handler

if TYPE_CHECKING:
    from player.base_player import Player
    from decks.decks import CardDeck


@dataclass
class BuyPhase(BasePhase):
    player: Player
    opponent: Player
    field_cards: CardDeck

    def condition_to_play(self) -> None:
        if self.player.nr_buys <= 0:
            return False
        return True

    @phasen_decorator
    def start_phase(self) -> None:
        while self.condition_to_play() == True:
            player_phasen_information(self.player)
            card_from_field, error = user_input_handler(self.field_cards)
            if error == UserInputException:
                break

            if self.player.available_money >= card_from_field.price:
                self.player.buy_card(card_from_field)
                self.player.nr_buys -= 1
            else:
                print(f"not enough money to buy  choose new card")
