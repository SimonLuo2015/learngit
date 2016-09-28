#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
wxPython
'''

import wx
import quotespd

class ChangeDepthDialog(wx.Dialog):
    '''a new dialog'''
    # 模式对话框阻塞了别的窗口部件接收用户事件，直到该模式对话框被关闭。
    # 在它存在期间，用户一直被置于对话模式中。特别注意，不能根据外观来区别
    # 对话框（wx.Dialog）和框架（wx.Frame）。在wxPython中，对话框
    # 和框架间的区别不是基于他们的外观的，而主要是它们处理事件的办法的实质。
    def __init__(self, *args, **kw):
        super(ChangeDepthDialog, self).__init__(*args, **kw) 

        self.InitUI()
        self.SetSize((350, 200))
        self.SetTitle("Configure Data")
        
    def InitUI(self):
        # 5个可勾选的内容。
        self.option_list = ['open', 'close', 'high', 'low', 'volume']

        # 新建一个panel。
        pnl = wx.Panel(self)
        # 新建两个boxsizer，一个纵向，一个横向。
        # wx.BoxSizer：在一条水平或垂直线上的窗口部件的布局，当尺寸改变时，在控制窗口部件的行为上很灵活。
        # 通常用于嵌套的样式，可用于几乎任何类型的布局。
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # 创建一个名叫sb的静态框。
        sb = wx.StaticBox(pnl, label='Data Range')
        # wx.StaticBoxSizer是wx.BoxSizer的子类，它的构造函数要求的参数是（静态框）和方向。
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL) 

        # 下面的-1表示使用默认分配的id
        sbs.Add(wx.StaticText(pnl, -1, r'Start Date'))
        # 返回DatePickerCtrl。
        self.dc_start = wx.DatePickerCtrl(pnl, -1, style=wx.DP_DEFAULT, pos=(130, 70))
        # 将dc_start添加到sbs中。
        sbs.Add(self.dc_start)


        sbs.Add(wx.StaticText(pnl, -1, r'End Date'))
        self.dc_end = wx.DatePickerCtrl(pnl, -1, style=wx.DP_DROPDOWN, pos=(330, 70))
        sbs.Add(self.dc_end)

        # 将sbs关联到容器pnl面板。因为box sizer要嵌套，而box sizer只能作用与一个panel中。
        pnl.SetSizer(sbs)

        # 再新建一个panel，重新应用一个box sizer。
        pnl2 = wx.Panel(self)
        # 新建sb2的静态框
        sb2 = wx.StaticBox(pnl2, label='Data Set')
        # 基于sb2的静态框，新建一个静态box sizer布局。
        sbs2 = wx.StaticBoxSizer(sb2, orient=wx.VERTICAL)

        # 创建一组复选框，cb是check box的缩写。
        self.cb_list = []
        for l in self.option_list:
            # 新建一个cb的复选框。
            # wx.CheckBox(parent, id, label, pos=wx.DefaultPosition,
            #   size=wx.DefaultSize, style=0, name="checkBox")
            cb = wx.CheckBox(pnl2, -1, l) # originally 3 params: style=wx.RB_GROUP
            # 将复选框加入到sb2的布局中。
            sbs2.Add(cb)
            # 将cb复选框实例加入到列表。有什么作用？
            self.cb_list.append(cb)

        # 将sbs2的静态框布局关联到新建的容器pnl2面板上。
        pnl2.SetSizer(sbs2)

        # 在一个dialog下，有两个panel面板？？然后使用hbox来将两个panel进行横向排列？
        # 将两个面板加入到bhox的纵向box sizer中。
        # pnl与pnl2是
        hbox.Add(pnl)
        hbox.Add(pnl2)
       
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox.Add(hbox, proportion=1)
        vbox.Add(hbox2, 
            flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        # 看到了没有，这里是self被关联到vbox这个布局。
        # 这个box sizer是最高级的，其他的box sizer都是和下面的panel这些小的容器关联，都是下级。
        self.SetSizer(vbox)
        
        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
    
    def ShowDialog(self, code1):
        # 该方法用于指定准备展示那个公司的股票信息，将code1值获取到。
        # code1为代码，如IBM。
        self.code = code1
        self.Show(True)
        
    def OnClose(self, e):
        l = []
        for i, cb in enumerate(self.cb_list):
            if cb.GetValue():
                l.append(self.option_list[i])
        print l
        print self.code
        print self.dc_start.GetValue(), self.dc_end.GetValue()
        quotespd.PlotData(code=self.code, start=self.dc_start.GetValue(), end=self.dc_end.GetValue(), list=l)
        #self.Destroy()


def ConfigureData(codes):
    '''
    create a instance of ChangeDepthDialog class.
    :param codes:
    :return:
    '''
    # 新建一个app实例。
    print "codes in dialogs", codes
    ex = wx.wx.App(False)
    print "retrived the first code", codes[0]
    # 新建ChangeDepthDialog类型的实例。
    cd = ChangeDepthDialog(None)

    # 指定再跳出窗口要显示哪一个公司的股票信息。
    cd.ShowDialog(codes[0])
    ex.MainLoop()


if __name__ == '__main__':
    # app = wx.PySimpleApp()
    # app.MainLoop()
    # dialog = ChangeDepthDialog(None)
    # # # 显示模式对话框
    # result = dialog.ShowModal()
    # # if result == wx.ID_OK:
    # #     print 'OK'
    # # else:
    # #     print 'Cancel'
    # dialog.Destroy()

    codes = ['IBM']
    ConfigureData(codes)