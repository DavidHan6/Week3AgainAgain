import wx

class Calculator(wx.Frame):
    Numberos = []
    def find(self, mom, dad):
        i = 0
        while i < len(mom):
            if mom [i] == dad:
                return [True, i]
            i += 1
        return [False, None]

    def Operations(self, i):
        def Addition(a, b):
            Answer = a + b
            return Answer

        def Subtraction(a, b):
            Answer = a - b
            return Answer

        def Multiplication(a, b):
            result = a * b
            return result

        def Division(a, b):
            result = a / b
            return result

        def Exponents(a, b):
            Answer = a**b
            return Answer

        def MinMax(a, b):
            Numbers = []
            active == True
            while active == True:
                i = int(input("Enter number"))
                h = input("To stop enter 'stop. To continue enter 'Continue'")
                Numbers.append(i)
                if h == 'Stop':
                    active = False
                elif h == 'Continue':
                    active = True
                    ha = sorted(Numbers)
                    print(ha)
                    print("min = " + str(ha[0]))
                    print("max = " + str(ha[-1]))

        if self.find (i, "+") [0]:
            goku = ""
            ii = 0
            q = self.find (i, "+")
            while (ii < int(q[1])):
                goku = goku + i[ii]
                ii+=1
            iii = ""
            ii+=1
            while (ii < len(i)):
                iii = iii + i[ii]
                ii+=1
                print(goku, iii)
                print(Addition(int(goku), int(iii)))

            self.display.WriteText(str(Addition(int(goku), int(iii))))

        if self.find (i, "-") [0]:
            goku = ""
            ii = 0
            q = self.find (i, "-")
            while (ii < int(q[1])):
                goku = goku + i[ii]
                ii+=1
            iii = ""
            ii+=1
            while (ii < len(i)):
                iii = iii + i[ii]
                ii+=1
                print(goku, iii)
                print(Subtraction(int(goku), int(iii)))

            self.display.WriteText(str(Subtraction(int(goku), int(iii))))

        if self.find (i, "/") [0]:
            goku = ""
            ii = 0
            q = self.find (i, "/")
            while (ii < int(q[1])):
                goku = goku + i[ii]
                ii+=1
            iii = ""
            ii+=1
            while (ii < len(i)):
                iii = iii + i[ii]
                ii+=1
                print(goku, iii)
                print(Division(int(goku), int(iii)))

            self.display.WriteText(str(Division(int(goku), int(iii))))

        if self.find (i, "*") [0]:
            goku = ""
            ii = 0
            q = self.find (i, "*")
            while (ii < int(q[1])):
                goku = goku + i[ii]
                ii+=1
            iii = ""
            ii+=1
            while (ii < len(i)):
                iii = iii + i[ii]
                ii+=1
                print(goku, iii)
                print(Multiplication(int(goku), int(iii)))

            self.display.WriteText(str(Multiplication(int(goku), int(iii))))


    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.btn1 = wx.Button(self, label='C')
        self.btn2 = wx.Button(self, label='CC')
        self.btn3 = wx.Button(self, label='<-')
        self.btn5 = wx.Button(self, label='Bin to Dec')
        self.btn6 = wx.Button(self, label='7')
        self.btn7 = wx.Button(self, label='8')
        self.btn8 = wx.Button(self, label='9')
        self.btn9 = wx.Button(self, label='/')
        self.btn10 = wx.Button(self, label='Dec to Oct')
        self.btn11 = wx.Button(self, label='4')
        self.btn12 = wx.Button(self, label='5')
        self.btn13 = wx.Button(self, label='6')
        self.btn14 = wx.Button(self, label='*')
        self.btn15 = wx.Button(self, label='Dec to Hex')
        self.btn16 = wx.Button(self, label='1')
        self.btn17 = wx.Button(self, label='2')
        self.btn18 = wx.Button(self, label='3')
        self.btn19 = wx.Button(self, label='-')
        self.btn20 = wx.Button(self, label='0')
        self.btn21 = wx.Button(self, label='.')
        self.btn22 = wx.Button(self, label='=')
        self.btn23 = wx.Button(self, label='+')

        self.btn1.Bind(wx.EVT_BUTTON,self.OnClicked1)
        self.btn2.Bind(wx.EVT_BUTTON,self.OnClicked2)
        self.btn3.Bind(wx.EVT_BUTTON,self.OnClicked3)
        self.btn5.Bind(wx.EVT_BUTTON,self.OnClicked5)
        self.btn6.Bind(wx.EVT_BUTTON,self.OnClicked6)
        self.btn7.Bind(wx.EVT_BUTTON,self.OnClicked7)
        self.btn8.Bind(wx.EVT_BUTTON,self.OnClicked8)
        self.btn9.Bind(wx.EVT_BUTTON,self.OnClicked9)
        self.btn10.Bind(wx.EVT_BUTTON,self.OnClicked10)
        self.btn11.Bind(wx.EVT_BUTTON,self.OnClicked11)
        self.btn12.Bind(wx.EVT_BUTTON,self.OnClicked12)
        self.btn13.Bind(wx.EVT_BUTTON,self.OnClicked13)
        self.btn14.Bind(wx.EVT_BUTTON,self.OnClicked14)
        self.btn15.Bind(wx.EVT_BUTTON,self.OnClicked15)
        self.btn16.Bind(wx.EVT_BUTTON,self.OnClicked16)
        self.btn17.Bind(wx.EVT_BUTTON,self.OnClicked17)
        self.btn18.Bind(wx.EVT_BUTTON,self.OnClicked18)
        self.btn19.Bind(wx.EVT_BUTTON,self.OnClicked19)
        self.btn20.Bind(wx.EVT_BUTTON,self.OnClicked20)
        self.btn21.Bind(wx.EVT_BUTTON,self.OnClicked21)
        self.btn22.Bind(wx.EVT_BUTTON,self.OnClicked22)
        self.btn23.Bind(wx.EVT_BUTTON,self.OnClicked23)


        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 5, 5, 5)

        gs.AddMany( [(self.btn1, 0, wx.EXPAND),
            (self.btn2, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (self.btn3, 0, wx.EXPAND),
            (self.btn5, 0, wx.EXPAND),
            (self.btn6, 0, wx.EXPAND),
            (self.btn7, 0, wx.EXPAND),
            (self.btn8, 0, wx.EXPAND),
            (self.btn9, 0, wx.EXPAND),
            (self.btn10, 0, wx.EXPAND),
            (self.btn11, 0, wx.EXPAND),
            (self.btn12, 0, wx.EXPAND),
            (self.btn13, 0, wx.EXPAND),
            (self.btn14, 0, wx.EXPAND),
            (self.btn15, 0, wx.EXPAND),
            (self.btn16, 0, wx.EXPAND),
            (self.btn17, 0, wx.EXPAND),
            (self.btn18, 0, wx.EXPAND),
            (self.btn19, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (self.btn20, 0, wx.EXPAND),
            (self.btn21, 0, wx.EXPAND),
            (self.btn22, 0, wx.EXPAND),
            (self.btn23, 0, wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


    def OnQuit(self, e):
        self.Close()

    def OnClicked1(self, event):
        self.display.WriteText("C")
        self.Numberos += "C"
    def OnClicked2(self, event):
        self.display.WriteText("CC")
        self.Numberos += "CC"
    def OnClicked3(self, event):
        self.display.WriteText(" ")
        self.Numberos += "Backspace"
    def OnClicked5(self, event):
        self.display.WriteText("Binary to Dec")
        self.Numberos += "Bin to Dec"
    def OnClicked6(self, event):
        self.display.WriteText("7")
        self.Numberos += "7"
    def OnClicked7(self, event):
        self.display.WriteText("8")
        self.Numberos += "8"
    def OnClicked8(self, event):
        self.display.WriteText("9")
        self.Numberos += "9"
    def OnClicked9(self, event):
        self.display.WriteText("/")
        self.Numberos += "/"
    def OnClicked10(self, event):
        self.display.WriteText("Decimal to Oct")
        self.Numberos += "Dec to Oct"
    def OnClicked11(self, event):
        self.display.WriteText("4")
        self.Numberos += "4"
    def OnClicked12(self, event):
        self.display.WriteText("5")
        self.Numberos += "5"
    def OnClicked13(self, event):
        self.display.WriteText("6")
        self.Numberos += "6"
    def OnClicked14(self, event):
        self.display.WriteText("*")
        self.Numberos += "*"
    def OnClicked15(self, event):
        self.display.WriteText("Decimal to Hex")
        self.Numberos += "Dec to Hex"
    def OnClicked16(self, event):
        self.display.WriteText("1")
        self.Numberos += "1"
    def OnClicked17(self, event):
        self.display.WriteText("2")
        self.Numberos += "2"
    def OnClicked18(self, event):
        self.display.WriteText("3")
        self.Numberos += "3"
    def OnClicked19(self, event):
        self.display.WriteText("-")
        self.Numberos += "-"
    def OnClicked20(self, event):
        self.display.WriteText("0")
        self.Numberos += "0"
    def OnClicked21(self, event):
        self.display.WriteText(".")
        self.Numberos += "."
    def OnClicked22(self, event):
        self.display.WriteText("=")
        self.Numberos += ""
        self.Operations(self.Numberos)
    def OnClicked23(self, event):
        self.Numberos += "+"
        self.display.WriteText("+")

def main():

    app = wx.App()
    ex = Calculator(None, title="Calculator")
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
