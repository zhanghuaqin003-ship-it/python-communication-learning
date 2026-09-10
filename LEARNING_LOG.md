# Python 通信工程项目学习轨迹

## 2026-09-10

- 学习主题：变量、赋值、加减运算、`print()`、`input()`、`float()`。
- 通信实践：链路预算接收功率计算。
- 已完成：独立计算 `-55 dBm`、`-65 dBm`、`-61 dBm`；完成发射功率与路径损耗的交互式输入。
- 当前状态：理解输入字符串需要转换为数字；正在巩固同时输入多个参数。
- 下一步：加入发射天线增益与接收天线增益；学习 `if` 条件判断，用接收功率门限判断链路是否可用。

## 当前练习代码摘要

```python
tx_power_dbm = float(input("请输入发射功率(dbm): "))
path_loss_db = float(input("请输入路径损耗(db): "))

rx_power_dbm = tx_power_dbm - path_loss_db

print("接收功率:", rx_power_dbm, "dbm")
```
