import wx
import os
from Concordancias import Searcher

wildcard = "Text File (*.txt)|*.txt|" \
            "All files (*.*)|*.*"
fileSelected = "";


class MiFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.currentDirectory = os.getcwd()


        # Etiquetas ...
        self.labelA = wx.StaticText(self, wx.ID_ANY, "Archivo seleccionado...", pos=(10, 15), size=(130, 15))
        self.labelB = wx.StaticText(self, wx.ID_ANY, "Resultado", pos=(200, 40), size=(80, 15))

        # Inputs
        self.text = wx.TextCtrl(self, wx.ID_ANY, pos=(150, 10), size=(180, 25))
        self.result = wx.TextCtrl(self,wx.ID_ANY,pos=(20,60),size=(450,250))

        # Botones
        self.open = wx.Button(self, wx.ID_ANY, "Abrir", pos=(350, 10), size=(80, 30))
        self.open.Bind(wx.EVT_BUTTON,self.OpenFile)
        self.search = wx.Button(self, wx.ID_ANY, "Buscar", pos=(350, 320), size=(120, 30))
        self.search.Bind(wx.EVT_BUTTON,self.SearchConcordance)


        self.Centre(True)
        self.Show()

    #Abrir explorador de archivos
    def OpenFile(self,event):
        dlg = wx.FileDialog(
            self, message="Seleccione un archivo",
            defaultDir=self.currentDirectory,
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print ("Archivo seleccionado")
            for path in paths:
                fileSelected = path
                self.text.SetLabelText(fileSelected)
        dlg.Destroy()

    def SearchConcordance(self,event):
        print(self.text.GetLabelText())
        path = self.text.GetLabelText()
        text = Searcher()
        print(text.readFile(path))


if __name__ == '__main__':
    app = wx.App()
    fr = MiFrame(None, -1, "wxPython App", size=(500, 400))
    app.MainLoop()

