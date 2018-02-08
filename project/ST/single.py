from Stock import Stock
from helper import *
import time

stock = get('02', '2881')
print(stock.line_5)
print(stock.line_20)
print(stock.line_60)

print(stock.dic["5_days"])
print(stock.dic["20_days"])
print(stock.dic["60_days"])
