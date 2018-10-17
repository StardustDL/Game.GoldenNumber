class Action:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2


class History:
    def __init__(self, goldenNums: list, userActs: dict):
        self.goldenNums = goldenNums
        self.userActs = userActs


class Game:
    def __init__(self):
        self.goldenNums = []
        self.userActs = {}
        self.round = 0
        self.scores = {}
        self.userNum = 0

    def initUsers(self, users: list):
        """Initialize players"""
        self.userNum = len(users)
        for name in users:
            self.userActs[name] = []
            self.scores[name] = 0

    def beginRound(self):
        """Start a new round"""
        self.round += 1

    def endRound(self):
        """End current round and judge for scores"""
        sm = 0
        cnt = 0
        for acts in self.userActs.values():
            if len(acts) == self.round:
                sm += acts[-1].num1 + acts[-1].num2
                cnt += 2
        avg = 0.618 * (sm / cnt)
        self.goldenNums.append(avg)
        if self.userNum >= 2:
            mn, mnName = 200, set()
            mx, mxName = -200, set()
            for name, acts in self.userActs.items():
                if len(acts) == self.round:
                    x, y = abs(acts[-1].num1-avg), abs(acts[-1].num2-avg)
                    if x < mn:
                        mn = x
                        mnName.clear()
                        mnName.add(name)
                    elif x == mn:
                        mnName.add(name)
                    if x > mx:
                        mx = x
                        mxName.clear()
                        mxName.add(name)
                    elif x == mx:
                        mxName.add(name)

                    if y < mn:
                        mn = y
                        mnName.clear()
                        mnName.add(name)
                    elif y == mn:
                        mnName.add(name)
                    if y > mx:
                        mx = y
                        mxName.clear()
                        mxName.add(name)
                    elif y == mx:
                        mxName.add(name)
            for name in mnName:
                self.scores[name] += self.userNum - 2
            for name in mxName:
                self.scores[name] += -2

        for acts in self.userActs.values():
            if len(acts) != self.round:
                acts.append(Action(0, 0))

    def getHistory(self) -> History:
        """Gets history"""
        return History(self.goldenNums, self.userActs)

    def userAct(self, name: str, action: Action) -> bool:
        """Do a user action"""
        if (not (0 < action.num1 < 100)) or (not (0 < action.num2 < 100)):
            return False
        if name not in self.userActs:
            return False
        if len(self.userActs[name]) == self.round:
            return False
        self.userActs[name].append(action)
        return True
