from __future__ import annotations

import sys

from utils.helper import phasen_decorator

sys.path.append(r"c:\Users\norma\Github\Dominion2023")


from attr import dataclass
from player.base_player import Player


@dataclass
class ClosingPhase:
    player: Player
    opponent: Player

    def condition_to_play():
        ...
    
    def start_phase(self):
        self.player.discard_all_hand_cards()
