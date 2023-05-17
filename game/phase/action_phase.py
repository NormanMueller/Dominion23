from __future__ import annotations
from typing import TYPE_CHECKING

from expansions.utils.helper import BoardError, UserInputException, get_user_input

if TYPE_CHECKING:
    from game.phase.turn import Turn
    from player.base_player import Player


class ActionPhase:
    @staticmethod
    def start_action_phase(player: Player, turn: Turn) -> None:
        try:
            while True:
                if turn.Actions <= 0:
                    break
                print(
                    "You are in the 'action_phase' input cardname u wanna play, for skip press enter"
                )

                desired_card = get_user_input()
                action_card, error = player.deck.hand_cards.return_card(desired_card)
                
                if error == BoardError.Empty:
                    player.deck.cards_in_play.card_list.append(action_card)
                    player.deck.hand_cards.discard(action_card)
                    action_card(player, turn)
                    turn.Actions -= 1
                else:
                    continue

        except UserInputException:
            pass
