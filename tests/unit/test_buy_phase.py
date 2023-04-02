import unittest.mock
from cards.treasurecards.card_entitys import Silver
from expansions.base_expansion import BaseExpansionField

from game.phase.buy_phase import BuyPhase


def test_calculate_available_money(player_with_copper):
    # GIVEN
    buy_phase = BuyPhase()
    player_with_copper.deck.draw(5)
    # WHEN
    return_value = buy_phase.calculate_available_money(player_with_copper)
    # THEN
    assert return_value == 5


def test_buy_card(player_with_copper):
    # GIVEN
    buy_phase = BuyPhase()
    player_with_copper.deck.draw(5)

    with unittest.mock.patch("builtins.input", return_value="Silver"):
        # WHEN
        buy_phase.buy_card(player_with_copper, BaseExpansionField(), 1)
    # THEN
    assert player_with_copper.deck.discard_pile.card_list == [Silver()] * 1
