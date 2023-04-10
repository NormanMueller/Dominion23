import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from attr import dataclass
from cards.actioncards.action_card import Actions, Buys
from player.base_player import Player


@dataclass
class TurnProperties:
    Actions: Actions = Actions.ONE
    Buys: Buys = Buys.ONE


class Turn(TurnProperties):
    def __init__(self,):
        super().__init__()

    @staticmethod
    def start_turn(player: Player) -> None:
        player.deck.draw(nr=5)

    @staticmethod
    def end_turn(player: Player) -> None:
        player.deck.end_of_turn()

    def new_turn(self):
        self.Actions = Actions.ONE
        self.Buys  = Buys.ONE

    def add_actions(self, nr: int) -> None:
        self.Actions += nr

    def add_buys(self, nr: int) -> None:
        self.Buys += nr

x = Turn()
print(x.Actions)
