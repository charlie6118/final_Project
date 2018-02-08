import urllib.request
import csv

#list for 5 days data
stock_line_5 = []

#list for 20 days data
stock_line_20 = []

#list for 60 days data
stock_line_60 = []

year = '2018'


#dictionary for three kinds of line point
dic = {'5_days': 0, '20_days': 0, '60_day': 0}

#get csv file from http://www.tse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html
def getFile(month, year, symbol):

    if month == '12' or month == '11':
        year = '2017'

    print(year, month)

    url = f"http://www.tse.com.tw/exchangeReport/STOCK_DAY_AVG?response=csv&date={year}{month}01&stockNo={symbol}"

    webpage = urllib.request.urlopen(url)

    datareader = csv.reader(webpage.read().decode("big5").splitlines())

    next(datareader)

    next(datareader)

    stock_list = list(datareader)

    return stock_list


#lookup three kinds of point and return a dictionary which stores the result
def lookup(month, symbol):

    stock_list = getFile(month, year, symbol)

    #count for the unnecessary rows
    count = 0

    #reversed for the newest data in that month
    for row in reversed(stock_list):

        #get rid of unnecessary rows
        if count > 4 :

            if len(stock_line_5) < 5:

                stock_line_5.append(row[1])

            if len(stock_line_20) < 20:

                stock_line_20.append(row[1])

            if len(stock_line_60) < 60:

                stock_line_60.append(row[1])

        count += 1

    #check the data is enough for 5 days, 20 days, 60 days, respectively
    if len(stock_line_5) < 5:
        lookup(getPreMonth(month), symbol)

    if len(stock_line_20) < 20:
        lookup(getPreMonth(month), symbol)

    if len(stock_line_60) < 60:
        lookup(getPreMonth(month), symbol)

    sum_5 = 0
    sum_20 = 0
    sum_60 = 0

    for str in stock_line_5:
        sum_5 += float(str)

    for str in stock_line_20:
        sum_20 += float(str)

    for str in stock_line_60:
        sum_60 += float(str)

    day_point_5 = sum_5 / len(stock_line_5)
    day_point_20 = sum_20 / len(stock_line_20)
    day_point_60 = sum_60 / len(stock_line_60)

    print(stock_line_5)
    print(stock_line_20)
    print(stock_line_60)


    dic["5_days"] = day_point_5
    dic["20_days"] = day_point_20
    dic["60_days"] = day_point_60

    print("5日均線點為: {}".format(dic["5_days"]))
    print("20日均線點為: {}".format(dic["20_days"]))
    print("60日均線點為: {}".format(dic["60_days"]))
    return;
    #return dic


#get previous month variable
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


lookup('02', '2881')