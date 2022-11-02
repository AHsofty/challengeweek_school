# Het doel van dit programma is om een student in een specialisatie te plaatsen door middel van diens antwoorden op 16 vragen

from PyQt5 import QtCore, QtGui, QtWidgets
from puntensysteem import Puntensysteem
import excelreader
from operator import attrgetter
from eindscherm import Ui_Form as eindschermpje

class Ui_Form(object):

    def openNewWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = eindschermpje()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")

        Form.resize(880, 879)
        Form.setFixedSize(880, 879) # Let op dit is hardcoded
        
        self.vraag_lable = QtWidgets.QLabel(Form)
        self.vraag_lable.setGeometry(QtCore.QRect(0, 20, 881, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.vraag_lable.setFont(font)
        self.vraag_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.vraag_lable.setObjectName("vraag_lable")
        self.next_button = QtWidgets.QPushButton(Form)
        self.next_button.setGeometry(QtCore.QRect(730, 790, 121, 41))
        self.next_button.setObjectName("next_button")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(40, 782, 111, 51))
        self.back_button.setObjectName("back_button")
        self.button_one = QtWidgets.QRadioButton(Form)
        self.button_one.setGeometry(QtCore.QRect(40, 490, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_one.setFont(font)
        self.button_one.setObjectName("button_one")
        self.button_two = QtWidgets.QRadioButton(Form)
        self.button_two.setGeometry(QtCore.QRect(214, 490, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_two.setFont(font)
        self.button_two.setObjectName("button_two")
        self.button_three = QtWidgets.QRadioButton(Form)
        self.button_three.setGeometry(QtCore.QRect(400, 490, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_three.setFont(font)
        self.button_three.setObjectName("button_three")
        self.button_four = QtWidgets.QRadioButton(Form)
        self.button_four.setGeometry(QtCore.QRect(550, 494, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_four.setFont(font)
        self.button_four.setObjectName("button_four")
        self.button_five = QtWidgets.QRadioButton(Form)
        self.button_five.setGeometry(QtCore.QRect(726, 493, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_five.setFont(font)
        self.button_five.setObjectName("button_five")
        self.vraag_lable.setWordWrap(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self._translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.vraag_lable.setText(_translate("Form", "Hier kom de vraag te staan"))
        self.next_button.setText(_translate("Form", "Volgende"))
        self.back_button.setText(_translate("Form", "Terug"))
        self.button_one.setText(_translate("Form", "1"))
        self.button_two.setText(_translate("Form", "2"))
        self.button_three.setText(_translate("Form", "3"))
        self.button_four.setText(_translate("Form", "4"))
        self.button_five.setText(_translate("Form", "5"))

  
        # Initial setup
        self.buttton_selected = 0
        self.next_button.clicked.connect(self.on_click_next)
        self.back_button.clicked.connect(self.on_click_back)
        self.button_one.clicked.connect(self.click_one)
        self.button_two.clicked.connect(self.click_two)
        self.button_three.clicked.connect(self.click_three)
        self.button_four.clicked.connect(self.click_four)
        self.button_five.clicked.connect(self.click_five)

        self.puntensysteem = Puntensysteem()
        self.excel = excelreader.Excelreader("database.xls", "Vragen")
        self.vragen = self.excel.get_data()
        self.index = 0
        self.klaar = False
        self.to_get_class = None # Dit word geweizigd met de class reference van de window die je wilt laden.

        self.show_question()




    def click_one(self):
        self.buttton_selected = 1

    def click_two(self):
        self.buttton_selected = 2

    def click_three(self):
        self.buttton_selected = 3

    def click_four(self):
        self.buttton_selected = 4

    def click_five(self):
        self.buttton_selected = 5


    def on_click_next(self):
        if self.buttton_selected != 0 and self.index+1 != len(self.vragen):
            self.puntensysteem.voeg_punten_toe(self.vragen[self.index].domein, self.buttton_selected)
            self.vragen[self.index].gegeven_antwoord = self.buttton_selected

            self.index += 1
            self.show_question()

        elif self.index+1 == len(self.vragen) and self.klaar == False:


            self.klaar = True
            x = self.vragen
            self.vragen.sort(key=attrgetter('gegeven_antwoord'), reverse=True)  # Sorteert de vragen op basis van de hoogste dingen
            domeinen = self.puntensysteem.get_domeinen()
            domein = domeinen[0] # We pakken lekker de eerste
            

            quote_amount = 3 # Lekker hardcoden
            nieuwe_lijst = []
            for p in self.vragen:
                if p.domein == domein.afgekorte_domein and p.gegeven_antwoord > 3:
                    nieuwe_lijst.append(p)

            lijst_met_quotes = []
            if len(nieuwe_lijst) != 0:
                for p in nieuwe_lijst:
                    lijst_met_quotes.append(p.quote)
            else:
                for p in self.vragen:
                    lijst_met_quotes.append(p.quote)
                    quote_amount -= 1
                    if quote_amount == 0:
                        break

            zin = ""
            for p in lijst_met_quotes:
                zin += p+" "

            # We veranderen een paar waardes
            eindschermpje.punten = domein.punten
            eindschermpje.specialisatie = domein.domein
            eindschermpje.quote = zin
            self.openNewWindow()



            # for i in domeinen:
            #     print(f"Jouw domein is: {i.domein} met {i.punten} punten")

            #     nieuwe_lijst = []
            #     for p in self.vragen:
            #         if p.domein == i.afgekorte_domein and p.gegeven_antwoord > 3:
            #             nieuwe_lijst.append(p)

            #     lijst_met_quotes = []
            #     if len(nieuwe_lijst) != 0:
            #         for p in nieuwe_lijst:
            #             lijst_met_quotes.append(p.quote)
            #     else:
            #         for p in vragen:
            #             lijst_met_quotes.append(p.quote)
            #             quote_amount -= 1
            #             if quote_amount == 0:
            #                 break

            #     zin = ""
            #     for p in lijst_met_quotes:
            #         zin += p+" "
                # print(zin)



    def on_click_back(self):
        if self.index != 0:
            self.index -= 1
            self.show_question()



    def show_question(self):
        self.vraag_lable.setText(self._translate("Form", self.vragen[self.index].vraag))



if __name__ == "__main__":  
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())