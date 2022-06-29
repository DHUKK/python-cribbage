from multiprocessing.sharedctypes import Value

import pytest
from python_cribbage.card_set import CardSet
from python_cribbage.hand_scoring import (
    PairsCondition,
    StraightInHandCondition,
    StraightInPlayCondition,
    FlushCondition,
    FifteensCondition,
    EqualsCondition,
)


def test_pairs():
    input_data = {
        "cards": [
            {"suit": 1, "rank": 4},
            {"suit": 2, "rank": 4},
            {"suit": 3, "rank": 5},
            {"suit": 1, "rank": 2},
            {"suit": 4, "rank": 2},
        ]
    }

    hand = CardSet.parse_obj(input_data)

    assert 4 == PairsCondition().check(hand)


def test_straight_in_hand():
    input_data = {
        "cards": [
            {"suit": 1, "rank": 8},
            {"suit": 3, "rank": 9},
            {"suit": 2, "rank": 3},
            {"suit": 4, "rank": 4},
            {"suit": 1, "rank": 5},
        ]
    }

    hand = CardSet.parse_obj(input_data)

    assert 3 == StraightInHandCondition().check(hand)

    input_data = {
        "cards": [
            {"suit": 1, "rank": 8},
            {"suit": 3, "rank": 9},
            {"suit": 2, "rank": 3},
            {"suit": 4, "rank": 5},
            {"suit": 1, "rank": 4},
        ]
    }

    hand = CardSet.parse_obj(input_data)

    assert 0 == StraightInHandCondition().check(hand)


def test_straight_in_play():
    input_data = {
        "cards": [
            {"suit": 1, "rank": 8},
            {"suit": 3, "rank": 9},
            {"suit": 2, "rank": 3},
            {"suit": 4, "rank": 4},
            {"suit": 1, "rank": 5},
        ]
    }

    card_set = CardSet.parse_obj(input_data)

    assert 3 == StraightInPlayCondition().check(card_set)

    input_data["cards"].append({"suit": 3, "rank": 10})

    card_set = CardSet.parse_obj(input_data)

    assert 0 == StraightInPlayCondition().check(card_set)


def test_flush():
    input_data = {
        "cards": [
            {"suit": 1, "rank": 8},
            {"suit": 1, "rank": 9},
            {"suit": 1, "rank": 1},
            {"suit": 1, "rank": 4},
        ]
    }

    card_set = CardSet.parse_obj(input_data)

    assert 4 == FlushCondition().check(card_set)

    input_data["cards"].append({"suit": 1, "rank": 10})

    card_set = CardSet.parse_obj(input_data)

    assert 5 == FlushCondition().check(card_set)

    input_data["cards"].append({"suit": 1, "rank": 12})

    card_set = CardSet.parse_obj(input_data)

    with pytest.raises(ValueError) as e:
        FlushCondition().check(card_set)


def test_fifteens():
    input_data = {
        "cards": [
            {"suit": 1, "rank": 8},
            {"suit": 2, "rank": 7},
            {"suit": 3, "rank": 6},
            {"suit": 4, "rank": 9},
        ]
    }

    card_set = CardSet.parse_obj(input_data)

    assert 4 == FifteensCondition().check(card_set)

    input_data["cards"].append({"suit": 2, "rank": 9})

    card_set = CardSet.parse_obj(input_data)

    assert 6 == FifteensCondition().check(card_set)

    input_data = {
        "cards": [
            {"suit": 1, "rank": 1},
            {"suit": 2, "rank": 1},
            {"suit": 3, "rank": 1},
            {"suit": 4, "rank": 2},
            {"suit": 4, "rank": 11},
        ]
    }

    card_set = CardSet.parse_obj(input_data)

    assert 2 == FifteensCondition().check(card_set)

    input_data["cards"].pop()
    input_data["cards"].append({"suit": 4, "rank": 9})

    card_set = CardSet.parse_obj(input_data)

    assert 0 == FifteensCondition().check(card_set)


def test_exactly_equals():
    input_data = {
        "cards": [
            {"suit": 1, "rank": 1},
            {"suit": 2, "rank": 1},
            {"suit": 3, "rank": 1},
            {"suit": 4, "rank": 2},
            {"suit": 4, "rank": 11},
        ]
    }

    card_set = CardSet.parse_obj(input_data)

    assert 2 == EqualsCondition(15).check(card_set)

    input_data["cards"].insert(0, {"suit": 4, "rank": 1})

    card_set = CardSet.parse_obj(input_data)

    assert 0 == EqualsCondition(15).check(card_set)
