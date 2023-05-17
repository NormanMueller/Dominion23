import sys
import copy
from typing import List
from decks.decks import (
    DiscardPile,
    DrawCardDeck,
    HandCardDeck,
    InPlayCardDeck,
)
from expansions.utils.helper import BoardError, UserInputException, get_user_input

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

    def discard_multiple_handcards(self, nr = 99):
        list_of_cards = []
        iteration = 0 
        try:
            while True and nr > iteration  :
                desired_card = get_user_input()
                card, error = self.hand_cards.return_card(desired_card)     
                if error == BoardError.Empty:
                    self.hand_cards.discard(card)
                    list_of_cards.append(card)
                else:
                    continue
        except UserInputException:
            return list_of_cards
        
        return list_of_cards