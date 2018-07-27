#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wx

class Calculator(wx.Frame):


    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, 'File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 5, 5, 5)

        Button = (wx.Button(self, label = '0'))
        Button1 = (wx.Button(self, label = '1'))
        Button2 = (wx.Button(self, label = '2'))
        Button3 = (wx.Button(self, label = '3'))
        Button4 = (wx.Button(self, label = '4'))
        Button5 = (wx.Button(self, label = '5'))
        Button6 = (wx.Button(self, label = '6'))
        Button7 = (wx.Button(self, label = '7'))
        Button8 = (wx.Button(self, label = '8'))
        Button9 = (wx.Button(self, label = '9'))
        ButtonMultiply = (wx.Button(self, label = '*'))
        ButtonDivision = (wx.Button(self, label = '/'))
        ButtonSubtract = (wx.Button(self, label = '-'))
        ButtonPlus = (wx.Button(self, label = '+'))
        ButtonBackspace = (wx.Button(self, label = '<-'))
        ButtonEnter = (wx.Button(self, label = 'Enter'))

        self.Bind(wx.EVT_BUTTON, self.Button, zero)
        self.Bind(wx.EVT_BUTTON, self.Button1, one)
        self.Bind(wx.EVT_BUTTON, self.Button2, two)
        self.Bind(wx.EVT_BUTTON, self.Button3, three)
        self.Bind(wx.EVT_BUTTON, self.Button4, four)
        self.Bind(wx.EVT_BUTTON, self.Button5, five)
        self.Bind(wx.EVT_BUTTON, self.Button6, six)
        self.Bind(wx.EVT_BUTTON, self.Button7, seven)
        self.Bind(wx.EVT_BUTTON, self.Button8, eight)
        self.Bind(wx.EVT_BUTTON, self.Button9, nine)
        self.Bind(wx.EVT_BUTTON, self.ButtonDivision, enter)
        self.Bind(wx.EVT_BUTTON, self.ButtonMultiply, backspace)
        self.Bind(wx.EVT_BUTTON, self.ButtonSubtract, multiply)
        self.Bind(wx.EVT_BUTTON, self.ButtonPlus, add)
        self.Bind(wx.EVT_BUTTON, self.ButtonBackspace, divide)
        self.Bind(wx.EVT_BUTTON, self.ButtonEnter, subtract)

        self.res = wx.Button(self, label='0')
        self.res = wx.Button(self, label='1')
        self.res = wx.Button(self, label='2')
        self.res = wx.Button(self, label='3')
        self.res = wx.Button(self, label='4')
        self.res = wx.Button(self, label='5')
        self.res = wx.Button(self, label='6')
        self.res = wx.Button(self, label='7')
        self.res = wx.Button(self, label='8')
        self.res = wx.Button(self, label='9')
        self.res = wx.Button(self, label='<-')
        self.res = wx.Button(self, label='*')
        self.res = wx.Button(self, label='/')
        self.res = wx.Button(self, label='-')
        self.res = wx.Button(self, label='+')
        self.res = wx.Button(self, label='Enter')

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


    def Button1(self, event):
            self.display.WriteText("1")

def main():

    app = wx.App()
    ex = Calculator(None, title='Calculator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
