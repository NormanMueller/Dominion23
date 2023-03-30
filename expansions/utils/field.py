import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from dataclasses import asdict, dataclass, fields
from typing import TYPE_CHECKING, Tuple
from cards.utils.base_card import BaseCard
from expansions.utils.helper import BoardError


@dataclass
class Field:
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    @classmethod
    def return_fieldcard(
        self, desired_card: BaseCard
    ) -> Tuple[BaseCard | None, BoardError | None]:
        try:
            desired_card = self.__dict__[desired_card]
            if desired_card.QUANTITY > 0:
                return desired_card, BoardError.Empty
            else:
                print("Card is no longer available")
                return None, BoardError.NotAvailable

        except (ValueError, KeyError) as e:
            print(f"no match for {desired_card}")
            return None, BoardError.NoMatch
