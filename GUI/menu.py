# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(7, 10, 861, 551))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.AppLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.AppLayout.setContentsMargins(0, 0, 0, 0)
        self.AppLayout.setObjectName("AppLayout")
        self.ConfigBox = QtWidgets.QHBoxLayout()
        self.ConfigBox.setObjectName("ConfigBox")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SearchInputField = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchInputField.sizePolicy().hasHeightForWidth())
        self.SearchInputField.setSizePolicy(sizePolicy)
        self.SearchInputField.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SearchInputField.setFont(font)
        self.SearchInputField.setPlaceholderText("")
        self.SearchInputField.setObjectName("SearchInputField")
        self.verticalLayout.addWidget(self.SearchInputField)
        self.controlesComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlesComboBox.sizePolicy().hasHeightForWidth())
        self.controlesComboBox.setSizePolicy(sizePolicy)
        self.controlesComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.controlesComboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.controlesComboBox.setFont(font)
        self.controlesComboBox.setObjectName("controlesComboBox")
        self.verticalLayout.addWidget(self.controlesComboBox)
        self.ConfigBox.addLayout(self.verticalLayout)
        self.AlphaSortButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AlphaSortButton.sizePolicy().hasHeightForWidth())
        self.AlphaSortButton.setSizePolicy(sizePolicy)
        self.AlphaSortButton.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AlphaSortButton.setFont(font)
        self.AlphaSortButton.setObjectName("AlphaSortButton")
        self.ConfigBox.addWidget(self.AlphaSortButton)
        self.guardarButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.guardarButton.setFont(font)
        self.guardarButton.setObjectName("guardarButton")
        self.ConfigBox.addWidget(self.guardarButton)
        self.borrarButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.borrarButton.setFont(font)
        self.borrarButton.setObjectName("borrarButton")
        self.ConfigBox.addWidget(self.borrarButton)
        self.cargarButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cargarButton.setFont(font)
        self.cargarButton.setObjectName("cargarButton")
        self.ConfigBox.addWidget(self.cargarButton)
        self.AppLayout.addLayout(self.ConfigBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.AppLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.AppLayout.addLayout(self.horizontalLayout_5)
        self.JSBox = QtWidgets.QHBoxLayout()
        self.JSBox.setObjectName("JSBox")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.JSBox.addItem(spacerItem1)
        self.JSI = QtWidgets.QGridLayout()
        self.JSI.setObjectName("JSI")
        self.L3Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.L3Sel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.L3Sel.setFont(font)
        self.L3Sel.setObjectName("L3Sel")
        self.JSI.addWidget(self.L3Sel, 1, 1, 1, 1)
        self.XNegCar = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.XNegCar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.XNegCar.setFont(font)
        self.XNegCar.setObjectName("XNegCar")
        self.JSI.addWidget(self.XNegCar, 1, 0, 1, 1)
        self.YPosCar = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.YPosCar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.YPosCar.setFont(font)
        self.YPosCar.setObjectName("YPosCar")
        self.JSI.addWidget(self.YPosCar, 0, 1, 1, 1)
        self.YNegCar = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.YNegCar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.YNegCar.setFont(font)
        self.YNegCar.setObjectName("YNegCar")
        self.JSI.addWidget(self.YNegCar, 2, 1, 1, 1)
        self.XPosCar = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.XPosCar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.XPosCar.setFont(font)
        self.XPosCar.setObjectName("XPosCar")
        self.JSI.addWidget(self.XPosCar, 1, 2, 1, 1)
        self.JSBox.addLayout(self.JSI)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.JSBox.addItem(spacerItem2)
        self.JSI_2 = QtWidgets.QGridLayout()
        self.JSI_2.setObjectName("JSI_2")
        self.R3Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.R3Sel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.R3Sel.setFont(font)
        self.R3Sel.setObjectName("R3Sel")
        self.JSI_2.addWidget(self.R3Sel, 1, 1, 1, 1)
        self.YPosCar_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.YPosCar_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.YPosCar_2.setFont(font)
        self.YPosCar_2.setObjectName("YPosCar_2")
        self.JSI_2.addWidget(self.YPosCar_2, 0, 1, 1, 1)
        self.YNegCar_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.YNegCar_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.YNegCar_2.setFont(font)
        self.YNegCar_2.setObjectName("YNegCar_2")
        self.JSI_2.addWidget(self.YNegCar_2, 2, 1, 1, 1)
        self.XPosCar_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.XPosCar_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.XPosCar_2.setFont(font)
        self.XPosCar_2.setObjectName("XPosCar_2")
        self.JSI_2.addWidget(self.XPosCar_2, 1, 2, 1, 1)
        self.XNegCar_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.XNegCar_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.XNegCar_2.setFont(font)
        self.XNegCar_2.setObjectName("XNegCar_2")
        self.JSI_2.addWidget(self.XNegCar_2, 1, 0, 1, 1)
        self.JSBox.addLayout(self.JSI_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.JSBox.addItem(spacerItem3)
        self.AppLayout.addLayout(self.JSBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.AppLayout.addItem(spacerItem4)
        self.ButtonBox = QtWidgets.QHBoxLayout()
        self.ButtonBox.setObjectName("ButtonBox")
        self.Bot1Box = QtWidgets.QVBoxLayout()
        self.Bot1Box.setObjectName("Bot1Box")
        self.Boton1txt = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton1txt.setFont(font)
        self.Boton1txt.setObjectName("Boton1txt")
        self.Bot1Box.addWidget(self.Boton1txt)
        self.Boton1Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton1Sel.setFont(font)
        self.Boton1Sel.setObjectName("Boton1Sel")
        self.Bot1Box.addWidget(self.Boton1Sel)
        self.Bot1Box_2 = QtWidgets.QVBoxLayout()
        self.Bot1Box_2.setObjectName("Bot1Box_2")
        self.Boton5txt = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton5txt.setFont(font)
        self.Boton5txt.setObjectName("Boton5txt")
        self.Bot1Box_2.addWidget(self.Boton5txt)
        self.Boton5Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton5Sel.setFont(font)
        self.Boton5Sel.setObjectName("Boton5Sel")
        self.Bot1Box_2.addWidget(self.Boton5Sel)
        self.Bot1Box.addLayout(self.Bot1Box_2)
        self.ButtonBox.addLayout(self.Bot1Box)
        self.Bot2Box = QtWidgets.QVBoxLayout()
        self.Bot2Box.setObjectName("Bot2Box")
        self.Boton2txt = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton2txt.setFont(font)
        self.Boton2txt.setObjectName("Boton2txt")
        self.Bot2Box.addWidget(self.Boton2txt)
        self.Boton2Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton2Sel.setFont(font)
        self.Boton2Sel.setObjectName("Boton2Sel")
        self.Bot2Box.addWidget(self.Boton2Sel)
        self.Bot2Box_2 = QtWidgets.QVBoxLayout()
        self.Bot2Box_2.setObjectName("Bot2Box_2")
        self.Boton6txt = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton6txt.setFont(font)
        self.Boton6txt.setObjectName("Boton6txt")
        self.Bot2Box_2.addWidget(self.Boton6txt)
        self.Boton6Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton6Sel.setFont(font)
        self.Boton6Sel.setObjectName("Boton6Sel")
        self.Bot2Box_2.addWidget(self.Boton6Sel)
        self.Bot2Box.addLayout(self.Bot2Box_2)
        self.ButtonBox.addLayout(self.Bot2Box)
        self.Bot3Box = QtWidgets.QVBoxLayout()
        self.Bot3Box.setObjectName("Bot3Box")
        self.Boton3txt = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton3txt.setFont(font)
        self.Boton3txt.setObjectName("Boton3txt")
        self.Bot3Box.addWidget(self.Boton3txt)
        self.Boton3Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton3Sel.setFont(font)
        self.Boton3Sel.setObjectName("Boton3Sel")
        self.Bot3Box.addWidget(self.Boton3Sel)
        self.Bot3Box_2 = QtWidgets.QVBoxLayout()
        self.Bot3Box_2.setObjectName("Bot3Box_2")
        self.Boton7txt = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton7txt.setFont(font)
        self.Boton7txt.setObjectName("Boton7txt")
        self.Bot3Box_2.addWidget(self.Boton7txt)
        self.Boton7Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton7Sel.setFont(font)
        self.Boton7Sel.setObjectName("Boton7Sel")
        self.Bot3Box_2.addWidget(self.Boton7Sel)
        self.Bot3Box.addLayout(self.Bot3Box_2)
        self.ButtonBox.addLayout(self.Bot3Box)
        self.Bot4Box = QtWidgets.QVBoxLayout()
        self.Bot4Box.setObjectName("Bot4Box")
        self.Boton4txt = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton4txt.setFont(font)
        self.Boton4txt.setObjectName("Boton4txt")
        self.Bot4Box.addWidget(self.Boton4txt)
        self.Boton4Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton4Sel.setFont(font)
        self.Boton4Sel.setObjectName("Boton4Sel")
        self.Bot4Box.addWidget(self.Boton4Sel)
        self.Bot4Box_2 = QtWidgets.QVBoxLayout()
        self.Bot4Box_2.setObjectName("Bot4Box_2")
        self.Boton8txt = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton8txt.setFont(font)
        self.Boton8txt.setObjectName("Boton8txt")
        self.Bot4Box_2.addWidget(self.Boton8txt)
        self.Boton8Sel = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Boton8Sel.setFont(font)
        self.Boton8Sel.setObjectName("Boton8Sel")
        self.Bot4Box_2.addWidget(self.Boton8Sel)
        self.Bot4Box.addLayout(self.Bot4Box_2)
        self.ButtonBox.addLayout(self.Bot4Box)
        self.AppLayout.addLayout(self.ButtonBox)
        self.CABox = QtWidgets.QHBoxLayout()
        self.CABox.setObjectName("CABox")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CABox.addItem(spacerItem5)
        self.CerrarButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.CerrarButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.CerrarButton.setFont(font)
        self.CerrarButton.setObjectName("CerrarButton")
        self.CABox.addWidget(self.CerrarButton)
        self.AceptarButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.AceptarButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.AceptarButton.setFont(font)
        self.AceptarButton.setCheckable(False)
        self.AceptarButton.setObjectName("AceptarButton")
        self.CABox.addWidget(self.AceptarButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CABox.addItem(spacerItem6)
        self.AppLayout.addLayout(self.CABox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cargarButton.released.connect(MainWindow.cargarControl) # type: ignore
        self.guardarButton.released.connect(MainWindow.guardarControl) # type: ignore
        self.borrarButton.released.connect(MainWindow.eliminarControl) # type: ignore
        self.AceptarButton.released.connect(MainWindow.aplicarControl) # type: ignore
        self.CerrarButton.released.connect(MainWindow.desactivarControl) # type: ignore
        self.AlphaSortButton.released.connect(MainWindow.sortearControl) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AlphaSortButton.setText(_translate("MainWindow", "A-Z"))
        self.guardarButton.setText(_translate("MainWindow", "Guardar Actual"))
        self.borrarButton.setText(_translate("MainWindow", "Eliminar"))
        self.cargarButton.setText(_translate("MainWindow", "Cargar"))
        self.label.setText(_translate("MainWindow", "Joystick Izquierdo"))
        self.label_2.setText(_translate("MainWindow", "Joystick Derecho"))
        self.Boton1txt.setText(_translate("MainWindow", "Boton 1"))
        self.Boton5txt.setText(_translate("MainWindow", "Boton 5"))
        self.Boton2txt.setText(_translate("MainWindow", "Boton 2"))
        self.Boton6txt.setText(_translate("MainWindow", "Boton 6"))
        self.Boton3txt.setText(_translate("MainWindow", "Boton 3"))
        self.Boton7txt.setText(_translate("MainWindow", "Boton 7"))
        self.Boton4txt.setText(_translate("MainWindow", "Boton 4"))
        self.Boton8txt.setText(_translate("MainWindow", "Boton 8"))
        self.CerrarButton.setText(_translate("MainWindow", "Cerrar"))
        self.AceptarButton.setText(_translate("MainWindow", "Aplicar y conectar control"))
