from __future__ import annotations

import itertools
from typing import TYPE_CHECKING
from expansions.utils.helper import UserInputException, get_user_input
from expansions.utils.field import  BoardError


if TYPE_CHECKING:
    from game.phase.turn import Turn
    from player.base_player import Player
    from expansions.utils.field import Field

class BuyPhase:
    @staticmethod
    def calculate_available_money(player: Player) -> int:
        overall_money = 0
        # Money from Treasure Cards (from Hand) and Action Cards (which are in play)
        for card in itertools.chain(
            player.deck.hand_cards.card_list + player.deck.cards_in_play.card_list
        ):
            overall_money += card.MONEY

        return overall_money

    @staticmethod
    def buy_card(player: Player, board: Field, turn: Turn) -> None:
        try:
            while True:
                if turn.Buys <= 0:
                    break

                print(
                    "You are in the 'buy_phase' input cardname u wanna buy, for skip press enter"
                )

                desired_card = get_user_input()
                card_from_field, error = board.return_fieldcard(desired_card)
                if error in [BoardError.NoMatch, BoardError.NotAvailable]:
                    continue

                if BuyPhase.calculate_available_money(player) >= card_from_field.PRICE:
                    player.deck.discard_pile.add(card_from_field)
                    turn.Buys -= 1
                else:
                    print(
                        f"not enough money to buy {desired_card}, choose new card or skip"
                    )

        except UserInputException:
            pass
