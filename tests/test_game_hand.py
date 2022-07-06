from python_cribbage.game_hand import GameHand
import pytest
from pydantic import ValidationError
import json


def test_game_hand_validation():
    input_data = {
        "hands": {
            "0": {
                "cards": [
                    {"rank": 1, "suit": 1},
                    {"rank": 2, "suit": 1},
                    {"rank": 3, "suit": 1},
                    {"rank": 4, "suit": 1},
                ]
            },
            "1": {
                "cards": [
                    {"rank": 5, "suit": 1},
                    {"rank": 6, "suit": 1},
                    {"rank": 7, "suit": 1},
                    {"rank": 8, "suit": 1},
                ]
            },
        },
        "crib": {
            "cards": [
                {"rank": 11, "suit": 1},
                {"rank": 12, "suit": 1},
                {"rank": 9, "suit": 1},
                {"rank": 10, "suit": 1},
            ]
        },
        "cut_card": {"rank": 1, "suit": 2},
        "deck": {
            "cards": [
                {"rank": 13, "suit": 1},
                {"rank": 2, "suit": 2},
                {"rank": 3, "suit": 2},
                {"rank": 4, "suit": 2},
                {"rank": 5, "suit": 2},
                {"rank": 6, "suit": 2},
                {"rank": 7, "suit": 2},
                {"rank": 8, "suit": 2},
                {"rank": 9, "suit": 2},
                {"rank": 10, "suit": 2},
                {"rank": 11, "suit": 2},
                {"rank": 12, "suit": 2},
                {"rank": 13, "suit": 2},
                {"rank": 1, "suit": 3},
                {"rank": 2, "suit": 3},
                {"rank": 3, "suit": 3},
                {"rank": 4, "suit": 3},
                {"rank": 5, "suit": 3},
                {"rank": 6, "suit": 3},
                {"rank": 7, "suit": 3},
                {"rank": 8, "suit": 3},
                {"rank": 9, "suit": 3},
                {"rank": 10, "suit": 3},
                {"rank": 11, "suit": 3},
                {"rank": 12, "suit": 3},
                {"rank": 13, "suit": 3},
                {"rank": 1, "suit": 4},
                {"rank": 2, "suit": 4},
                {"rank": 3, "suit": 4},
                {"rank": 4, "suit": 4},
                {"rank": 5, "suit": 4},
                {"rank": 6, "suit": 4},
                {"rank": 7, "suit": 4},
                {"rank": 8, "suit": 4},
                {"rank": 9, "suit": 4},
                {"rank": 10, "suit": 4},
                {"rank": 11, "suit": 4},
                {"rank": 12, "suit": 4},
                {"rank": 13, "suit": 4},
            ]
        },
        "crib_player": "1",
    }

    game_hand = GameHand.parse_obj(input_data)

    hand_scores = game_hand.hand_scores
    assert 3 == len(hand_scores)
    assert 14 == hand_scores["0"]
    assert 12 == hand_scores["1"]
    assert 8 == hand_scores["crib"]

    player_scores = game_hand.player_scores
    assert 2 == len(player_scores)
    assert 14 == player_scores["0"]
    assert 20 == player_scores["1"]

    print(GameHand.schema_json(indent=2))
