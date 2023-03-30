from expansions.utils.helper import UserInputException, get_user_input
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
                if error == None:
                    action_card(player)
                    number_allowed_actions -= 1
                else:
                    continue
        
        except UserInputException:
            pass
