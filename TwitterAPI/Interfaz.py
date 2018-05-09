import wx
import os
from geopy.geocoders import Nominatim
from APICall import APISearcher


class MiFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        states = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Chiapas',
                  'Chihuahua', 'Ciudad de México', 'Coahuila', 'Colima', 'Durango', 'Chiapas', 'Guanajuato',
                  'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León',
                  'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco',
                  'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas'
        ]


        # Etiquetas ...
        self.labelA = wx.StaticText(self, wx.ID_ANY, "Resultado", pos=(200, 10), size=(80, 15))
        self.labelB = wx.StaticText(self,wx.ID_ANY, "Estado:",pos=(20,308   ),size=(40,15))

        # Inputs
        self.result = wx.TextCtrl(self,wx.ID_ANY,pos=(20,30),size=(450,250),style=wx.TE_MULTILINE)

        # Botones
        self.search = wx.Button(self, wx.ID_ANY, "Buscar", pos=(260, 297), size=(100, 30))
        self.search.Bind(wx.EVT_BUTTON,self.searchTweets)
        self.saveBtn = wx.Button(self, wx.ID_ANY, "Guardar", pos=(375, 297), size=(100, 30))
        self.saveBtn.Bind(wx.EVT_BUTTON,self.saveTweets)
        self.saveBtn.Disable()


        #ComboBox
        self.comboBox = wx.ComboBox(self,wx.ID_ANY,pos = (70,305),size = (180,25), choices = states ,style=wx.CB_READONLY)

        self.Centre(True)
        self.Show()

    def searchTweets(self,event):
        call = APISearcher()
        stateSelection = self.comboBox.GetStringSelection()
        tweets = call.Search(stateSelection,10);
        self.result.AppendText(tweets)

    def saveTweets():
        print("Save")


if __name__ == '__main__':
    app = wx.App()
    saveFile = open('tweetFile.txt', 'a', encoding='utf-8')
    fr = MiFrame(None, -1, "Twitter API", size=(500, 400))
    app.MainLoop()


