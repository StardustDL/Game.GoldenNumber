from goldenNumber.game import Game

importedSuccess = False

try:
    import numpy as np
    import matplotlib.pyplot as plt
    importedSuccess = True
except ImportError:
    print("Importing failed for viewer, please install nessesary modules. See README.")


def drawScore(game: Game):
    """Draw players' score figure"""
    plt.figure()
    plt.title("Scores")
    plt.xlabel("Player")
    plt.ylabel("Score")

    sortedScores = sorted(game.scores.items(),
                          key=lambda x: x[1])
    names = list(map(lambda x: x[0], sortedScores))
    scores = list(map(lambda x: x[1], sortedScores))

    plt.barh(names, scores)


def drawGoldenNumber(game: Game):
    """Draw golden number trend figure"""
    plt.figure()
    plt.title("Golden Number Trend")
    plt.xlabel("Round")
    plt.ylabel("Golden Number")

    rounds = list(range(game.round))

    plt.xticks(rounds)
    plt.plot(game.goldenNums)
