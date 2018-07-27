#Math
"""    def Operations(self, lst):
    Powers(a , b)

    def Addition(a , b):
        return a + b

    def Multiplication(a , b):
        result = 0
        for x in range (b):
            result= result + a
        return result

    def Division(a , b):
        return a / b

    def Subtraction(a , b):
        return a - b

    def Powers(a , b):
        # 0 <= i <= (b-1)
        for i in range(b):
            if b > 0:
                b = b - 1
                answer = a * a
        print (answer)

def Operations(i):
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

"""#photoshop menu
import wx

########################################################################
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="wx.Menu Tutorial")

        self.panel = wx.Panel(self, wx.ID_ANY)

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        BlurringPicture = fileMenu.Append(wx.NewId(), "Blurring",
                                       "Blurs the picture")
        BrightenPicture = fileMenu.Append(wx.NewId(), "Brighten",
                                       "Brightens the picture")
        DarkenPicture = fileMenu.Append(wx.NewId(), "Darken",
                                       "Darkens the picture")
        GreyScalePicture = fileMenu.Append(wx.NewId(), "GreyScale",
                                       "Greys the picture")
        InvertPicture = fileMenu.Append(wx.NewId(), "Invert",
                                       "Inverts the picture")
        PosterizePicture = fileMenu.Append(wx.NewId(), "Posterize",
                                       "Posterizes the picture")
        SolarizePicture = fileMenu.Append(wx.NewId(), "Solarize",
                                       "Solarizes the picture")
        menuBar.Append(fileMenu, "&something")
        self.Bind(wx.EVT_MENU, self.Blur, BlurringPicture)
        self.Bind(wx.EVT_MENU, self.Bright, BrightenPicture)
        self.Bind(wx.EVT_MENU, self.Dark, DarkenPicture)
        self.Bind(wx.EVT_MENU, self.Grey, GreyScalePicture)
        self.Bind(wx.EVT_MENU, self.UpsideDown, InvertPicture)
        self.Bind(wx.EVT_MENU, self.Post, PosterizePicture)
        self.Bind(wx.EVT_MENU, self.Solar, SolarizePicture)
        self.SetMenuBar(menuBar)

    #----------------------------------------------------------------------
    def onExit(self, event):
        """"""
        self.Close()

#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()

"""#Darken
from PIL import Image

img = Image.open("dukelogo.png")
pixels = [(int(r * .75), int(g * .75), int(b * .75)) for (r,g,b) in img.getdata()]
img.putdata(pixels)
img.show()
"""
