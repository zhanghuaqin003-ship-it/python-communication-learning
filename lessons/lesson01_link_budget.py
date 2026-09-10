tx_power_dbm = float(input("请输入发射功率(dbm): "))
path_loss_db = float(input("请输入路径损耗(db): "))

rx_power_dbm = tx_power_dbm - path_loss_db

print("接收功率:", rx_power_dbm, "dbm")
