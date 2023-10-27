from __future__ import annotations
from copy import copy
import itertools
import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from decks.decks import DrawCardDeck
from utils.exceptions import UserSkipPhaseException
from utils.helper import user_input_handler


from typing import TYPE_CHECKING, List
from player.player_deck import PlayerCardDeck
from cards.utils.base_card import CardType

if TYPE_CHECKING:
    from cards.utils.base_card import BaseCard


class Player:
    def __init__(self, name: str, start_deck: List[BaseCard]) -> None:
        self.name = name
        self.deck = PlayerCardDeck(start_deck)
        self.nr_actions: int = 0
        self.nr_buys: int = 0

    @property
    def available_money(self):
        overall_money = 0
        for card in itertools.chain(self.deck.hand_cards, self.deck.cards_in_play):
            overall_money += card.money

        return overall_money

    @property
    def action_cards_in_hand(self) -> bool:
        action_cards = [
            card for card in self.deck.hand_cards if card.type == CardType.ACTIONCARD
        ]
        result = True if action_cards else False
        return result

    def add_action(self, nr: int) -> int:
        self.nr_actions += nr

    def add_buy(self, nr: int) -> int:
        self.nr_buys += nr

    def play_card(self, action_card) -> None:
        self.deck.cards_in_play.add_card(action_card)
        self.deck.hand_cards.remove_card(action_card)

    def buy_card(self, card_from_field) -> None:
        self.deck.discard_pile.add_card(card_from_field)

    def draw(self, nr: int) -> None:
        for _ in range(nr):
            try:
                self.deck.hand_cards.add_card(next(self.deck.draw_pile.card_list))
            except StopIteration:
                self.deck.draw_pile = DrawCardDeck(self.deck.discard_pile.card_list)
                self.deck.hand_cards.add_card(next(self.deck.draw_pile.card_list))

    def discard_all_hand_cards(self) -> None:
        copy_cards = copy(self.deck.hand_cards.card_list)
        self.deck.hand_cards.remove_card(copy_cards)
        self.deck.discard_pile.add_card(copy_cards)

    def discard_spectific_card(self, number_of_discards) -> None:
        iteration = 0
        while number_of_discards > iteration:
            card_user_wants_to_discard, error = user_input_handler(self.deck.hand_cards)
            if error == UserSkipPhaseException:
                raise

            self.deck.hand_cards.remove_card(card_user_wants_to_discard)
            iteration += 1
