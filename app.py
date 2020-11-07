import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import random

class e_gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="Aleatorizador de Tareas"
        self.iconName = ""
        self.last_item = None
        self.InitUI()
        self.boton_agregar_tarea.clicked.connect(self.add_item)
        self.boton_quitar_tarea.clicked.connect(self.del_item)
        self.boton_aleatorio.clicked.connect(self.random_item)
        

    def InitUI(self):
        uic.loadUi("gui_app.ui",self)
        
    
    def add_item(self):
        self.tareas.insertItem(self.tareas.count(), str(self.tareas.count()+1) + " - " + self.get_description())
        self.last_item = self.tareas.item(0)

    def get_description(self):
        return self.tarea_input.text().capitalize()

    def del_item(self):
        self.tareas.takeItem(self.get_id())

    def get_id(self):
        inp = self.borrar_tarea_input.text()
        return self.tareas.row(self.tareas.findItems(inp, QtCore.Qt.MatchStartsWith)[0])
            
    def random_item(self):
        self.last_item.setBackground(QtGui.QColor("#FFFFFF"))
        inp = str(random.randint(1,self.tareas.count()))
        pos = self.tareas.row(self.tareas.findItems(inp, QtCore.Qt.MatchStartsWith)[0])
        item = self.tareas.item(pos)
        item.setBackground(QtGui.QColor("#7fc97f"))
        self.last_item = item

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = e_gui()
    GUI.show()
    sys.exit(app.exec_())
