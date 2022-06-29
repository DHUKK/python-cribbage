from pydantic import BaseModel, conint

value_map = {
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
    rank: conint(ge=1, le=13)
    suit: conint(ge=1, le=4)

    @property
    def value(self) -> int:
        return value_map[self.rank]

    def pair(self, card: "Card") -> bool:
        return card.rank == self.rank
