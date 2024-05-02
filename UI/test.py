import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import requests

class APICallExample(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.label = QLabel("Data will be shown here.")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Call API")
        self.button.clicked.connect(self.call_api)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def call_api(self):
        try:
            response = requests.get(url='https://api.ipify.org/',headers='')
            if response.status_code == 200:
                data = response.json()
                self.label.setText(str(data))
    
        except Exception as e:
            self.label.setText("Error: " + str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = APICallExample()
    window.show()
    sys.exit(app.exec_())
