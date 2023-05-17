import sys

from expansions.utils.helper import BoardError, get_user_input
sys.path.append(r"c:\Users\norma\Github\Dominion2023")
from typing import List
from player.player_deck_of_cards import PlayerCardDeck
from cards.utils.base_card import BaseCard


class Player:
    def __init__(self, name: str, start_deck: List[BaseCard]) -> None:
        self.name = name
        self.deck = PlayerCardDeck(start_deck)
    
