import sys

sys.path.append(r"c:\Users\norma\Github\Dominion2023")

from cards.actioncards.card_entitys import Smithy
from cards.treasurecards.card_entitys import Copper
from decks.decks import CardDeck, HandCardDeck
from expansions.base_expansion import BaseExpansionField
import pytest
from cards.utils.base_card import (
    BaseCard,
    CardBuys,
    CardCost,
    CardMoney,
    CardType,
    CardVictory,
    Cardname,
    Expansion,
)
from cards.actioncards.action_card import ActionCard, Draws
from player.base_player import Player


@pytest.fixture
def action_card_standard() -> ActionCard:
    return ActionCard(
        Cardname.Smithy,
        CardCost.FOUR,
        CardType.ACTIONCARD,
        CardMoney.ZERO,
        CardVictory.ZERO,
        CardBuys.ZERO,
        Expansion.Dominion,
    )


@pytest.fixture
def base_expansion_field() -> BaseExpansionField:
    return BaseExpansionField()


@pytest.fixture
def card_copper() -> Copper:
    return Copper()


@pytest.fixture
def empty_deck() -> CardDeck:
    return CardDeck([])


@pytest.fixture
def empty_hand_card_deck() -> HandCardDeck:
    return HandCardDeck([])


@pytest.fixture
def hand_cards() -> BaseCard:
    return []


@pytest.fixture
def player_with_smithy() -> Player:
    return Player("Norman", [Smithy()] * 10)


@pytest.fixture
def player_with_copper() -> Player:
    return Player("Norman", [Copper()] * 10)


@pytest.fixture(scope="function")
def base_expansion() -> CardDeck:
    return BaseExpansionField()
