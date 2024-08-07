
import sys
 
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
 
app = QApplication(sys.argv)
 
window = QWidget()
 
window.setWindowTitle("PySide Example")
 
button = QPushButton("Click Me!", window)
 
button.move(50, 50)
 
window.show()
 
sys.exit(app.exec_())