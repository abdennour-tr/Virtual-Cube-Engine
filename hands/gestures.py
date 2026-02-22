import math


def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def pinch(p1, p2, threshold=25):
    return distance(p1, p2) < threshold


def is_fist(hand):
    # index plié
    return hand.landmark[8].y > hand.landmark[6].y


def is_hand_open(hand):
    tips = [8, 12, 16, 20]
    wrist = hand.landmark[0]

    for tip in tips:
        if hand.landmark[tip].y > wrist.y:
            return False
    return True


def count_extended_fingers(hand):
    count = 0

    tips = [8, 12, 16, 20]
    bases = [6, 10, 14, 18]

    for tip, base in zip(tips, bases):
        if hand.landmark[tip].y < hand.landmark[base].y:
            count += 1

    return count


def is_two_fingers(hand):
    return count_extended_fingers(hand) == 2


def is_three_fingers(hand):
    return count_extended_fingers(hand) == 3
