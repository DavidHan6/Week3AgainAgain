import wx
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="wx.Photoshop UI")

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

        menuBar.Append(fileMenu, "&Filters")
        self.Bind(wx.EVT_MENU, self.Blur, BlurringPicture)
        self.Bind(wx.EVT_MENU, self.Bright, BrightenPicture)
        self.Bind(wx.EVT_MENU, self.Dark, DarkenPicture)
        self.Bind(wx.EVT_MENU, self.Grey, GreyScalePicture)
        self.Bind(wx.EVT_MENU, self.UpsideDown, InvertPicture)
        self.Bind(wx.EVT_MENU, self.Post, PosterizePicture)
        self.Bind(wx.EVT_MENU, self.Solar, SolarizePicture)
        self.SetMenuBar(menuBar)

    def onExit(self, event):
        """"""
        self.Close()
