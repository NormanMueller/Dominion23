import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from phase.action_phase import ActionPhase
from cards.treasurecards.card_entitys import Copper
from cards.victorycards.card_entitys import Estate
from expansions.utils.field import Field
from player.base_player import Player
from expansions.base_expansion import BaseExpansionField
from phase.buy_phase import BuyPhase

from cards.actioncards.card_entitys import Smithy


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
            player.deck.draw(nr=5)

            # action phase
            if player.deck.hand_cards.player_has_action_cards():
                action_phase = ActionPhase()
                action_phase.play_card(player, 1)

            # buy phase
            buy_phase = BuyPhase()
            buy_phase.buy_card(player, self.field_cards, 1)

            # end turn
            player.deck.end_of_turn()


if __name__ == "__main__":
    start_cards = [Smithy()] * 7 + [Estate()] * 3
    x = Game(
        Player("Norman", start_cards),
        Player("Nico", start_cards),
        BaseExpansionField,
    )
    x.start_game()
