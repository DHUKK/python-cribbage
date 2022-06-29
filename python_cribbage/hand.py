from pydantic import validator
from python_cribbage import card_set


class Hand(card_set.CardSet):
    @validator("cards")
    def number_of_cards(cls, v):
        if len(v) > 4:
            raise ValueError("Too many cards in hand. Must be <= 4.")
        return v
