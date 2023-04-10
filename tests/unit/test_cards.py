import sys
from cards.actioncards.card_entitys import Smithy

from cards.utils.base_card import (
    CardCost,
    CardMoney,
    CardType,
    CardVictory,
    Cardname,
    Expansion,
)
from cards.actioncards.action_card import ActionCard, Draws
from cards.victorycards.card_entitys import Estate
from game.phase.turn import Turn
from player.base_player import Player


def test_action_card(action_card_standard: ActionCard):
    # GIVEN
    # When
    # Then
    assert action_card_standard.DISCARDS == 0
    assert action_card_standard.DELETES == 0
    assert action_card_standard.DRAWS == 0


def test_smithy(action_card_standard: ActionCard):
    # GIVEN
    smithy = Smithy()
    player = Player("norm", [Estate] * 3)
    # When
    smithy(player,Turn())
    # Then
    assert action_card_standard.DISCARDS == 0
    assert action_card_standard.DELETES == 0
    assert action_card_standard.DRAWS == 0
