# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eindscherm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    # Een statische variabel die we vanuit de vragenlijstUI.py script kunnen weizigen
    specialisatie = None
    quote = None
    punten = 0


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 445)
        self.specialisatie = QtWidgets.QLabel(Form)
        self.specialisatie.setGeometry(QtCore.QRect(94, 60, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.specialisatie.setFont(font)
        self.specialisatie.setTextFormat(QtCore.Qt.AutoText)
        self.specialisatie.setAlignment(QtCore.Qt.AlignCenter)
        self.specialisatie.setObjectName("specialisatie")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(44, 116, 481, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setGeometry(QtCore.QRect(450, 400, 93, 28))
        self.exit_button.setObjectName("exit_button")
        self.label_2.setWordWrap(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.specialisatie.setText(_translate("Form", Ui_Form.specialisatie))
        self.label_2.setText(_translate("Form", Ui_Form.quote))
        self.exit_button.setText(_translate("Form", "Exit"))

        self.exit_button.clicked.connect(self.exitt)


    def exitt(self):
        exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
