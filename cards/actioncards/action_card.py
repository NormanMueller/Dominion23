from __future__ import annotations
from typing import TYPE_CHECKING, List
from dataclasses import dataclass
from enum import Enum, IntFlag
from sre_constants import ANY
import sys
from typing import Any
from typing import Literal
from typing import TYPE_CHECKING


sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from cards.utils.base_card import (
    BaseCard,
)
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from player.base_player import Player
    from decks.expansions.base_expansion import BaseExpansionField


player_methods = Literal[
    "draw", "discard_all_hand_cards", "discard_spectific_card"
]  # must be a method player can perform


class AdditionalActions(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class AdditionalBuys(IntFlag):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3


class ActionImpacts(Enum):
    PLAYER = "PLAYER"
    OPPONENTS = "OPPONENTS"


@dataclass
class ActionInstruction:
    impact: ActionImpacts
    player_method: player_methods
    properties: ANY


@dataclass
class ActionCard(BaseCard):
    # standard actions, add Buys and Actions
    action_instructions: List[ActionInstruction] | ActionInstruction
    additional_actions: AdditionalActions = AdditionalActions.ZERO
    additional_buys: AdditionalBuys = AdditionalBuys.ZERO

    @abstractmethod
    def execute(
        self, player: Player, opponent: Player, board: BaseExpansionField
    ) -> None:
        ...
