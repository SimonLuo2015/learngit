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
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        sb = wx.StaticBox(pnl, label='Data Range')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL) 

        # 下面的-1表示使用默认分配的id
        sbs.Add(wx.StaticText(pnl, -1, r'Start Date'))
        self.dc_start = wx.DatePickerCtrl(pnl, -1, style=wx.DP_DROPDOWN, pos=(130, 70))
        sbs.Add(self.dc_start)
        sbs.Add(wx.StaticText(pnl, -1, r'End Date'))
        self.dc_end = wx.DatePickerCtrl(pnl, -1, style=wx.DP_DROPDOWN, pos=(330, 70))
        sbs.Add(self.dc_end)
        pnl.SetSizer(sbs)

        pnl2 = wx.Panel(self)
        sb2 = wx.StaticBox(pnl2, label='Data Set')
        sbs2 = wx.StaticBoxSizer(sb2, orient=wx.VERTICAL)        
        self.cb_list = []
        for l in self.option_list:
            cb = wx.CheckBox(pnl2, label = l) # originally 3 params: style=wx.RB_GROUP
            sbs2.Add(cb)
            self.cb_list.append(cb)
        
         
        pnl2.SetSizer(sbs2)
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

        self.SetSizer(vbox)
        
        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
    
    def ShowDialog(self, code1):
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
        quotespd.PlotData(code = self.code, start = self.dc_start.GetValue(), end = self.dc_end.GetValue(), list = l)
        #self.Destroy()
#
# def ConfigureData(codes):
#     print "codes in dialogs", codes
#     ex = wx.App()
#     print "retrived the first code", codes[0]
#     cd = ChangeDepthDialog(None)
#     cd.ShowDialog(codes[0])
#     ex.MainLoop()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    app.MainLoop()
    dialog = ChangeDepthDialog(None)
    # # 显示模式对话框
    result = dialog.ShowModal()
    # if result == wx.ID_OK:
    #     print 'OK'
    # else:
    #     print 'Cancel'
    dialog.Destroy()