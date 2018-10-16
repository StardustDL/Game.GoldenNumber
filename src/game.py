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
        self.userNum = len(users)
        for name in users:
            self.userActs[name] = []
            self.scores[name] = 0

    def beginRound(self):
        self.round += 1

    def endRound(self):
        sm = 0
        cnt = 0
        for acts in self.userActs.values():
            if len(acts) == self.round:
                sm += acts[-1].num1 + acts[-1].num2
                cnt += 2
        avg = sm / cnt
        self.goldenNums.append(avg)
        if self.userNum >= 2:
            mn, mnName = 200, None
            mx, mxName = -200, None
            for name, acts in self.userActs.items():
                if len(acts) == self.round:
                    x, y = abs(acts[-1].num1-avg), abs(acts[-1].num2-avg)
                    if x < mn:
                        mn, mnName = x, name
                    if x > mx:
                        mx, mxName = x, name
                    if y < mn:
                        mn, mnName = y, name
                    if y > mx:
                        mx, mxName = y, name
            self.scores[mnName] += self.userNum - 2
            self.scores[mxName] += -2

        for acts in self.userActs.values():
            if len(acts) != self.round:
                acts.append(Action(0, 0))

    def getHistory(self) -> History:
        return History(self.goldenNums, self.userActs)

    def userAct(self, name: str, action: Action)->bool:
        if (not (0 < action.num1 < 100)) or (not (0 < action.num2 < 100)):
            return False
        if name not in self.userActs:
            return False
        if len(self.userActs[name]) == self.round:
            return False
        self.userActs[name].append(action)
        return True
