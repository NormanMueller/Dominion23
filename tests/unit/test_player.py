from cards.treasurecards.card_entitys import Copper
from player.player_deck import PlayerCardDeck


def test_draw():
    # GIVEN
    start_cards = [Copper()] * 5
    card_deck = PlayerCardDeck(start_cards)
    # WHEN
    card_deck.draw(5)
    # THEN
    assert card_deck.hand_cards.card_list == start_cards


def test_end_of_turn():
    # GIVEN
    start_cards = [Copper()] * 5
    card_deck = PlayerCardDeck(start_cards)
    # WHEN
    card_deck.draw(5)
    card_deck.end_of_turn()
    # THEN
    assert card_deck.hand_cards.card_list == []
    assert card_deck.discard_pile.card_list == start_cards
