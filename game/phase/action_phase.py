from expansions.utils.helper import BoardError, UserInputException, get_user_input
from player.base_player import Player


class ActionPhase:
    @staticmethod
    def play_card(player: Player, number_allowed_actions: int) -> None:
        try:
            while True:
                if number_allowed_actions <= 0:
                    break
                print(
                    "You are in the 'action_phase' input cardname u wanna play, for skip press enter"
                )

                desired_card = get_user_input()
                action_card, error = player.deck.hand_cards.return_card(desired_card)
                if error == BoardError.Empty:
                    action_card(player)
                    player.deck.cards_in_play.card_list.append(action_card)
                    player.deck.hand_cards.discard(action_card)
                    number_allowed_actions -= 1
                else:
                    continue

        except UserInputException:
            pass
