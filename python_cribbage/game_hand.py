from pydantic import BaseModel, root_validator
from typing import List, Dict, Optional
from python_cribbage import hand, card, card_set
from python_cribbage.hand_scoring import HandScoring


class GameHand(BaseModel):
    hands: Dict[str, hand.Hand]
    crib: hand.Hand
    cut_card: Optional[card.Card]
    deck: card_set.CardSet
    crib_player: str

    @root_validator
    def validate_number_of_cards(cls, values):
        hands = values.get("hands").values()
        if not hands:
            raise ValueError("Invalid hands")
        cut_card = values.get("cut_card")
        if not cut_card:
            raise ValueError("Invalid cut card")
        deck = values.get("deck")
        if not cut_card:
            raise ValueError("Invalid deck")
        combined_cards = deck + cut_card
        for hand in hands:
            combined_cards += hand
        combined_cards += values.get("crib")
        if len(combined_cards) != 52:
            raise ValueError("Incorrect number of cards in play")
        return values

    @root_validator
    def validate_crib_player(cls, values):
        crib_player = values.get("crib_player")
        players = values.get("hands").keys()
        if crib_player not in players:
            raise ValueError("Crib player not in game")
        return values

    @property
    def hand_scores(self) -> Dict[str, int]:
        scores = {}
        scorer = HandScoring()
        for player, hand in self.hands.items():
            scores[player] = scorer.score(hand + self.cut_card)
        scores["crib"] = scorer.score(self.crib)
        return scores

    @property
    def player_scores(self) -> Dict[str, int]:
        scores = {}
        scorer = HandScoring()
        for player, hand in self.hands.items():
            scores[player] = scorer.score(hand + self.cut_card)
            if player == self.crib_player:
                scores[player] += scorer.score(self.crib)
        return scores
