import unittest.mock
from cards.actioncards.card_entitys import Smithy

from game.phase.action_phase import ActionPhase
from game.phase.start_phase import Turn


def test_start_action_phase(player_with_smithy):
    # GIVEN
    with unittest.mock.patch("builtins.input", return_value="Smithy"):
        # player_with_smithy
        action_phase = ActionPhase()
        player_with_smithy.deck.draw(5)
        # WHEN
        action_phase.start_action_phase(player_with_smithy, Turn())
    # THEN
    assert player_with_smithy.deck.hand_cards.card_list == [Smithy()] * 7
    assert player_with_smithy.deck.cards_in_play.card_list == [Smithy()]
