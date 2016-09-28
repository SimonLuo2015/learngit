# -*- coding:utf-8 -*-
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

def _wxdate2pydate(date):
    import datetime
    if date.IsValid():
        ymd = map(int, date.FormatISODate().split('-'))
        return datetime.date(*ymd)
    else:
        return None

def PlotData(code, start, end, list2):
    start_date = _wxdate2pydate(start)
    end_date = _wxdate2pydate(end)
    print code
    print start_date
    print end_date
    quotes = quotes_historical_yahoo_ochl(code, start_date, end_date)
    fields = ['date','open','close','high','low','volume']
    # 获取到quotes有多少天的数据。
    list1 = []
    for i in range(0,len(quotes)):
        x = date.fromordinal(int(quotes[i][0]))
        y = datetime.strftime(x,'%Y-%m-%d')
        # list1里存储了查到的所有的日期，准备用作index。
        list1.append(y)
    # print list1
    
    quotesdf = pd.DataFrame(quotes, index = list1, columns = fields)
    quotesdf = quotesdf.drop(['date'], axis = 1)

    # 新建一个temp的DataFrame实例。
    quotesdftemp = pd.DataFrame()
    print quotesdftemp
    
    # list2里存储的是用户的check box选择项集合。
    for i in range(0,len(list2)):
        # 根据用户选择需要展示的'open', 'close', 'high', 'low', 'volume'中一个或几个，
        # 将quotesdf中对应的column复制到quotesdftemp
        quotesdftemp[list2[i]] = quotesdf[list2[i]]
    print quotesdftemp
    print "ready to plot"
    quotesdftemp.plot(marker='o')
    plt.show()
 

