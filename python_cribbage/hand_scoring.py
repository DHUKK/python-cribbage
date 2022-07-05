from itertools import combinations
import math
from python_cribbage.card_set import CardSet
from collections import Counter


PAIR_SCORES: dict[int, int] = {1: 0, 2: 2, 3: 6, 4: 12}


class HandScoring:
    def score(self, hand: CardSet):
        total_score = 0
        for i in [
            PairsCondition(),
            StraightInHandCondition(),
            FifteensCondition(),
            FlushCondition(),
        ]:
            total_score += i.check(hand)
        return total_score


class PairsCondition:
    def check(self, hand: CardSet):
        score = 0
        counts = Counter(hand.ranks).values()
        for count in counts:
            score += PAIR_SCORES.get(count)
        return score


class EqualsCondition:
    def __init__(self, n):
        self.n = n

    def check(self, hand: CardSet):
        total = sum(hand.values)
        return 2 if total == self.n else 0


class StraightInHandCondition:
    @classmethod
    def check(cls, hand: CardSet):
        ans = 0
        count = 0

        arr = sorted(hand.ranks)
        n, v = len(arr), [arr[0]]

        for i in range(1, n):
            if arr[i] != arr[i - 1]:
                v.append(arr[i])

        for i in range(len(v)):
            if i > 0 and v[i] == v[i - 1] + 1:
                count += 1
            else:
                count = 1
            ans = max(ans, count)

        if ans >= 3:
            count = Counter(arr)
            mul = []
            for i in v:
                if count[i] > 1:
                    mul.append(count[i])
            return ans * math.prod(mul)
        return ans if ans >= 3 else 0


class StraightInPlayCondition:
    @staticmethod
    def _is_straight(card_set: CardSet):
        rank_set = set(card_set.ranks)
        return (
            ((max(rank_set) - min(rank_set) + 1) == len(card_set) == len(rank_set))
            if len(card_set) > 2
            else False
        )

    @classmethod
    def check(cls, card_set: CardSet):
        while card_set:
            if cls._is_straight(card_set):
                return len(card_set)
            card_set.cards.pop(0)
        return 0


class FifteensCondition:
    def check(self, hand: CardSet):
        count = 0
        combs = []
        card_values = hand.values
        for i in range(len(card_values)):
            combs += list(combinations(card_values, i + 1))
        for i in combs:
            count += 1 if sum(i) == 15 else 0
        return count * 2


class FlushCondition:
    def check(self, hand: CardSet):
        suit_count = max(Counter(hand.suits).values())
        if suit_count > 5:
            raise ValueError("Cannot have a flush higher than 5")
        return suit_count if suit_count >= 4 else 0
