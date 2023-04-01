import sys
from typing import List, Tuple

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
import random
from cards.utils.base_card import BaseCard, Cardname
from expansions.utils.field import BoardError
from cards.utils.base_card import CardType


class CardDeck:
    def __init__(self, card_list: List[BaseCard]) -> None:
        self.card_list = card_list

    def return_card(
        self, desired_card: str
    ) -> Tuple[BaseCard | None, BoardError | None]:
        try:
            desired_card = [
                card for card in self.card_list if card.NAME == Cardname[desired_card]
            ]
            return desired_card[0], BoardError.Empty
        except:
            print(f"{BoardError.NoMatch}  for {desired_card}")
            return None, BoardError.NoMatch

    def discard(self, card: BaseCard) -> None:
        self.card_list.remove(card)

    def add(self, card: BaseCard) -> None:
        self.card_list.append(card)


class DiscardPile(CardDeck):
    def __init__(self, card_list: List[BaseCard]) -> None:
        super().__init__(card_list)


class DrawCardDeck(CardDeck):
    def __init__(self, card_list: List[BaseCard]) -> None:
        super().__init__(self.draw_generator(card_list))

    def draw_generator(self, card_list) -> BaseCard:
        random.shuffle(card_list)
        for card in card_list:
            yield card


class HandCardDeck(CardDeck):
    def __init__(self, card_list: List[BaseCard]) -> None:
        super().__init__(card_list)

    def player_has_action_cards(self) -> bool:
        action_cards = [
            card for card in self.card_list if card.TYPE == CardType.ACTIONCARD
        ]
        if action_cards:
            return True
        else:
            return False


class InPlayCardDeck(CardDeck):
    def __init__(self, card_list: List[BaseCard]) -> None:
        super().__init__(card_list)
