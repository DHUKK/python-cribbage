from pydantic import BaseModel
from typing import List, Dict
from python_cribbage import hand


class GameHand(BaseModel):
    id: str
    scores: Dict[str, int]
    hands: Dict[str, hand.Hand]