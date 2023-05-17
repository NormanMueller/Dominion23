from expansions.utils.helper import BoardError, UserInputException, get_user_input


def discard_hand_card( player, nr = 99) -> int:
    iteration = 0

    try:
        while iteration < nr:
            desired_card = get_user_input("name a card to discard")
            card, error = player.deck.hand_cards.return_card(desired_card)
            if error == BoardError.Empty:
                player.deck.hand_cards.discard(card)
                player.deck.discard_pile.add(card)
                iteration +=1
            else:
                continue
    except UserInputException:
        pass

    return iteration


