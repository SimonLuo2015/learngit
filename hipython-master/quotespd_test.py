# -*- coding:utf-8 -*-
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#验证下载道琼斯数据的函数是否正常
code = 'IBM'
start_date = (2016, 1, 1)
end_date = (2016, 8, 31)
quotes = quotes_historical_yahoo_ochl(code, start_date, end_date)
fields = ['date','open','close','high','low','volume']
list1 = []
for i in range(0,len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)

quotesdf = pd.DataFrame(quotes, index = list1, columns = fields)
quotesdf = quotesdf.drop(['date'], axis = 1)
print quotesdf.head()

#测试的输出结果如下，表明以上程序正确。
#                   open       close        high         low     volume
# 2016-01-04  131.807555  132.147757  132.167202  130.485590  5229400.0
# 2016-01-05  132.935101  132.050563  133.061470  131.078531  3924800.0
# 2016-01-06  130.621674  131.389573  131.788110  129.882920  4310900.0
# 2016-01-07  129.960684  129.144181  131.243773  128.726199  7025800.0
# 2016-01-08  129.455224  127.948586  130.077338  127.647258  4762700.0

# 测试能否正常绘图
quotesdf.plot(marker='o')
plt.show()
# 测试结果表明可以正常绘图。

# quotes_plot_df = pd.DataFrame()
# for i in range(0,len(list1)):
#     quotes_plot_df[list1[i]] = quotesdf[list1[i]]
# print "ready to plot"
# quotes_plot_df.plot(marker='o')