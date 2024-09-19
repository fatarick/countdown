import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Countdown App") #Window Title

        browser = QWebEngineView()
        layout = QVBoxLayout()
        layout.addWidget(browser)

        browser.setUrl(QUrl("")) # Set the URL here
        self.resize(450, 325)
        self.setLayout(layout)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
