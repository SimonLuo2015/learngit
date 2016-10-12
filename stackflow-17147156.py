import wx
import random

class welkom(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Aminozuurtoets V.1.0", size=(900,600))
        self.mainFrame = mainFrame

        top_panel = wx.Panel(self)
        w_tekst = wx.StaticText(top_panel, -1, "Welkom bij de aminozuurtoets",(325,50), (100, -1), wx.ALIGN_CENTER)
        w_font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        w_tekst.SetFont(w_font)

        st_nr = wx.StaticText(top_panel, -1, 'Studentnummer' ,(100,150))
        inp_st_nr = wx.TextCtrl(top_panel, -1, '', (300,150), size=(140,-1))
        st_vr= wx.StaticText(top_panel, -1, 'Student voornaam' ,(100,200))
        inp_st_vr = wx.TextCtrl(top_panel, -1, '', (300,200), size=(140,-1))
        st_ach = wx.StaticText(top_panel, -1, 'Student achternaam' ,(100,250))
        inp_st_ach = wx.TextCtrl(top_panel, -1, '', (300,250), size=(140,-1))
        aan_vr = wx.StaticText(top_panel, -1, 'Aantal vragen' ,(100,300))
        inp_aan_vr = wx.TextCtrl(top_panel, -1, '20', (300,300), size=(140,-1))

        close_button = wx.Button(top_panel, label = "Stoppen", pos=(600, 400), size=(150, 200))
        self.Bind(wx.EVT_BUTTON, self.closebutton, close_button)
        go_button = wx.Button(top_panel, label = "Doorgaan", pos=(100, 400), size=(150, 200))
        self.Bind(wx.EVT_BUTTON, self.buttonClick, go_button)

    def closebutton(self, event):
        self.Close(True)

    def buttonClick(self, event):
        self.Hide()
        self.mainFrame(None, id = -1).Show()

class mainFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Aminozuurtoets V.1.0", size=(900,600))

        top_panel = wx.Panel(self)
        self.vraag = 1
        m_tekst = wx.StaticText(top_panel, -1, "Vraag " + str(self.vraag),(400,50), (100, -1), wx.ALIGN_CENTER)
        m_font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        m_tekst.SetFont(m_font)

        cijfer = random.randint(1,100)


        test2 = wx.StaticText(top_panel, -1, str(cijfer), (325,300))

        res_but = wx.Button(top_panel, label = "Resultaten", pos=(650, 400), size=(150, 200))
        ga_naar = wx.Button(top_panel, label = "Ga naar vraag", pos=(100, 400), size=(150, 200))
        ga_button = wx.Button(top_panel, label = "Volgende vraag", pos=(380, 400), size=(150, 200))
        self.Bind(wx.EVT_BUTTON, self.buttonClick1, ga_button)

    def buttonClick1(self, event):
        self.Update()


    def closebutton(self, event):
        self.Close(True)

app = wx.App()
frame = welkom(None, id = -1).Show()
app.MainLoop()