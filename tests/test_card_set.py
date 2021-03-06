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


def test_card_set_add():
    input_data = {
        "cards": [
            {"rank": 1, "suit": 1},
            {"rank": 10, "suit": 1},
            {"rank": 3, "suit": 1},
        ]
    }
    cardset = CardSet.parse_obj(input_data)
    input_data = {
        "cards": [
            {"rank": 1, "suit": 2},
            {"rank": 10, "suit": 2},
            {"rank": 3, "suit": 2},
        ]
    }
    cardset2 = CardSet.parse_obj(input_data)

    input_data = {
        "cards": [
            {"rank": 1, "suit": 1},
            {"rank": 10, "suit": 1},
            {"rank": 3, "suit": 1},
            {"rank": 1, "suit": 2},
            {"rank": 10, "suit": 2},
            {"rank": 3, "suit": 2},
        ]
    }
    added_cardset = CardSet.parse_obj(input_data)

    assert added_cardset == cardset + cardset2


def test_pick_random_cards():
    input_data = {
        "cards": [
            {"rank": 1, "suit": 1},
            {"rank": 10, "suit": 1},
            {"rank": 3, "suit": 1},
            {"rank": 1, "suit": 2},
            {"rank": 10, "suit": 2},
            {"rank": 3, "suit": 2},
        ]
    }
    cards = CardSet.parse_obj(input_data)

    sub = cards.pick_random_cards(3)
    cards_sub = cards - sub

    cards_add = cards_sub + sub
    assert True == all(elem in cards_add.cards for elem in cards.cards)


def test_random_cards():
    cards = CardSet.random_cards(52)
    assert 52 == len(cards)

    cards = CardSet.random_cards(21)
    assert 21 == len(cards)

    cards = CardSet.random_cards()
    assert 52 == len(cards)
