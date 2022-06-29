from pydantic import BaseModel, validator
from typing import List
from python_cribbage import card


class CardSet(BaseModel, frozen=True):
    cards: List[card.Card]

    @validator("cards")
    def cards_not_duplicate(cls, v):
        if len(v) == len(set(v)):
            return v
        raise ValueError("CardSet cannot contain duplicate cards")
