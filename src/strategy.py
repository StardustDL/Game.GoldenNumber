import random

from goldenNumber.game import Action, History
import goldenNumber.helper as helper


def randomReal() -> float:
    """Return random number in [0,1]"""
    MAX = 10**10
    return random.randint(0, MAX) / MAX


def historyAvg(history: History) -> float:
    gl = history.goldenNums
    if len(gl) == 0:
        return None
    return sum(gl)/len(gl)


def getRandom(history: History) -> Action:
    """Random number in [0,61.8]"""
    x = 0 + 100 * 0.618 * randomReal()
    y = 0 + 100 * 0.618 * randomReal()
    return Action(x, y)


def getHistoryTrend(history: History) -> Action:
    """Follow the last two golden Number's trend"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom(history)
    elif len(gl) == 1:
        return Action(gl[0], gl[0])
    else:
        y = gl[-1] + gl[-1] - gl[-2]
        return Action(gl[-1], helper.adjustNumberInRange(y))


def getHistoryAvg(history: History) -> Action:
    """Average of history golden numbers"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom(history)
    else:
        x = historyAvg(history)
        return Action(x, x)


def getHistoryTrendAndAvg(history: History) -> Action:
    """Follow the last two golden number's trend"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom(history)
    elif len(gl) == 1:
        return Action(gl[0], gl[0])
    else:
        y = gl[-1] + gl[-1] - gl[-2]
        return Action(historyAvg(history), helper.adjustNumberInRange(y))
