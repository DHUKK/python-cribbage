from python_cribbage.card import Card
import pytest
from pydantic import ValidationError


def test_card_validation():
    Card(rank=1, suit=2)
    with pytest.raises(ValidationError) as e:
        Card(rank=66, suit=2)


def test_card_pair():
    ace_heart = Card(rank=1, suit=1)
    ace_spade = Card(rank=1, suit=2)

    assert True == ace_heart.pair(ace_spade)
    assert True == ace_spade.pair(ace_heart)
    assert not ace_spade == ace_heart
