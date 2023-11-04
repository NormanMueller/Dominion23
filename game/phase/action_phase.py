from __future__ import annotations
import sys


sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from game.phase.base_phase import BasePhase
from cards.actioncards.action_card import ActionCard, ActionImpacts

from typing import TYPE_CHECKING

from attr import dataclass
from player.base_player import Player

from utils.exceptions import UserSkipPhaseException
from utils.helper import phasen_decorator, player_phasen_information, user_input_handler


if TYPE_CHECKING:
    from decks.decks import CardDeck


@dataclass
class ActionPhase(BasePhase):
    player: Player
    opponent: Player
    field_cards: CardDeck

    def condition_to_play(self) -> None:
        if self.player.action_cards_in_hand == False or self.player.nr_actions <= 0:
            return False
        return True

    @phasen_decorator
    def start_phase(self) -> None:
        while self.condition_to_play() == True:
            player_phasen_information(self.player)
            action_card_to_play, error = user_input_handler(self.player.deck.hand_cards)
            if error == UserSkipPhaseException:
                break

            self.player.play_card(action_card_to_play)
            action_card_to_play: ActionCard
            action_card_to_play.execute(self.player, self.opponent, self.field_cards)

            self.player.nr_actions -= 1
