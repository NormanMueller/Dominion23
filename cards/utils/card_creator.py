from __future__ import annotations

import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from typing import TYPE_CHECKING
from cards.actioncards.card_entitys import Milits, Smithy
from cards.treasurecards.card_entitys import Copper, Gold, Silver

from cards.victorycards.card_entitys import Duchy, Estate, Province

if TYPE_CHECKING:
    from cards.utils.base_card import BaseCard


class CardCreator:
    @staticmethod
    def make_instance(card: str) -> BaseCard:
        if card == "Copper":
            return Copper()
        elif card == "Silver":
            return Silver()
        elif card == "Gold":
            return Gold()
        elif card == "Estate":
            return Estate()
        elif card == "Duchy":
            return Duchy()
        elif card == "Province":
            return Province()
        elif card == "Smithy":
            return Smithy()
        elif card == "Milits":
            return Milits()
