import strategy

players = {
    "random11": strategy.getRandom1,
    "random12": strategy.getRandom1,
    "random13": strategy.getRandom1,
    "random14": strategy.getRandom1,
    "random21": strategy.getRandom2,
    "random22": strategy.getRandom2,
    "random23": strategy.getRandom2,
    "random24": strategy.getRandom2,
    "trend1": strategy.getHistoryTrend,
    "trend2": strategy.getHistoryTrend,
    "trend3": strategy.getHistoryTrend,
    "Trend1": strategy.getSpecialTrend,
    "repeater1": strategy.getRepeat,
    "avg1": strategy.getHistoryAvg,
    "avg2": strategy.getHistoryAvg,
    "avg3": strategy.getHistoryAvg,
    "avg&trend": strategy.getHistoryTrendAndAvg,
    "avg&last": strategy.getHistoryLastAndAvg,
}
