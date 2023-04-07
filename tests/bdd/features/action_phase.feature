Feature: Action phase 
   
    Scenario Outline: Player plays action card
        Given Card is <default_card>
        Given Player with deck of <default_card> 

        #Action phase skipped
        When ActionPhase <default_card> is played
        
        Then <default_card> card is in cards_in_play pile True

        Examples:
        | default_card |
        | Smithy       |

