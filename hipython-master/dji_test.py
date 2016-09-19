# -*- coding:utf-8 -*-
import urllib
import re

# 下载道琼斯工业平均指数的前三位
str = urllib.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components').read()
print str
# m = re.findall("<tr><td class=\"yfnc_tabledata1\"><b><a href=\".*?\">(.*?)</a></b></td><td class=\"yfnc_tabledata1\">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>", str)

# if m:
#     #print m
#     #print"\n"
#     print len(m)
#     top.setData(m)
# else:  
#     wx.MessageBox('Download failed.', 'Message',  wx.OK | wx.ICON_INFORMATION)
