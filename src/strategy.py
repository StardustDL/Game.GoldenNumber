from game import Action, History
import random


def randomReal() -> float:
    MAX = 10**10
    return random.randint(0, MAX) / MAX


def getRandomNum(history: History) -> Action:
    x = 0 + 100 * 0.618 * randomReal()
    y = 0 + 100 * 0.618 * randomReal()
    return Action(x, y)

def getHistoryNum(history: History) -> Action:
    gl = history.goldenNums
    if len(gl)==0:
        return getRandomNum(history)
    elif len(gl) == 1:
        return Action(gl[0], gl[0])
    else:
        y = gl[-1] + gl[-1] - gl[-2]
        if y <= 0:
            y = 0.1
        if y >= 100*0.618:
            y = 100 * 0.618 - 0.1
        return Action(gl[-1], y)
