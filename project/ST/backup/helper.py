import urllib.request
import csv
import time
from Stock import Stock

def check(month, symbol):

    if month == '12' or month == '11' or month == '10':
        year = '2017'
    else:
        year = '2018'

    proxy = urllib.request.ProxyHandler({'http': 'http://www.tse.com.tw/exchangeReport/STOCK_DAY_AVG?response=csv&date={year}{month}01&stockNo={symbol}'})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)

    url = f"http://www.tse.com.tw/exchangeReport/STOCK_DAY_AVG?response=csv&date={year}{month}01&stockNo={symbol}"

    webpage = urllib.request.urlopen(url)

    datareader = csv.reader(webpage.read().decode("big5").splitlines())

    row = next(datareader)

    if not row:
        return False
    return True

#get csv file from http://www.tse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html
def getFile(month, symbol):

    if month == '12' or month == '11' or month == '10':
        year = '2017'
    else:
        year = '2018'

    proxy = urllib.request.ProxyHandler({'http': 'http://www.tse.com.tw/exchangeReport/STOCK_DAY_AVG?response=csv&date={year}{month}01&stockNo={symbol}'})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)

    url = f"http://www.tse.com.tw/exchangeReport/STOCK_DAY_AVG?response=csv&date={year}{month}01&stockNo={symbol}"

    #print(year, month)
    time.sleep(1)

    webpage = urllib.request.urlopen(url)

    datareader = csv.reader(webpage.read().decode("big5").splitlines())

    next(datareader)

    next(datareader)

    stock_list = list(datareader)

    return stock_list

#lookup three kinds of point and Insert the value to the dictionary
def lookup(month, symbol):

    stock = Stock()

    stock_list = getFile(month, symbol)

    #count for getting rid of the unnecessary rows
    count = 0

    #reversed for the newest data in that month
    for row in reversed(stock_list):

        #get rid of unnecessary rows
        if count > 4 :

            if len(stock.line_5) < 5:

                stock.line_5.append(row[1])

            if len(stock.line_20) < 20:

                stock.line_20.append(row[1])

            if len(stock.line_60) < 60:

                stock.line_60.append(row[1])

        if count != 5:
            count += 1

    #insert the element into line_5, line_20, line_60 respectively
    if len(stock.line_5) < 5:

        stock_pre = lookup(getPreMonth(month), symbol)
        stock_pre_ = lookup(getPreMonth(getPreMonth(month)), symbol)
        stock_pre_p = lookup(getPreMonth(getPreMonth(getPreMonth(month))), symbol)

        if len(stock.line_5) < 5:
            for i in range(5 - len(stock.line_5)):
                stock.line_5.append(stock_pre.line_5[i])

        if len(stock.line_20) < 20:
            for i in range(20 - len(stock.line_20)):
                stock.line_20.append(stock_pre.line_20[i])

        if len(stock.line_60) < 60:
            for i in range(len(stock_pre.line_60)):
                stock.line_60.append(stock_pre.line_60[i])
            for i in range(len(stock_pre_.line_60)):
                stock.line_60.append(stock_pre_.line_60[i])
            for i in range(60 - len(stock.line_60)):
                stock.line_60.append(stock_pre_p.line_60[i])

    return stock



def get(month, symbol):

    stock = lookup(month, symbol)

    sum_5 = 0
    sum_20 = 0
    sum_60 = 0

    for str in stock.line_5:
        sum_5 += float(str)

    for str in stock.line_20:
        sum_20 += float(str)

    for str in stock.line_60:
        sum_60 += float(str)

    day_point_5 = sum_5 / len(stock.line_5)
    day_point_20 = sum_20 / len(stock.line_20)
    day_point_60 = sum_60 / len(stock.line_60)

    print(stock.line_5)
    print(stock.line_20)
    print(stock.line_60)


    stock.dic["5_days"] = day_point_5
    stock.dic["20_days"] = day_point_20
    stock.dic["60_days"] = day_point_60

    print("{}之5日均線點為: {}".format(symbol, stock.dic["5_days"]))
    print("{}之20日均線點為: {}".format(symbol, stock.dic["20_days"]))
    print("{}之60日均線點為: {}".format(symbol, stock.dic["60_days"]))

    if stock.dic["5_days"] == stock.dic["20_days"] or stock.dic["20_days"] == stock.dic["60_days"] or stock.dic["60_days"] == stock.dic["5_days"]:
        return True
    else:
        return False

#get previous month value
def getPreMonth(month):

    if not int(month) in range(1, 13):
        print("month out of range")
        return;

    if int(month) == 1:
        #print('12')
        return '12'

    if int(month) <= 10:
        #print('0' + str(int(month)-1))
        return '0' + str(int(month)-1)

    if int(month) > 10:
        #print(str(int(month)-1))
        return str(int(month)-1)
