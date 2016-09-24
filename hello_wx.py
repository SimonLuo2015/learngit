# -*- coding:utf-8 -*-
'''Hello, wxPython! program.'''
import wx

class Frame(wx.Frame):
    '''Frame class that display an image.'''

    def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title='Hello, wxPython!'):
        '''create a Frame instance and display image.'''
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)

class App(wx.App):
    '''Application class'''
    
    def OnInit(self):
        '''Init the app'''
        image = wx.Image('googlelogo.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)

        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App()
    app.MainLoop

if __name__ == '__main__':
    main()
    