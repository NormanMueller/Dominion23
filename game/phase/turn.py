import copy
import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from attr import dataclass
from cards.actioncards.action_card import Actions, Buys
from player.base_player import Player


@dataclass
class TurnProperties:
    Actions: Actions = Actions.ONE
    Buys: Buys = Buys.ONE

    def new_turn(self):
        self.Actions = Actions.ONE
        self.Buys  = Buys.ONE

    def add_actions(self, nr: int) -> None:
        self.Actions += nr

    def add_buys(self, nr: int) -> None:
        self.Buys += nr


class Turn(TurnProperties):
    def __init__(self,):
        super().__init__()

    @staticmethod
    def start_turn(player: Player) -> None:
        player.deck.draw(nr=5)


    @staticmethod
    def end_turn(player: Player):
        copy_cards = copy.copy(player.deck.hand_cards.card_list)
        for card in copy_cards:
            player.deck.hand_cards.discard(card)
            player.deck.discard_pile.add(card)
    

