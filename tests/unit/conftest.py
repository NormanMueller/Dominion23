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
