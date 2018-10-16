import players
from game import Game
import sys
import os
import json


def main():

    maxRound = 5
    saveLog = False

    if len(sys.argv) <= 1:
        pass
    elif len(sys.argv) == 2:
        maxRound = int(sys.argv[1])
    elif len(sys.argv) == 3:
        maxRound = int(sys.argv[1])
        saveLog = sys.argv[2] == "-l"

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
    print(g.scores)
    if saveLog:
        with open("./log.json", 'w', encoding='utf-8') as json_file:
            json.dump(g.getHistory(), json_file,
                      default=lambda obj: obj.__dict__, sort_keys=True, indent=4)


if __name__ == "__main__":
    main()
