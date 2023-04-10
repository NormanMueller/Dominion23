Feature: Buy Phase
    Scenario: Player has no Treasure card
        Given Player with no treasure card in handcards
        
        When Player in buy phase
   
        Then Player cant buy a card cost more then 0
        Then Player can buy a card cost more then 0

    Scenario: Player has action card
        Given Player with action card in handcards
       
        When Player plays action card

        Then Action card is in cards_inplay pile
        Then Action card is not in handcards

