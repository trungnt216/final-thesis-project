import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import deque
from itertools import count
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matplotlib Animation in PyQt")

        # Tạo layout chính
        layout = QVBoxLayout()

        # Tạo canvas Matplotlib
        self.canvas = MplCanvas(self, width=5, height=4)
        layout.addWidget(self.canvas)

        # Tạo widget chính và thiết lập layout chính
        main_widget = QWidget(self)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Tạo dữ liệu cho animation
        self.xLable = deque(maxlen=30)
        self.data1 = deque(maxlen=30)
        self.index = count()

        # Tạo animation
        self.ani = FuncAnimation(self.canvas.figure, self.animate, interval=500)

    def animate(self, i):
        self.xLable.append(next(self.index))
        self.data1.append(random.randrange(0, 9)*0.1 + 220)
        self.canvas.ax.clear()
        self.canvas.ax.plot(self.xLable, self.data1)
        self.canvas.ax.set_xlabel('Time')
        self.canvas.ax.set_ylabel('Voltage')
        self.canvas.draw()

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
