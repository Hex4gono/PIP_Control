from PyQt5.QtWidgets import QDialog
import json
from GUI.promptconfirmar import Ui_ConfirmarDialog

class ConfirmarDialog(QDialog):
    def __init__(self, controles, comboBox):
        super().__init__()

        self.ui = Ui_ConfirmarDialog()
        self.ui.setupUi(self)
        self.setGeometry(300, 300, 300, 100)
        self.controles = controles
        self.comboBox = comboBox

    def eliminacionConfirmada(self):
        try:
            self.controles.pop(self.comboBox.currentText())
            with open("data/controllers.json", 'w') as file:
                json.dump(self.controles, file, indent=4)
            self.comboBox.clear()
            self.comboBox.addItems(self.controles.keys())
        except AttributeError:
            pass