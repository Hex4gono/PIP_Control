# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'promptconfirmar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfirmarDialog(object):
    def setupUi(self, ConfirmarDialog):
        ConfirmarDialog.setObjectName("ConfirmarDialog")
        ConfirmarDialog.resize(400, 304)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfirmarDialog)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 260, 351, 21))
        self.buttonBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ConfirmarDialog)
        self.label.setGeometry(QtCore.QRect(16, 34, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(ConfirmarDialog)
        self.buttonBox.accepted.connect(ConfirmarDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ConfirmarDialog.reject) # type: ignore
        self.buttonBox.accepted.connect(ConfirmarDialog.eliminacionConfirmada) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ConfirmarDialog)

    def retranslateUi(self, ConfirmarDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfirmarDialog.setWindowTitle(_translate("ConfirmarDialog", "Confirmar eliminación"))
        self.label.setText(_translate("ConfirmarDialog", "¿Confirmar eliminación de control?"))
