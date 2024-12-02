from PyQt5.QtWidgets import QDialog
import json
from GUI.config import Ui_Configuracion

class ConfiguracionDialog(QDialog):
    def __init__(self, configDict):
        super().__init__()
        self.ui = Ui_Configuracion()
        self.ui.setupUi(self)
        self.setGeometry(300, 300, 300, 100)
        self.configDict = configDict

        
        self.sens = configDict["sensibilidad"]
        self.zm = configDict["zona muerta"]
        
        self.ui.sensibilidadLineEdit.setText(str(self.sens))
        self.ui.ZMLineEdit.setText(str(self.zm))
        
        self.ui.sensibilidadSlider.setValue(self.sens)
        self.ui.ZMSlider.setValue(self.zm)

    def sensibilidadSelecField(self):
        txt = self.ui.sensibilidadLineEdit # para abreviar nomas
        try:
            self.sens = int(txt.text())
        except ValueError:
            txt.setText(str(self.sens))
            return
        
        if self.sens < 1 or self.sens > 200:
            return
        
        self.ui.sensibilidadSlider.setValue(self.sens)
            
    
    def sensibilidadSelecSlider(self):
        self.sens = self.ui.sensibilidadSlider.value()
        
        self.ui.sensibilidadLineEdit.setText(str(self.sens))

    def ZMSelecField(self):
        yo = self.ui.ZMLineEdit # para abreviar nomas
        
        try:
            self.zm = int(yo.text())
        except ValueError:
            yo.setText(str(self.zm))
            return
        
        if self.zm < 5:
            yo.setText("5")

        if self.zm > 550:
            yo.setText("550")

        
        self.ui.ZMSlider.setValue(self.zm)

    def ZMSelecSlider(self):
        self.zm = self.ui.ZMSlider.value()
        self.ui.ZMLineEdit.setText(str(self.zm))  
    
    def guardarConfig(self):
        
        with open("data/config.json", "w") as file:
            self.configDict = {"sensibilidad" : self.sens, "zona muerta" : self.zm}
            json.dump(self.configDict, file, indent = 4)
            
        self.close()