# 黄金点游戏测试框架

## 游戏规则

N 个玩家，每回合每个玩家给出两个区间 (0,100) 中的有理数（浮点数），回合结束时计算所有数的平均数，然后乘以 **0.618**，得到值 G。
提交的数字最靠近 G（取绝对值）的玩家得到 N-2 分，离 G 最远的玩家得到 -2 分，其他玩家得 0 分。

- 如果玩家数不足两个，则所有玩家分数不变
- 如果回合中某玩家未给出有效数值，则此回合不统计此玩家数值，此玩家得分不变
- 如果一个人同时为最近和最远值，则其得到 N-4 分（即 N-2-2）
- 如果有多个人最近（或最远），他们都得到 N-2 （或 -2）分
- 一个人得分和扣分分别最多一次

## 文件架构

- `main.py` 程序主文件，处理命令行参数
- `players.py` 记录所有注册的玩家及其策略
- `strategy.py` 定义用到的策略，实现解耦
- `game.py` 游戏相关类型
- `viewer.py` 可视化显示相关方法

## 安装

依赖于以下模块，请使用 pip 安装：

- `numpy`
- `matplotlib`

```sh
pip install numpy
pip install matplotlib
```

## 使用

1. 在策略文件中实现自己的策略函数

```python
def getRandom(history: History) -> Action:
    x = None
    y = None
    return Action(x, y)
```

2. 在玩家文件中登记玩家名和对应策略

```python
"random1": strategy.getRandom,
```

3. 命令行调用，执行完成后，程序输出并显示每个玩家的得分，黄金点变化趋势图

|命令行选项|描述|
|-|-|
|数字|指定总回合数，默认为 8|
|`-l`|写入日志文件 `log.json`|
|`-g`|显示黄金点趋势图|
|`-s`|显示玩家得分图|

```sh
python ./main.py

# 测试 1000 回合
python ./main.py 1000

# 测试 100 回合并将回合历史信息记录到 log.json 文件中
python ./main.py 100 -l

python ./main.py 100 -s

python ./main.py 100 -s -g
```

