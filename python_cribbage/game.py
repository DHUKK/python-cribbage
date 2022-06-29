from pydantic import BaseModel
from typing import Dict, List
from python_cribbage import game_hand


class Game(BaseModel):
    scores: Dict[str, int]
    game_hands: List[game_hand.GameHand]
