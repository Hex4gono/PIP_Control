from PyQt5.QtWidgets import QDialog
import json

class ConfirmarDialog(QDialog):
    def __init__(self, controles, comboBox):
        super().__init__()
        from GUI.promptconfirmar import Ui_ConfirmarDialog
        self.ui = Ui_ConfirmarDialog()
        self.ui.setupUi(self)
        self.setGeometry(300, 300, 300, 100)
        self.controles = controles
        self.comboBox = comboBox

    def eliminacionConfirmada(self):
        self.controles.pop(self.comboBox.currentText())
        with open("data/controllers.json", 'w') as file:
            json.dump(self.controles, file, indent=4)
        self.comboBox.clear()
        self.comboBox.addItems(self.controles.keys())
