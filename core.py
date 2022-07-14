from PySide2.QtWidgets import QApplication
from main import MainWindow
import sys


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())