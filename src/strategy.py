import random
import numpy as np

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


def getRandom1(history: History) -> Action:
    """Random number in (0,100)"""
    x = helper.adjustNumberInRange(0 + 100 * randomReal())
    y = helper.adjustNumberInRange(0 + 100 * randomReal())
    return Action(x, y)


def getRandom2(history: History) -> Action:
    """Random number in (0,61.8]"""
    x = helper.adjustNumberInRange(0 + 100 * 0.618 * randomReal())
    y = helper.adjustNumberInRange(0 + 100 * 0.618 * randomReal())
    return Action(x, y)


def getHistoryTrend(history: History) -> Action:
    """Follow the last two golden Number's trend"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom2(history)
    elif len(gl) == 1:
        return Action(gl[0], gl[0])
    else:
        y = gl[-1] + gl[-1] - gl[-2]
        return Action(gl[-1], helper.adjustNumberInRange(y))


def getHistoryAvg(history: History) -> Action:
    """Average of history golden numbers"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom2(history)
    else:
        x = historyAvg(history)
        return Action(x, x)


def getHistoryTrendAndAvg(history: History) -> Action:
    """Use trend and average"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom2(history)
    elif len(gl) == 1:
        return Action(gl[0], gl[0])
    else:
        y = gl[-1] + gl[-1] - gl[-2]
        return Action(historyAvg(history), helper.adjustNumberInRange(y))


def getHistoryLastAndAvg(history: History) -> Action:
    """Use last and average"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom2(history)
    elif len(gl) == 1:
        return Action(gl[0], gl[0])
    else:
        return Action(historyAvg(history), gl[-1])


def getRepeat(history: History) -> Action:
    """Use last two golden number"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom2(history)
    elif len(gl) == 1:
        return Action(gl[-1], gl[-1])
    else:
        return Action(gl[-1], gl[-2])


def getSpecialTrend(history: History) -> Action:
    """Special trend with history"""
    gl = history.goldenNums
    if len(gl) == 0:
        return getRandom2(history)
    x, y = gl[-1], gl[-1]
    if len(gl) >= 2:
        t = gl[-1] - gl[-2]
        if abs(t) > 2:
            t = 0
        x += t
    if len(gl) >= 3:
        t = gl[-2]-gl[-3]
        if abs(t) > 2:
            t = 0
        y += t
    return Action(x,y)