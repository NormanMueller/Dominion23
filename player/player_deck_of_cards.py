import sys
import copy
from typing import List
from decks.decks import (
    DiscardPile,
    DrawCardDeck,
    HandCardDeck,
    InPlayCardDeck,
)

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from cards.utils.base_card import BaseCard


class PlayerCardDeck:
    def __init__(self, start_cards: List[BaseCard]) -> None:
        self.hand_cards: HandCardDeck = HandCardDeck([])
        self.draw_pile: DrawCardDeck = DrawCardDeck(start_cards)
        self.discard_pile: DiscardPile = DiscardPile([])
        self.cards_in_play: InPlayCardDeck = InPlayCardDeck([])

    def draw(self, nr: int) -> None:
        for _ in range(nr):
            try:
                self.hand_cards.card_list.append(next(self.draw_pile.card_list))
            except StopIteration:
                self.draw_pile = DrawCardDeck(self.discard_pile.card_list)
                self.hand_cards.card_list.append(next(self.draw_pile.card_list))

    def end_of_turn(self):
        copy_cards = copy.copy(self.hand_cards.card_list)
        for card in copy_cards:
            self.hand_cards.discard(card)
            self.discard_pile.add(card)
