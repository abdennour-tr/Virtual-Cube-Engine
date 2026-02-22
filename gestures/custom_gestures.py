import math


def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def pinch(p1, p2, threshold=30):
    return distance(p1, p2) < threshold


def is_hand_open(hand):
    tips = [8, 12, 16, 20]
    bases = [5, 9, 13, 17]

    count = 0
    for t, b in zip(tips, bases):
        if hand.landmark[t].y < hand.landmark[b].y:
            count += 1

    return count >= 4


def is_fist(hand):
    # index plié
    return hand.landmark[8].y > hand.landmark[6].y
