import sys

import unittest.mock
from pytest_bdd import given, parsers, scenario, then, when
from game.actual_game import Game, ActionPhase, Player, Turn


@given(parsers.parse("Card is {default_card}"), target_fixture="card")
def card_return(default_card, base_expansion):
    card, error = base_expansion.return_fieldcard(default_card)
    return card


@given(parsers.parse("Player with {default_card}"), target_fixture="player")
def player_with_cards(default_card, card):
    start_deck = [card] * 10
    player = Player("test", start_deck)
    player.deck.draw(5)

    return player

@when(parsers.parse("ActionPhase {default_card} is played"), target_fixture="player")
def action_phase(default_card, player):
    if player.deck.hand_cards.player_has_action_cards() == False:
        return player

    with unittest.mock.patch("builtins.input", return_value=default_card):
        action_phase = ActionPhase()
        action_phase.play_card(player, Turn())
        return player


@then(parsers.parse("{default_card} card is in cards_in_play pile {bool_value}"))
def after_action_phase(bool_value, card, player):
    if bool_value:
        assert card in player.deck.cards_in_play.card_list
        return

    if bool_value == False:
        assert card not in player.deck.cards_in_play.card_list
