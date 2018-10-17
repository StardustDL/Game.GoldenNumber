import strategy

players = {
    "random1": strategy.getRandom,
    "random2": strategy.getRandom,
    "random3": strategy.getRandom,
    "random4": strategy.getRandom,
    "random5": strategy.getRandom,
    "random6": strategy.getRandom,
    "random7": strategy.getRandom,
    "random8": strategy.getRandom,
    "trend": strategy.getHistoryTrend,
    "avg": strategy.getHistoryAvg,
    "avg&trend": strategy.getHistoryTrendAndAvg,
}
