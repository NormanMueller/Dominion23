from typing import Tuple
from cards.utils.base_card import BaseCard
from decks.decks import CardDeck
from utils.exceptions import BoardErrorEmpty, UserInputException


def get_user_input(txt: str = "Name Card") -> str:
    user_input = input(txt)

    if len(user_input.strip()) > 0 and isinstance(user_input, str):
        return user_input
    else:
        raise UserInputException


def user_input_handler(
    deck: CardDeck,
) -> Tuple[None | BaseCard, None | UserInputException]:
    while True:
        try:
            print(deck)
            user_input = get_user_input()
            card_from_deck = deck.get_instance_of_card(user_input)
            return card_from_deck, None

        except UserInputException as e:
            print(e.message)
            return None, UserInputException

        except BoardErrorEmpty as e:
            print(e.message)

        except (ValueError, KeyError) as e:
            print("No Card with this name in the Board")


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
