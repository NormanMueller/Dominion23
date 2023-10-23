import random

from cards.utils.base_card import BaseCard


def draw_generator(card_list) -> BaseCard:
    random.shuffle(card_list)
    for card in card_list:
        yield card
