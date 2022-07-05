from pydantic import BaseModel, root_validator
from typing import List, Dict, Optional
from python_cribbage import hand, card, card_set


class GameHand(BaseModel):
    scores: List[int]
    hands: List[hand.Hand]
    cut_card: Optional[card.Card]
    deck: card_set.CardSet
    crib_player: int

    @root_validator
    def validate_number_of_cards(cls, values):
        hands = values.get("hands")
        if not hands:
            raise ValueError("Invalid hands")
        cut_card = values.get("cut_card")
        if not cut_card:
            raise ValueError("Invalid cut card")
        deck = values.get("deck")
        if not cut_card:
            raise ValueError("Invalid deck")
        test = deck + cut_card
        for hand in hands:
            test += hand
        if len(test) != 52:
            raise ValueError("Incorrect number of cards in play")
        return values
