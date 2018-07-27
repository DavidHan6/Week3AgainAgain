import wx
app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,50)
# Create open file dialog
openFileDialog = wx.FileDialog(frame, "Open", "", "",
"PNG files (*.png)|*.png",
wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

openFileDialog.ShowModal()
print(openFileDialog.GetPath())
i = openFileDialog.GetPath()

########################################################################
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

    #----------------------------------------------------------------------
    def Blur(self, event, i):
        from PIL import Image
        from PIL import ImageFilter
        original_image = str(i)
        original_image = Image.open(original_image)
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=5))
        blurred_image.show()

        blurImage('noise.png')

    def Bright(self, event):
        from PIL import Image

        img = Image.open("dukelogo.png")
        pixels = [(int(r * 1.25), int(g * 1.25), int(b * 1.25)) for (r,g,b) in img.getdata()]
        img.putdata(pixels)
        img.show()

    def Dark(self, event):
        from PIL import Image

        img = Image.open("dukelogo.png")
        pixels = [(int(r * .75), int(g * .75), int(b * .75)) for (r,g,b) in img.getdata()]
        img.putdata(pixels)
        img.show()

    def Grey(self, event):
        from PIL import Image

        img = Image.open("dukelogo.png")
        pixels = [(int(r), int(g), int(b)) for (r,g,b) in img.getdata()]
        new_pixels = []
        for (r, g, b) in pixels:
            grey = int((r+g+b)/3.0)
            new_pixel = (grey, grey, grey)
            new_pixels.append(new_pixel)
        img.putdata(new_pixels)
        img.show()

    def UpsideDown(self, event):
        from PIL import Image

        img = Image.open("dukelogo.png")
        pixels = [(int(255 - r), int(255 - g), int(255 - b)) for (r,g,b) in img.getdata()]
        img.putdata(pixels)
        img.show()

    def Post(self, event):
        from PIL import Image

        img = Image.open("vases.png")

        pixels = [(int(r), int(g), int(b), int(a)) for (r,g,b,a) in img.getdata()]
        new_pixels = []
        for (r,g,b,a) in pixels:
            if r >= 0 and r <= 63:
                great = 50
            elif r >= 64 and r <= 127:
                great = 100
            elif r >= 128 and r <= 191:
                great = 150
            elif r >= 192 and r <= 255:
                great = 200

            if g >= 0 and g <= 63:
                brown = 50
            elif g >= 64 and g <= 127:
                brown = 100
            elif g >= 128 and g <= 191:
                brown = 150
            elif g >= 192 and g <= 255:
                brown = 200

            if b >= 0 and b <= 63:
                shit = 50
            elif b >= 64 and b <= 127:
                shit = 100
            elif b >= 128 and b <= 191:
                shit = 150
            elif b >= 192 and b <= 255:
                shit = 200
            new_pixel = (great, brown, shit)
            new_pixels.append(new_pixel)
        img.putdata(new_pixels)
        img.show()
    def Solar(self, event):
        from PIL import Image

        img = Image.open("dukelogo.png")
        pixels = [(int(r), int(g), int(b)) for (r,g,b) in img.getdata()]
        new_pixel = []
        for (r,g,b) in pixels:
            if r < 128:
                r = 255 - r
            if g < 128:
                g = 255 - g
            if b < 128:
                b = 255 - b
            new_pixels = (r, g, b)
            new_pixel.append(new_pixels)
        img.putdata(new_pixel)
        img.show()

#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()
