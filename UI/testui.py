import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
from collections import deque
from itertools import count
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 280)
        self.trungnguyenyeuem = QtWidgets.QWidget(Form)
        self.trungnguyenyeuem.setGeometry(QtCore.QRect(100, 109, 111, 71))
        self.trungnguyenyeuem.setObjectName("trungnguyenyeuem")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(100, 70, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 190, 111, 61))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("border-radius: 5px;\n"
                                       "border: 1px solid orange;\n"
                                       "margin-right: 2px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/icons/Setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 190, 111, 61))
        self.pushButton_4.setStyleSheet("border-radius: 5px;\n"
                                         "border: 1px solid rgb(170, 0, 255);\n"
                                         "margin-right: 2px;")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("source/icons/angle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Add animated plot to the widget
        self.add_animated_plot()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_19.setText(_translate("Form", "Average voltage"))

    def add_animated_plot(self):
        # Create Matplotlib figure and canvas
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)

        # Embed the canvas into the widget
        layout = QtWidgets.QVBoxLayout(self.trungnguyenyeuem)
        layout.addWidget(self.canvas)

        # Set up animation
        self.xLable = deque(maxlen=30)
        self.data1 = deque(maxlen=30)
        self.index = count()

        self.ani = FuncAnimation(self.fig, self.animate, interval=500)

    def animate(self, i):
        self.xLable.append(next(self.index))
        self.data1.append(random.randrange(0, 9) * 0.1 + 220)
        self.ax.clear()
        self.ax.plot(self.xLable, self.data1)
        self.ax.set_ylabel('Voltage')
        self.ax.set_facecolor("#00416A")
        self.fig.tight_layout()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
