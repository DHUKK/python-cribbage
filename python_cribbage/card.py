from pydantic import BaseModel, conint

_card_value_map: dict[int, int] = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 10,
    12: 10,
    13: 10,
}


class Card(BaseModel, frozen=True):
    """Representation of a playing card"""

    rank: conint(ge=1, le=13)
    suit: conint(ge=1, le=4)

    @property
    def value(self) -> int:
        """Get the value of the playing card.

        Returns:
            int: The value of the playing card. Between 1 and 10.
        """
        return _card_value_map[self.rank]

    def pair(self, card: "Card") -> bool:
        """Determine whether a playing card pairs another playing card.

        Args:
            card (Card): Card to check if this card pairs.

        Returns:
            bool: Whether the card pairs this card.
        """
        return card.rank == self.rank
