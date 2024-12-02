from PyQt5.QtWidgets import QDialog
import json

class Dialog(QDialog):
    def __init__(self, controles, widgets, comboBox):
        super().__init__()
        from GUI.nameprompt import Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Guardar Configuración")
        self.setGeometry(300, 300, 250, 150)
        self.controles = controles
        self.widgets = widgets
        self.comboBox = comboBox

    def aceptarguardar(self):
        nombreconfig = self.ui.nombreguardar.text()
        nueva_config = {nombreconfig: {}}
        for widget in self.widgets:
            nueva_config[nombreconfig][widget.objectName()] = widget.currentText()
        self.controles.update(nueva_config)
        with open("data/controllers.json", 'w') as file:
            json.dump(self.controles, file, indent=4)
        self.comboBox.clear()
        self.comboBox.addItems(self.controles.keys())