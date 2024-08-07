# QtPy5 is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
 
app = QApplication(sys.argv)
 
window = QWidget()
 
window.setWindowTitle("PyQt Example")
 
button = QPushButton("Click Me!", window)
 
button.move(50, 50)
 
window.show()
 
sys.exit(app.exec_())
