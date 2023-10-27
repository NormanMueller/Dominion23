from typing import Tuple

from pydantic_core import PydanticCustomError
from cards.utils.base_card import BaseCard, Cardname
from decks.decks import CardDeck
from utils.exceptions import (
    BoardErrorEmpty,
    UserInputCardValidationError,
    UserSkipPhaseException,
)
from pydantic import BaseModel, ValidationError, field_validator


class UserInput(BaseModel):
    cardname: str

    @field_validator("cardname")
    def cardname_must_be_valid_cardname(cls, v):
        allowed_cardnames = Cardname._member_names_
        if v not in allowed_cardnames:
            raise UserInputCardValidationError(
                'value is not "allowed cardname", got "{v}"'
            )
        return v


def get_user_input(txt: str = "Name Card") -> str:
    user_input = input(txt)

    if len(user_input.strip()) > 0:
        return UserInput(cardname=user_input).cardname

    else:
        raise UserSkipPhaseException


def user_input_handler(
    deck: CardDeck,
) -> Tuple[None | BaseCard, None | UserSkipPhaseException]:
    while True:
        try:
            print(deck)
            user_input = get_user_input()
            card_from_deck = deck.get_instance_of_card(user_input)
            return card_from_deck, None

        except UserSkipPhaseException as e:
            print(e.message)
            return None, UserSkipPhaseException

        except BoardErrorEmpty as e:
            print(e.message)

        except UserInputCardValidationError as e:
            # "Pydantic validation error"
            print(e)


def phasen_decorator(phase):
    def _(*args, **kwargs):
        print(f"{args[0].__class__.__name__} starts for Player {args[0].player.name}")

        phase(*args, **kwargs)

        print(f"{args[0].__class__.__name__} ends for Player {args[0].player.name}")

    return _


def player_phasen_information(player):
    print(
        f"{player.name} you have actions: {player.nr_actions} and buys: {player.nr_buys} "
    )
