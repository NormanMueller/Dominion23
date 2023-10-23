import sys
from typing import List, Tuple
from cards.utils.card_creator import CardCreator
from decks.helper import draw_generator
from utils.exceptions import HandErrorNoMatch
from tabulate import tabulate

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from cards.utils.base_card import BaseCard


class CardDeck:
    def __init__(self, card_list: List[BaseCard]) -> None:
        self.card_list = card_list

    card_creator: CardCreator = CardCreator()

    def __iter__(self):
        return self.RangeIterator(self.card_list)

    class RangeIterator:
        def __init__(self, card_list: List[BaseCard]):
            self.i = 0
            self.card_list = card_list

        def __iter__(self):
            return self

        def __next__(self):
            self.i += 1
            if self.i < len(self.card_list):
                return self.card_list[self.i]
            else:
                raise StopIteration()

    def __contains__(self, desired_card):
        return True if desired_card in self.card_list else False

    def get_instance_of_card(self, desired_card) -> BaseCard:
        if [card for card in self.card_list if card.name == desired_card]:
            raise HandErrorNoMatch
        return self.card_creator.make_instance(desired_card)

    def remove_card(self, card: BaseCard | List[BaseCard]) -> None:
        if isinstance(card, list):
            [self.card_list.remove(entity) for entity in card]

        elif isinstance(card, BaseCard):
            self.card_list.remove(card)

    def add_card(self, card: BaseCard) -> None:
        if isinstance(card, list):
            [self.card_list.append(entity) for entity in card]

        elif isinstance(card, BaseCard):
            self.card_list.append(card)


class DiscardPile(CardDeck):
    def __init__(self, card_list: List[BaseCard]) -> None:
        super().__init__(card_list)


class DrawCardDeck(CardDeck):
    def __init__(self, card_list: List[BaseCard]) -> None:
        super().__init__(draw_generator(card_list))


class HandCardDeck(CardDeck):
    def __init__(self, card_list: List[BaseCard]) -> None:
        super().__init__(card_list)

    def __str__(self) -> str:
        return tabulate(
            [(card.name, card.type, card.description) for card in self.card_list],
            headers=["Name", "Type", "Description"],
        )


class InPlayCardDeck(CardDeck):
    def __init__(self, card_list: List[BaseCard]) -> None:
        super().__init__(card_list)
