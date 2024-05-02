from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
from itertools import count
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)

        # Create the trungnguyenyeuem widget
        self.trungnguyenyeuem = QtWidgets.QWidget(Form)
        self.trungnguyenyeuem.setGeometry(QtCore.QRect(100, 100, 400, 280))
        self.trungnguyenyeuem.setObjectName("trungnguyenyeuem")

        # Add Matplotlib canvas to the trungnguyenyeuem widget
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QtWidgets.QVBoxLayout(self.trungnguyenyeuem)
        layout.addWidget(self.canvas)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Matplotlib in PyQt5"))


class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Matplotlib animation variables
        self.x_label = deque(maxlen=30)
        self.data1 = deque(maxlen=30)
        self.index = count()

        # Start the animation
        self.ani = FuncAnimation(self.ui.figure, self.animate, interval=500)

    def animate(self, i):
        self.x_label.append(next(self.index))
        self.data1.append(random.randrange(0, 9) * 0.1 + 220)
        self.ui.figure.clear()
        ax = self.ui.figure.add_subplot(111)
        ax.plot(self.x_label, self.data1)
        ax.set_facecolor("#00416A")
        ax.set_ylabel('Voltage')
        self.ui.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = MatplotlibWidget()
    widget.show()
    sys.exit(app.exec_())
