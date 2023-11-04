from dataclasses import dataclass, field
from random import shuffle

from typing import List, Tuple
from cards.utils.card_creator import CardCreator
from decks.helper import draw_generator
from utils.exceptions import HandErrorNoMatch
from tabulate import tabulate
from dataclasses_json import LetterCase, dataclass_json, config

from cards.utils.base_card import BaseCard

@dataclass(kw_only=True)
class CardDeck:
    card_list : List[BaseCard]
    card_creator: CardCreator = CardCreator()
    i:int = 0
    
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
        if [card for card in self.card_list if str(card.name) == desired_card]:
            return self.card_creator.make_instance(desired_card)
        
        raise HandErrorNoMatch

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

class DrawCardDeck(CardDeck):
    def __init__(self, card_list : List[BaseCard]):
        self.card_list = card_list
        shuffle(self.card_list)


class DiscardPile(CardDeck):
    ...


class InPlayCardDeck(CardDeck):
    ...

class HandCardDeck(CardDeck):
    def __str__(self) -> str:
        return tabulate(
            [(card.name, card.type, card.description) for card in self.card_list],
            headers=["Name", "Type", "Description"],
        )
