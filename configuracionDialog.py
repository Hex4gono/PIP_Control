from PyQt5.QtWidgets import QDialog
import json
from GUI.config import Ui_Configuracion


class ConfiguracionDialog(QDialog):
    def __init__(self, configDict):
        super().__init__()
        self.ui = Ui_Configuracion()
        self.ui.setupUi(self)
        self.setGeometry(300, 300, 300, 100)
        print(configDict)
        self.ui.sensibilidadLabel.setText(configDict["sensibilidad"])
        self.ui.ZMLineEdit.setText(configDict["zona muerta"])

    def sensibilidadSelecField(self):
        pass
    
    def sensibilidadSelecSlider(self):
        pass

    def ZMSelecField(self):
        pass

    def ZMSelecSlider(self):
        pass    
    
    def guardarConfig(self):
        pass    