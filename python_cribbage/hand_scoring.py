from itertools import combinations
from abc import ABCMeta, abstractmethod
from python_cribbage.card_set import CardSet
from collections import Counter


class ScoreCondition(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def check(self, hand):
        raise NotImplementedError


PAIR_SCORES = {1: 0, 2: 2, 3: 6, 4: 12}


class PairsCondition(ScoreCondition):
    def check(self, hand: CardSet):
        score = 0
        counts = Counter(c.rank for c in hand.cards).values()
        for count in counts:
            score += PAIR_SCORES.get(count)
        return score


class EqualsCondition(ScoreCondition):
    def __init__(self, n):
        self.n = n
        super().__init__()

    def check(self, hand: CardSet):
        total = sum(card.rank for card in hand.cards)
        return 2 if total == self.n else 0


class StraightInHandCondition(ScoreCondition):
    @classmethod
    def check(cls, hand: CardSet):
        ans = 0
        count = 0

        arr = [x.rank for x in hand.cards]
        n = len(arr)
        v = [arr[0]]

        for i in range(1, n):
            if arr[i] != arr[i - 1]:
                v.append(arr[i])

        for i in range(len(v)):
            if i > 0 and v[i] == v[i - 1] + 1:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans if ans >= 3 else 0


class StraightInPlayCondition(ScoreCondition):
    @staticmethod
    def _is_straight(cards):
        rank_set = set([card.rank for card in cards])
        return (
            ((max(rank_set) - min(rank_set) + 1) == len(cards) == len(rank_set))
            if len(cards) > 2
            else False
        )

    @classmethod
    def check(cls, card_set: CardSet):
        card_set = card_set.cards[:]
        while card_set:
            if cls._is_straight(card_set):
                return len(card_set)
            card_set.pop(0)
        return 0


class FifteensCondition(ScoreCondition):
    def check(self, hand: CardSet):
        count = 0
        combs = []
        card_ranks = [card.rank for card in hand.cards]
        for i in range(len(card_ranks)):
            combs += list(combinations(card_ranks, i + 1))
        for i in combs:
            count += 1 if sum(i) == 15 else 0
        return count * 2


class FlushCondition(ScoreCondition):
    def check(self, hand: CardSet):
        suit_count = max(Counter([card.suit for card in hand.cards]).values())
        if suit_count > 5:
            raise ValueError("Cannot have a flush higher than 5")
        return suit_count if suit_count >= 4 else 0
