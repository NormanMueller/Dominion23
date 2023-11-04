import sys



sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from dataclasses import asdict, dataclass

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
        self.draw_pile: DrawCardDeck = DrawCardDeck(card_list=deck)
        self.hand_cards: HandCardDeck = HandCardDeck(card_list=[])
        self.discard_pile: DiscardPile = DiscardPile(card_list=[])
        self.cards_in_play: InPlayCardDeck = InPlayCardDeck(card_list=[])

    @property
    def overall_cards(self) -> int:
        return len(
            self.draw_pile + self.hand_cards + self.discard_pile + self.cards_in_play
        )


    def logger(self):
        log_dict ={}
        for name, value  in self.__dict__.items():
            log_dict[name] = value.card_list
        return log_dict