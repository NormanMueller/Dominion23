import pytest
from cards.actioncards.card_entitys import Smithy
from cards.treasurecards.card_entitys import Copper
from cards.victorycards.card_entitys import Estate
from expansions.utils.helper import BoardError


def test_return_card(empty_deck, card_copper):
    # GIVEN
    empty_deck.card_list = [Copper()] * 1
    # WHEN
    returned_card, error = empty_deck.return_card("Copper")
    # THEN
    assert returned_card == card_copper
    assert error == BoardError.Empty


def test_return_card_nomatch(empty_deck, card_copper):
    # GIVEN
    # WHEN
    returned_card, error = empty_deck.return_card("Copper")
    # THEN
    assert returned_card == None
    assert error == BoardError.NoMatch


def test_add(empty_deck, card_copper):
    # GIVEN
    # WHEN
    empty_deck.add(card_copper)
    # THEN
    assert empty_deck.card_list == [card_copper]


def test_discard(empty_deck, card_copper):
    # GIVEN
    empty_deck.card_list = [card_copper] * 1
    # WHEN
    empty_deck.discard(card_copper)
    # THEN
    assert empty_deck.card_list == []


@pytest.mark.parametrize(
    "hand_cards",
    [[Copper(), Copper(), Copper()], [Estate(), Estate(), Estate()], []],
)
def test_has_no_action_card(empty_hand_card_deck, hand_cards):
    # GIVEN
    empty_hand_card_deck.card_list = hand_cards
    # WHEN
    return_value = empty_hand_card_deck.player_has_action_cards()
    # THEN
    assert return_value == False


@pytest.mark.parametrize(
    "hand_cards",
    [
        [Smithy(), Copper(), Copper()],
        [Estate(), Smithy(), Estate()],
        [Estate(), Smithy(), Smithy()],
    ],
)
def test_has_action_card(empty_hand_card_deck, hand_cards):
    # GIVEN
    empty_hand_card_deck.card_list = hand_cards
    # WHEN
    return_value = empty_hand_card_deck.player_has_action_cards()
    # THEN
    assert return_value == True
