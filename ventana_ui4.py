# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tabla3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Huertas(object):
    def setupUi(self, Huertas):
        Huertas.setObjectName("Huertas")
        Huertas.resize(1602, 795)
        self.frame = QtWidgets.QFrame(Huertas)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1601, 801))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(340, 10, 691, 91))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(50, 55, 201, 231))
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Img/imagenHuertas.ico"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(340, 105, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(340, 165, 91, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(340, 235, 91, 41))
        self.label_7.setObjectName("label_7")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(440, 109, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(205, 255, 214);")
        self.name.setText("")
        self.name.setClearButtonEnabled(True)
        self.name.setObjectName("name")
        self.lastname = QtWidgets.QLineEdit(self.frame)
        self.lastname.setGeometry(QtCore.QRect(440, 175, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lastname.setFont(font)
        self.lastname.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(205, 255, 214);")
        self.lastname.setText("")
        self.lastname.setClearButtonEnabled(True)
        self.lastname.setObjectName("lastname")
        self.dni = QtWidgets.QLineEdit(self.frame)
        self.dni.setGeometry(QtCore.QRect(440, 235, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dni.setFont(font)
        self.dni.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(205, 255, 214);")
        self.dni.setText("")
        self.dni.setClearButtonEnabled(True)
        self.dni.setObjectName("dni")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 400, 464, 289))
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(530, 440, 131, 31))
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 550, 131, 31))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btnContrato = QtWidgets.QPushButton(self.frame)
        self.btnContrato.setGeometry(QtCore.QRect(530, 390, 131, 41))
        self.btnContrato.setStyleSheet("background-color: rgb(101, 255, 183);\n"
"\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.btnContrato.setObjectName("btnContrato")
        self.btnInicial = QtWidgets.QPushButton(self.frame)
        self.btnInicial.setGeometry(QtCore.QRect(530, 500, 131, 41))
        self.btnInicial.setStyleSheet("background-color: rgb(101, 255, 183);\n"
"\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.btnInicial.setObjectName("btnInicial")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(730, 390, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(730, 440, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(740, 560, 119, 23))
        self.radioButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(880, 560, 119, 23))
        self.radioButton_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(830, 235, 131, 31))
        self.comboBox.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(101, 255, 183);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btnCalcular = QtWidgets.QPushButton(self.frame)
        self.btnCalcular.setGeometry(QtCore.QRect(510, 710, 681, 71))
        self.btnCalcular.setWhatsThis("")
        self.btnCalcular.setStyleSheet("background-color: rgb(55, 162, 61);\n"
"color: rgb(255, 255, 255);\n"
"font: 64 18pt \"Segoe UI Semibold\";\n"
"selection-color: rgb(255, 255, 127);")
        self.btnCalcular.setObjectName("btnCalcular")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 350, 981, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(730, 490, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.cuota = QtWidgets.QSpinBox(self.frame)
        self.cuota.setGeometry(QtCore.QRect(830, 500, 71, 22))
        self.cuota.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 254, 248);")
        self.cuota.setMaximum(150)
        self.cuota.setObjectName("cuota")
        self.inicial = QtWidgets.QDoubleSpinBox(self.frame)
        self.inicial.setGeometry(QtCore.QRect(830, 450, 161, 22))
        self.inicial.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 254, 248);")
        self.inicial.setMaximum(999999999.99)
        self.inicial.setObjectName("inicial")
        self.importe = QtWidgets.QDoubleSpinBox(self.frame)
        self.importe.setGeometry(QtCore.QRect(830, 400, 161, 22))
        self.importe.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 254, 248);")
        self.importe.setMaximum(999999999.99)
        self.importe.setObjectName("importe")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(440, 325, 241, 31))
        self.comboBox_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(101, 255, 183);\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lote = QtWidgets.QLineEdit(self.frame)
        self.lote.setGeometry(QtCore.QRect(440, 285, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lote.setFont(font)
        self.lote.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(205, 255, 214);")
        self.lote.setText("")
        self.lote.setClearButtonEnabled(True)
        self.lote.setObjectName("lote")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(340, 285, 91, 41))
        self.label_12.setObjectName("label_12")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(1050, 10, 21, 681))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(1100, 10, 461, 91))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(1090, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(1090, 160, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(1090, 220, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(1090, 260, 471, 41))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(1090, 540, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(1090, 580, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(1090, 630, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.domicilio = QtWidgets.QLineEdit(self.frame)
        self.domicilio.setGeometry(QtCore.QRect(1270, 110, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.domicilio.setFont(font)
        self.domicilio.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(205, 255, 214);")
        self.domicilio.setText("")
        self.domicilio.setClearButtonEnabled(True)
        self.domicilio.setObjectName("domicilio")
        self.telefono = QtWidgets.QLineEdit(self.frame)
        self.telefono.setGeometry(QtCore.QRect(1270, 170, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.telefono.setFont(font)
        self.telefono.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(205, 255, 214);")
        self.telefono.setText("")
        self.telefono.setClearButtonEnabled(True)
        self.telefono.setObjectName("telefono")
        self.fiador = QtWidgets.QLineEdit(self.frame)
        self.fiador.setGeometry(QtCore.QRect(1270, 230, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fiador.setFont(font)
        self.fiador.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(255, 254, 208);")
        self.fiador.setText("")
        self.fiador.setClearButtonEnabled(True)
        self.fiador.setObjectName("fiador")
        self.banco = QtWidgets.QLineEdit(self.frame)
        self.banco.setGeometry(QtCore.QRect(1270, 540, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.banco.setFont(font)
        self.banco.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(255, 254, 208);")
        self.banco.setText("")
        self.banco.setClearButtonEnabled(True)
        self.banco.setObjectName("banco")
        self.cuentabanco = QtWidgets.QLineEdit(self.frame)
        self.cuentabanco.setGeometry(QtCore.QRect(1270, 590, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cuentabanco.setFont(font)
        self.cuentabanco.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(255, 254, 208);")
        self.cuentabanco.setText("")
        self.cuentabanco.setClearButtonEnabled(True)
        self.cuentabanco.setObjectName("cuentabanco")
        self.cci = QtWidgets.QLineEdit(self.frame)
        self.cci.setGeometry(QtCore.QRect(1270, 640, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cci.setFont(font)
        self.cci.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(255, 254, 208);")
        self.cci.setText("")
        self.cci.setClearButtonEnabled(True)
        self.cci.setObjectName("cci")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(1230, 270, 201, 51))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(1090, 370, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(1090, 420, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.avalDOI = QtWidgets.QLineEdit(self.frame)
        self.avalDOI.setGeometry(QtCore.QRect(1270, 420, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avalDOI.setFont(font)
        self.avalDOI.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(255, 254, 208);")
        self.avalDOI.setText("")
        self.avalDOI.setClearButtonEnabled(True)
        self.avalDOI.setObjectName("avalDOI")
        self.avalDomicilio = QtWidgets.QLineEdit(self.frame)
        self.avalDomicilio.setGeometry(QtCore.QRect(1270, 370, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avalDomicilio.setFont(font)
        self.avalDomicilio.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(255, 254, 208);")
        self.avalDomicilio.setText("")
        self.avalDomicilio.setClearButtonEnabled(True)
        self.avalDomicilio.setObjectName("avalDomicilio")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(1090, 460, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.avalTelefono = QtWidgets.QLineEdit(self.frame)
        self.avalTelefono.setGeometry(QtCore.QRect(1270, 470, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avalTelefono.setFont(font)
        self.avalTelefono.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(255, 254, 208);")
        self.avalTelefono.setText("")
        self.avalTelefono.setClearButtonEnabled(True)
        self.avalTelefono.setObjectName("avalTelefono")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(1090, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.avalNombre = QtWidgets.QLineEdit(self.frame)
        self.avalNombre.setGeometry(QtCore.QRect(1270, 320, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.avalNombre.setFont(font)
        self.avalNombre.setStyleSheet("border-color: rgb(18, 154, 168);\n"
"background-color: rgb(255, 254, 208);")
        self.avalNombre.setText("")
        self.avalNombre.setClearButtonEnabled(True)
        self.avalNombre.setObjectName("avalNombre")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(1100, 500, 461, 41))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.retranslateUi(Huertas)
        QtCore.QMetaObject.connectSlotsByName(Huertas)
        Huertas.setTabOrder(self.name, self.lastname)
        Huertas.setTabOrder(self.lastname, self.dni)
        Huertas.setTabOrder(self.dni, self.lote)
        Huertas.setTabOrder(self.lote, self.comboBox)
        Huertas.setTabOrder(self.comboBox, self.comboBox_2)
        Huertas.setTabOrder(self.comboBox_2, self.btnCalcular)
        Huertas.setTabOrder(self.btnCalcular, self.btnContrato)
        Huertas.setTabOrder(self.btnContrato, self.calendarWidget)
        Huertas.setTabOrder(self.calendarWidget, self.btnInicial)
        Huertas.setTabOrder(self.btnInicial, self.lineEdit)
        Huertas.setTabOrder(self.lineEdit, self.lineEdit_2)
        Huertas.setTabOrder(self.lineEdit_2, self.importe)
        Huertas.setTabOrder(self.importe, self.inicial)
        Huertas.setTabOrder(self.inicial, self.cuota)
        Huertas.setTabOrder(self.cuota, self.radioButton)
        Huertas.setTabOrder(self.radioButton, self.radioButton_2)
        Huertas.setTabOrder(self.radioButton_2, self.domicilio)
        Huertas.setTabOrder(self.domicilio, self.telefono)
        Huertas.setTabOrder(self.telefono, self.fiador)
        Huertas.setTabOrder(self.fiador, self.avalNombre)
        Huertas.setTabOrder(self.avalNombre, self.avalDomicilio)
        Huertas.setTabOrder(self.avalDomicilio, self.avalDOI)
        Huertas.setTabOrder(self.avalDOI, self.avalTelefono)
        Huertas.setTabOrder(self.avalTelefono, self.banco)
        Huertas.setTabOrder(self.banco, self.cuentabanco)
        Huertas.setTabOrder(self.cuentabanco, self.cci)
      

    def retranslateUi(self, Huertas):
        _translate = QtCore.QCoreApplication.translate
        Huertas.setWindowTitle(_translate("Huertas", "Dialog"))
        self.label.setText(_translate("Huertas", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Tabla de Amortización</span></p></body></html>"))
        self.label_5.setText(_translate("Huertas", "<html><head/><body><p><span style=\" font-size:11pt;\">Nombre:</span></p></body></html>"))
        self.label_6.setText(_translate("Huertas", "<html><head/><body><p><span style=\" font-size:11pt;\">Apellido:</span></p></body></html>"))
        self.label_7.setText(_translate("Huertas", "<html><head/><body><p><span style=\" font-size:11pt;\">DNI:</span></p></body></html>"))
        self.btnContrato.setText(_translate("Huertas", "Fecha Contrato"))
        self.btnInicial.setText(_translate("Huertas", "Fecha Pago"))
        self.label_8.setText(_translate("Huertas", "<html><head/><body><p><span style=\" font-size:11pt;\">Importe:</span></p></body></html>"))
        self.label_9.setText(_translate("Huertas", "<html><head/><body><p><span style=\" font-size:11pt;\">Inicial:</span></p></body></html>"))
        self.radioButton.setText(_translate("Huertas", "Soles"))
        self.radioButton_2.setText(_translate("Huertas", "Dolares"))
        self.comboBox.setItemText(0, _translate("Huertas", "Proyecto"))
        self.comboBox.setItemText(1, _translate("Huertas", "Olivar"))
        self.comboBox.setItemText(2, _translate("Huertas", "Oasis"))
        self.comboBox.setItemText(3, _translate("Huertas", "Apolo"))
        self.btnCalcular.setText(_translate("Huertas", "Calcular"))
        self.label_11.setText(_translate("Huertas", "<html><head/><body><p><span style=\" font-size:11pt;\">Cuotas:</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Huertas", "Categoría"))
        self.comboBox_2.setItemText(1, _translate("Huertas", "Precio de Lote"))
        self.comboBox_2.setItemText(2, _translate("Huertas", "Habilitación Urbana"))
        self.label_12.setText(_translate("Huertas", "<html><head/><body><p><span style=\" font-size:11pt;\">LOTE:</span></p></body></html>"))
        self.label_3.setText(_translate("Huertas", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Letra de Cambio</span></p></body></html>"))
        self.label_10.setText(_translate("Huertas", "<html><head/><body><p>Domicilio:</p></body></html>"))
        self.label_13.setText(_translate("Huertas", "<html><head/><body><p>Teléfono:</p></body></html>"))
        self.label_25.setText(_translate("Huertas", "<html><head/><body><p>Fiador:</p></body></html>"))
        self.label_26.setText(_translate("Huertas", "<html><head/><body><p>Banco:</p></body></html>"))
        self.label_27.setText(_translate("Huertas", "<html><head/><body><p>N° de cuenta:</p></body></html>"))
        self.label_28.setText(_translate("Huertas", "<html><head/><body><p>CCI:</p></body></html>"))
        self.label_29.setText(_translate("Huertas", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Aval Permanente:</span></p></body></html>"))
        self.label_30.setText(_translate("Huertas", "<html><head/><body><p>Domicilio:</p></body></html>"))
        self.label_31.setText(_translate("Huertas", "<html><head/><body><p>DOI:</p></body></html>"))
        self.label_32.setText(_translate("Huertas", "<html><head/><body><p>Teléfono:</p></body></html>"))
        self.label_33.setText(_translate("Huertas", "<html><head/><body><p>Nombre:</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Huertas = QtWidgets.QDialog()
    ui = Ui_Huertas()
    ui.setupUi(Huertas)
    Huertas.show()
    sys.exit(app.exec_())
