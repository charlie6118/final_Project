from Stock import Stock
from helper import *
import time
invest = []


for symbol in range(1101, 1130):
    stock_exist = check("02", symbol)
    if not stock_exist:
        pass
    else:
        print(symbol)
        stock = get("02", symbol)
        if stock.dic["5_days"] == stock.dic["20_days"] or stock.dic["5_days"] == stock.dic["60_days"] or stock.dic["20_days"] == stock.dic["60_days"]:
            invest.append(symbol)
        else:
            pass
    time.sleep(10)

print(invest)