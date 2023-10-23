from dataclasses import dataclass
import sys
import copy

from utils.helper import user_input_handler

sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from typing import List
from decks.decks import (
    DiscardPile,
    DrawCardDeck,
    HandCardDeck,
    InPlayCardDeck,
)

from cards.utils.base_card import BaseCard


class PlayerCardDeck:
    def __init__(self, deck) -> None:
        self.draw_pile: DrawCardDeck = DrawCardDeck(deck)
        self.hand_cards: HandCardDeck = HandCardDeck([])
        self.discard_pile: DiscardPile = DiscardPile([])
        self.cards_in_play: InPlayCardDeck = InPlayCardDeck([])

    @property
    def overall_cards(self) -> int:
        return len(
            self.draw_pile + self.hand_cards + self.discard_pile + self.cards_in_play
        )
