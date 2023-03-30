import sys
from typing import List

sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from player.player_deck_of_cards import PlayerCardDeck
from cards.utils.base_card import BaseCard


class Player:
    def __init__(self, name: str, start_deck: List[BaseCard]) -> None:
        self.name = name
        self.deck = PlayerCardDeck(start_deck)
