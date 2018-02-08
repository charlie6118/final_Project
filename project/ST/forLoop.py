from Stock import Stock
from helper import *
import time

invest = []


for symbol in range(1201, 1237):
    stock_exist = check("02", symbol)
    if not stock_exist:
        pass
    else:

        stock = get("02", symbol)

        print('{}之五日均線為{}'.format(symbol, stock.dic["5_days"]))
        print('{}之二十日均線為{}'.format(symbol, stock.dic["20_days"]))
        print('{}之六十日均線為{}'.format(symbol, stock.dic["60_days"]))


        if stock.dic["5_days"] == stock.dic["20_days"] or stock.dic["5_days"] == stock.dic["60_days"] or stock.dic["20_days"] == stock.dic["60_days"]:
            invest.append(symbol)
        else:
            pass
    time.sleep(10)

if len(invest) != 0:
    print(invest)
else:
    print("nothing match")