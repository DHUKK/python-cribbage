from python_cribbage.card import Card
from python_cribbage.card_set import CardSet
import pytest
from pydantic import ValidationError


def test_card_set_validation():
    input_data = {
        "cards": [
            {"rank": 1, "suit": 1},
            {"rank": 1, "suit": 1},
        ]
    }
    with pytest.raises(ValidationError) as e:
        CardSet.parse_obj(input_data)

    input_data = {
        "cards": [
            {"rank": 1, "suit": 1},
            {"rank": 10, "suit": 1},
            {"rank": 3, "suit": 1},
        ]
    }
    cardset = CardSet.parse_obj(input_data)
    print(cardset)