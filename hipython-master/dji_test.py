# -*- coding:utf-8 -*-
import urllib
import re
import wx
import requests
from bs4 import BeautifulSoup 
from custom_dialogs import ConfigureData

# 下载道琼斯工业平均指数的前三位
# str = urllib.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components').read()
# 原来的yahoo英文站改版了，现在使用动态加载而不是原来的html表格版本的数据表示形式，
# 因而原来的正则表达式不能匹配，现在改用香港的雅虎财经页面
str = urllib.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI%27').read()
# # 验证过，这里str可以把网页源代码下载下来。
print str
# # 问题在这里，这个re的正则表达式已经没法匹配到数据了。
# m = re.findall("<tr><td class=\"yfnc_tabledata1\"><b><a href=\".*?\">(.*?)</a></b></td><td class=\"yfnc_tabledata1\">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>", str)
# # print m

# if m:
#     #print m
#     #print"\n"
#     print len(m)
#     top.setData(m)
# else:  
#     wx.MessageBox('Download failed.', 'Message',  wx.OK | wx.ICON_INFORMATION)


# 尝试使用requests模块来解决问题。
# r = requests.get('http://finance.yahoo.com/q/cp?s=%5EDJI+Components')
# print r.content

# 尝试使用BeautifulSoup来解决问题
# str = urllib.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components').read()
# # print str
# soup = BeautifulSoup(str)
# print(soup.prettify())

