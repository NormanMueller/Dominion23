from dataclasses import asdict, astuple, dataclass, fields
import sys
from typing import List

from tabulate import tabulate

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from decks.decks import CardDeck

from cards.treasurecards.card_entitys import Copper, Gold, Silver
from cards.victorycards.card_entitys import Estate, Duchy, Province
from cards.actioncards.card_entitys import Smithy


@dataclass
class BaseExpansionField(CardDeck):
    def __init__(self) -> None:
        super().__init__(card_list=
            [
                Copper(),
                Silver(),
                Gold(),
                Estate(),
                Duchy(),
                Province(),
                Smithy(),
            ]
        )

    def __str__(self) -> str:
        return tabulate(
            [
                (card.name, card.type, card.price, card.quantity, card.description)
                for card in self.card_list
            ],
            headers=["Name", "Type", "Price", "Quantity", "Description"],
        )
