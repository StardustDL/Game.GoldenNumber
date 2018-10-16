# 黄金点游戏测试框架

## 文件架构

- `main.py` 程序主文件，处理命令行参数
- `players.py` 记录所有注册的玩家及其策略
- `strategy.py` 定义用到的策略，实现解耦
- `game.py` 游戏相关类型

## 使用

1. 在策略文件中实现自己的策略函数

```python
def getRandomNum(history: History) -> Action:
    x = None
    y = None
    return Action(x, y)
```

2. 在玩家文件中登记玩家名和对应策略

```python
"random1": strategy.getRandomNum,
```

3. 命令行调用，执行完成后，程序显示每个玩家的得分

```sh
python ./main.py

# 测试 1000 回合
python ./main.py 1000

# 测试 100 回合并将回合历史信息记录到 log.json 文件中
python ./python 100 -l
```
