import sys
from PyQt5 import QtWidgets
class Window2(QtWidgets.QWidget):

    def __init__(self):
        super().__init__() # dziedziczy konstruktor z klas

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Push Button')
        self.l = QtWidgets.QLabel('I have not been click yet')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 lesson')

        self.b.clicked.connect(self.button_clicked) # wykonuje funkcje jesli przycisk wcisniety

        self.show()

    def button_clicked(self):
        self.l.setText('Second') # tekst wyswietlany po wcisnieciu przycisku

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__() # dziedziczy konstruktor z klas

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Push Button')
        self.l = QtWidgets.QLabel('First')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 lesson')

        self.b.clicked.connect(self.button_clicked) # wykonuje funkcje jesli przycisk wcisniety

        self.show()

    def button_clicked(self):
        self.W = Window2()
        self.show()


app = QtWidgets.QApplication(sys.argv)
a_Window = Window()
sys.exit(app.exec_())