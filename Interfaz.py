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
        self.labelC = wx.StaticText(self,wx.ID_ANY, "Palabra a buscar:",pos=(30,325),size=(100,15))

        # Inputs
        self.text = wx.TextCtrl(self, wx.ID_ANY, pos=(150, 10), size=(180, 25), style = wx.TE_READONLY)
        self.result = wx.TextCtrl(self,wx.ID_ANY,pos=(20,60),size=(450,250),style=wx.TE_MULTILINE)
        self.word = wx.TextCtrl(self,wx.ID_ANY,pos = (145,320),size = (180,25))

        # Botones
        self.open = wx.Button(self, wx.ID_ANY, "Abrir", pos=(350, 10), size=(80, 30))
        self.open.Bind(wx.EVT_BUTTON,self.openFile)
        self.search = wx.Button(self, wx.ID_ANY, "Buscar", pos=(350, 320), size=(120, 30))
        self.search.Bind(wx.EVT_BUTTON,self.searchConcordance)


        self.Centre(True)
        self.Show()

    #Abrir explorador de archivos
    def openFile(self,event):
        dlg = wx.FileDialog(
            self, message="Seleccione un archivo",
            defaultDir=self.currentDirectory,
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                fileSelected = path
                self.text.SetLabelText(fileSelected)
        dlg.Destroy()

    #LLamada a la clase Concordance para operaciones dentro del archivo
    def searchConcordance(self,event):
        path = self.text.GetLabelText()
        word = self.word.GetValue()

        #Verificamos que se haya seleccionado el archivo
        if(self.checkIsNotEmpty(path)):
            if(self.checkIsNotEmpty(word)):
                self.result.Clear()
                self.word.Clear()

                text = Searcher()
                returnResult = (text.searchConc(path,word))
                #Hacemos el Split para mostrar de una manera mas ordenada los datos
                resSplit = returnResult.split("',")
                #print(returnResult)

                for i in resSplit:
                    self.result.AppendText(i + "\n")
            else:
                self.messageDetail("Escriba una palabra")
        else:
            self.messageDetail("Seleeciona un archivo")

    def checkIsNotEmpty(self,path):
        if not path:
            #Si esta vacia regresamos False para que no pase
            print("true")
            return False
        else:
            #Si se tiene algo regresamos True para que siga el proceso
            print("false")
            return True

    def messageDetail(self,message):
        wx.MessageBox(message, 'Error', wx.OK | wx.ICON_ERROR)


if __name__ == '__main__':
    app = wx.App()
    fr = MiFrame(None, -1, "wxPython App", size=(500, 400))
    app.MainLoop()


