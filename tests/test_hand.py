from pydantic import ValidationError
from python_cribbage.hand import Hand
import pytest
from pydantic import ValidationError


def test_hand_validation():
    input_data = {
        "cards": [
            {"suit": 1, "rank": 4},
            {"suit": 2, "rank": 4},
            {"suit": 3, "rank": 5},
            {"suit": 1, "rank": 2},
        ]
    }

    Hand.parse_obj(input_data)

    input_data = {
        "cards": [
            {"suit": 1, "rank": 4},
            {"suit": 2, "rank": 4},
            {"suit": 3, "rank": 5},
            {"suit": 1, "rank": 2},
            {"suit": 1, "rank": 8},
        ]
    }
    with pytest.raises(ValidationError) as e:
        Hand.parse_obj(input_data)
