from random import shuffle
from pydantic import BaseModel, validator
from typing import List
from python_cribbage.card import Card, card_ranks, card_suits
from itertools import product
import random


class CardSet(BaseModel, frozen=True):
    """A set of playing cards"""

    cards: List[Card]

    @validator("cards")
    def cards_not_duplicate(cls, v: List[Card]) -> List[Card]:
        """Ensure no duplicate cards.

        Args:
            v (List[Card]): List of cards to validate.

        Raises:
            ValueError: If duplicates cards are found.

        Returns:
            List[Card]: Valid list of cards.
        """
        if len(v) == len(set(v)):
            return v
        raise ValueError("CardSet cannot contain duplicate cards")

    @property
    def values(self) -> List[int]:
        """Get the values of all the cards in the set.

        Returns:
            List[int]: Values of each card in the set.
        """
        return [card.value for card in self.cards]

    @property
    def ranks(self) -> List[int]:
        """Get the ranks of all the cards in the set.

        Returns:
            List[int]: Ranks of each card in the set.
        """
        return [card.rank for card in self.cards]

    @property
    def suits(self) -> List[int]:
        """Get the suits of all the cards in the set.

        Returns:
            List[int]: Suits of each card in the set.
        """
        return [card.suit for card in self.cards]

    def __len__(self) -> int:
        """Override length

        Returns:
            int: Number of cards in the set.
        """
        return len(self.cards)

    def __add__(self, other):
        """Add two card sets together

        Args:
            other (CardSet): cardset to add

        Returns:
            CardSet: New cardset with cards from self and other
        """
        if isinstance(other, Card):
            return CardSet(cards=self.cards + [other])
        return CardSet(cards=self.cards + other.cards)

    def __sub__(self, other):
        if isinstance(other, Card):
            return CardSet(cards=[item for item in self.cards if item != other])
        return CardSet(cards=[item for item in self.cards if item not in other.cards])

    def pick_random_cards(self, n: int = 1):
        ret_cards = self.cards
        shuffle(ret_cards)
        return CardSet(cards=ret_cards[0:n])

    @classmethod
    def random_cards(cls, n: int = 52) -> "CardSet":
        cards = []
        for suit, rank in product(card_suits, card_ranks):
            cards.append(Card(suit=suit, rank=rank))
        random.shuffle(cards)
        return CardSet(cards=cards[0:n])
