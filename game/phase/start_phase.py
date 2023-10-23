from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from utils.helper import phasen_decorator

sys.path.append(r"c:\Users\norma\Github\Dominion2023")


from attr import dataclass

if TYPE_CHECKING:
    from player.base_player import Player

NUMBER_START_CARDS = 5
NUMBER_START_ACTIONS = 1
NUMBER_START_BUYS = 1


@dataclass
class StartPhase:
    player: Player
    opponent: Player

    def condition_to_play():
        ...
   
    def start_phase(self) -> None:
        self.player.draw(nr=NUMBER_START_CARDS)
        self.player.nr_buys = NUMBER_START_BUYS
        self.player.nr_actions = NUMBER_START_ACTIONS

    def opponent_start_phase(self) -> None:
        self.opponent.draw(nr=NUMBER_START_CARDS)
        self.opponent.nr_buys = NUMBER_START_BUYS
        self.opponent.nr_actions = NUMBER_START_ACTIONS