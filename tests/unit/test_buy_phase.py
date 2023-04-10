import unittest.mock
from cards.treasurecards.card_entitys import Silver
from expansions.base_expansion import BaseExpansionField

from game.phase.buy_phase import BuyPhase
from game.phase.turn import Turn
from player.base_player import Player


def test_calculate_available_money(player_with_copper: Player):
    # GIVEN
    buy_phase = BuyPhase()
    player_with_copper.deck.draw(5)
    # WHEN
    return_value = buy_phase.calculate_available_money(player_with_copper)
    # THEN
    assert return_value == 5


def test_start_buy_phase(player_with_copper: Player):
    # GIVEN
    buy_phase = BuyPhase()
    player_with_copper.deck.draw(5)

    with unittest.mock.patch("builtins.input", return_value="Silver"):
        # WHEN
        buy_phase.start_buy_phase(player_with_copper, BaseExpansionField(), Turn())
    # THEN
    assert player_with_copper.deck.discard_pile.card_list == [Silver()] * 1