# 测试GUI图形界面能否正常显示
class StockFrame(wx.Frame):
    # 复用wx.Frame的__init__函数
    def __init__(self, title):
        # 调用super类的初始化函数
        wx.Frame.__init__(self, None, title=title, size=(500,600))

        # 增加最下面的状态栏
        self.CreateStatusBar()

        # 增加上面的菜单栏
        menuBar = wx.MenuBar()

        # 新增一个菜单
        filemenu= wx.Menu()
        # 将filemenu增加到菜单栏上，名称用&File标识。
        menuBar.Append(filemenu, "&File")
        
        # 在新增的菜单上，增加具体的about子菜单
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        # 在about子菜单下增加分隔符。
        filemenu.AppendSeparator()

        # 在新增加的菜单上，增加quit子菜单
        menuQuit = filemenu.Append(wx.ID_EXIT, "Q&uit", " Terminate the program")

        # 绑定两个子菜单的事件响应方法，就是说两个子菜单被触发了后会执行什么操作。
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.onQuit, menuQuit)

        # 将新增的菜单栏指定到本Frame下（self就是代表了本Frame）。
        self.SetMenuBar(menuBar)

        # 在本Frame下新建一个Panel（面板）
        panel = wx.Panel(self)

        # 指定boxsize的布局，是水平排列的。
        codeSizer = wx.BoxSizer(wx.HORIZONTAL)

        # 在panel下新建一个固定文本，显示Stock Code。
        labelText = wx.StaticText(panel, label="Stock Code:")
        # 指定labelText的布局，显示在哪里。
        codeSizer.Add(labelText, 0, wx.ALIGN_BOTTOM)
        codeSizer.Add((10, 10))
        # 在panel下新建一个文本框，默认显示AAPL。
        addressText = wx.TextCtrl(panel, value='AAPL')
        # 指定addressText的大小，使用了自适应大小。
        addressText.SetSize(addressText.GetBestFittingSize())
        # 在codeSizer布局下增加文本框。
        codeSizer.Add(addressText)
        #self.addressText.Layout()
        #self.control.Show(True)
        
        # 在panel下新增一个列表框，类别为报告样式。
        # 原来使用list作为对象属性，复用了list，不太合适，现在改为reportList
        self.reportList = wx.ListCtrl(panel, wx.NewId(), style=wx.LC_REPORT)
        # 列表框中增加第一至第三类，名称具体指定。
        self.reportList.InsertColumn(0,"Symbol")
        self.reportList.InsertColumn(1,"Name")
        self.reportList.InsertColumn(2,"Last Trade")  

        # 不太清楚，看起来是在第一列增加了字符数据，但是用pos来标识，比较怪异。
        pos = self.reportList.InsertStringItem(0,"--")
        self.reportList.SetStringItem(pos,1,"loading...")
        self.reportList.SetStringItem(pos,2,"--")  
        # 绑定列表框的响应方法。
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self.reportList)
        
        # 新建一个布局，为垂直布局。
        vsizer = wx.BoxSizer(wx.VERTICAL)
        # 将codeSizer布局也纳入到新建的vsizer中，布局一环一环进行控制。
        vsizer.Add(codeSizer, 0, wx.ALL, 10)
        vsizer.Add(self.reportList, -1, wx.ALL | wx.EXPAND, 10)
        #panel.SetSizer(self.sizer)

        # 再新建一个水平布局。
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        # 指定这个水平布局的使用点？？？
        hsizer.Add((10, 10))
        # 在panel下新增加Quit按钮
        buttonQuit = wx.Button(panel, -1, "Quit")
        # 绑定Quit按钮的响应方法。
        self.Bind(wx.EVT_BUTTON, self.onQuit, buttonQuit)
        # 设置该Quit按钮为默认设置？？？不太清楚具体作用。
        buttonQuit.SetDefault()
        # 将该按钮增加到水平布局中。
        hsizer.Add(buttonQuit, 1)

        # 在panel下新增Refresh按钮
        buttonRefresh = wx.Button(panel, -1, "Refresh")
        # 绑定Refresh函数的响应方法。
        self.Bind(wx.EVT_BUTTON, self.onRefresh, buttonRefresh)
        # 将该按钮增加到水平布局中。
        hsizer.Add(buttonRefresh, 1)
        #self.buttonGroupSizer.Layout()
        #self.buttonGroupSizer.Fit(self)
        # 将该水平布局增加上总的垂直布局中。
        vsizer.Add(hsizer, 0, wx.ALIGN_BOTTOM)
        #self.sizer.Layout()
        #vsizer.Fit(self)

        #self.buttonGroupSizer.Fit(self)
        ###self.SetSizer(self.buttonGroupSizer)
        # 将总的垂直布局指定给panel应用。
        panel.SetSizerAndFit(vsizer)  
        # panel进行展示。      
        panel.Layout()        
        #self.Show(True)
        
        '''frameSizer = wx.BoxSizer(wx.VERTICAL)
        frameSizer.Add(panel)
        self.SetSizerAndFit(frameSizer)
        self.Layout()
        self.Fit()'''

    def setData(self, data):
        # 设置列表框中的数据
        self.reportList.ClearAll()
        # 依然要先设置表头信息，需要注意。
        self.reportList.InsertColumn(0,"Symbol")
        self.reportList.InsertColumn(1,"Name")
        self.reportList.InsertColumn(2,"Last Trade")  

        # ？？？？？？
        pos = 0
        # 增加行
        for row in data:
            # This one looks neater but cannot replace the "&amp;"
            #self.list.Append(row) 
            # InsertStringItem(index, label) 插入文本到列表中。           
            pos = self.reportList.InsertStringItem(pos+1, row[0])
            self.reportList.SetStringItem(pos, 1, row[1].replace("&amp;", "&"))
            self.reportList.SetColumnWidth(1, -1)
            self.reportList.SetStringItem(pos, 2, row[2])
            if (pos % 2 == 0):
                # Get the item at a specific index:
                #item = self.list.GetItem(pos)
                self.reportList.SetItemBackgroundColour(pos, (134, 225, 249))
                # Set new look and feel back to the list
                #self.list.SetItem(item)
        # 调整window尺寸以匹配sizer认为所需要的最小化尺寸，参数值通常使用sizer窗口。
        # FtiInside()是类似方法，只不过将改变窗口在屏幕上的显示替换为只改变他的内部实现，
        # 它用于scroll panel中的窗口以出发滚动栏的显示。
        self.FitInside()
        
    def GetAllSelected(self):
        selection = []

        # start at -1 to get the first selected item
        current = -1
        while True:
            next = self.GetNextSelected(current)
            if next == -1:
                return selection

            selection.append(self.reportList.GetItemText(next))
            current = next

    def GetNextSelected(self, current):
        return self.reportList.GetNextItem(current,
                                wx.LIST_NEXT_ALL,
                                wx.LIST_STATE_SELECTED)

    def OnClick(self, event):
        codes = self.GetAllSelected()
        print "code in DJI", codes
        ConfigureData(codes)
        
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def onQuit(self, event):
        self.Close()
        self.Destroy()
        
    # onRefresh函数需要重写，保证实现刷新重写读取
    def onRefresh(self, event):
        pass




if __name__ == '__main__':

    app = wx.App(False)

    top = StockFrame("Dow Jones Industrial Average (^DJI)")
    top.Show(True)

    # # 下载道琼斯工业平均指数的前三位
    # str = urllib.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components').read()
    # #print str
    # m = re.findall("<tr><td class=\"yfnc_tabledata1\"><b><a href=\".*?\">(.*?)</a></b></td><td class=\"yfnc_tabledata1\">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>", str)
    # if m:
    #     #print m
    #     #print"\n"
    #     print len(m)
    #     top.setData(m)
    # else:  
    #     wx.MessageBox('Download failed.', 'Message',  wx.OK | wx.ICON_INFORMATION)


    app.MainLoop()