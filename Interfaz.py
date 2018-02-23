import wx


class MiFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        # Etiquetas ...
        self.labelA = wx.StaticText(self, wx.ID_ANY, "Archivo seleccionado...", pos=(10, 15), size=(130, 15))
        self.labelB = wx.StaticText(self, wx.ID_ANY, "Resultado", pos=(200, 40), size=(80, 15))

        # Inputs
        self.text = wx.TextCtrl(self, wx.ID_ANY, pos=(150, 10), size=(180, 25))
        self.result = wx.TextCtrl(self,wx.ID_ANY,pos=(20,60),size=(450,250))

        # Botones
        self.suma = wx.Button(self, wx.ID_ANY, "Abrir", pos=(350, 10), size=(80, 30))
        self.suma = wx.Button(self, wx.ID_ANY, "Buscar", pos=(350, 320), size=(120, 30))

        self.Centre(True)
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    fr = MiFrame(None, -1, "wxPython App", size=(500, 400))
    app.MainLoop()

