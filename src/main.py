import players
from goldenNumber.game import Game
import sys
import os
import json


def main():

    maxRound = 8
    saveLog = False
    showGoldenNum, showPlayerScore = True, True

    if len(sys.argv) <= 1:
        pass
    elif len(sys.argv) >= 2:
        other = list(filter(lambda x: not x.startswith('-'), sys.argv[1:]))
        if len(other) > 0:
            maxRound = int(other[0])

        switches = list(map(lambda x: x.lstrip('-'),
                            filter(lambda x: x.startswith('-'), sys.argv[1:])))
        saveLog = "l" in switches
        showGoldenNum, showPlayerScore = "ng" not in switches, "ns" not in switches

    g = Game()

    g.initUsers(players.players.keys())

    while g.round < maxRound:
        g.beginRound()
        for name, func in players.players.items():
            act = func(g.getHistory())
            if not g.userAct(name, act):
                print("User", name, "submitting failed:", (act.num1, act.num2))
        g.endRound()

    print("Finished", maxRound, "rounds")
    if g.userNum > 0:
        print("Winner:", sorted(g.scores.items(),
                                key=lambda x: x[1], reverse=True)[0])
    print(g.scores)

    if showGoldenNum or showPlayerScore:
        import viewer
        if viewer.importedSuccess:
            if showGoldenNum:
                viewer.drawGoldenNumber(g)
            if showPlayerScore:
                viewer.drawScore(g)
            viewer.plt.show()

    if saveLog:
        with open("./log.json", 'w', encoding='utf-8') as json_file:
            json.dump(g.getHistory(), json_file,
                      default=lambda obj: obj.__dict__, sort_keys=True, indent=4)


if __name__ == "__main__":
    main()
