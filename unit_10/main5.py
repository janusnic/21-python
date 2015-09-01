#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

Employee demo class
"""
import sys, os
import employee
from PyQt4 import QtGui, QtCore

class MessagesWidgets(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MessagesWidgets, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        okButton = QtGui.QPushButton("Ok")
        abouttext = QtGui.QLabel('Janus Nic Aplication')
        grid = QtGui.QGridLayout() 
        grid.addWidget(abouttext, 1, 0)       
        grid.addWidget(okButton)
       
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        
        self.setWindowTitle("Message for You")
        okButton.clicked.connect(self.close)  


class ModalWind(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ModalWind, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        
        fname = QtGui.QLabel('First Name')
        lname = QtGui.QLabel('Last Name')
        city = QtGui.QLabel('City')
        zid = QtGui.QLabel('ID')

        fnamrEdit = QtGui.QLineEdit()
        lnameEdit = QtGui.QLineEdit()
        cityEdit = QtGui.QLineEdit()
        zidEdit = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(fname, 1, 0)
        grid.addWidget(fnamrEdit, 1, 1)

        grid.addWidget(lname, 2, 0)
        grid.addWidget(lnameEdit, 2, 1)

        grid.addWidget(city, 3, 0)
        grid.addWidget(cityEdit, 3, 1)

        grid.addWidget(zid, 4, 0)
        grid.addWidget(zidEdit, 4, 1)

        okButton = QtGui.QPushButton("Save")
        cancelButton = QtGui.QPushButton("Cancel")
        
        grid.addWidget(okButton)
        grid.addWidget(cancelButton)
        
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Add new employee")
        cancelButton.clicked.connect(self.close)  
        

class Staff(object):

    def __init__(self):
        self.employee_list = []

    def add_employee(self, first_name, last_name, ID, city, base_pay, shift, hours):
        new_emp = employee.Employee(first_name, last_name, ID, city, base_pay, shift, hours)
        self.employee_list.append(new_emp)

data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}

class Manage(QtGui.QMainWindow):

    def __init__(self):

        super(Manage, self).__init__()
        self.textEdit = QtGui.QTextEdit()
        self.data = data


        self.initUI()

    def about(self):
        messages_widget = MessagesWidgets(self)
    
        self.setToolTip('About Aplication')
        messages_widget.show()

    def showDialog(self):
        win = ModalWind(self)
        win.show()
       

    def showList(self):
        mystaff = Staff()
        mystaff.add_employee('Mary', 'Ann', 123, 'Denwer', 1010, 1, 8)
        mystaff.add_employee('Boby', 'Ban', 234, 'Denwer', 1100, 2, 8)

        for ind, emp in enumerate(mystaff.employee_list):
            self.textEdit.append(str(emp))

    def initUI(self):


        self.setCentralWidget(self.textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/close.png"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        aboutAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/help.png"), 'About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.setStatusTip('About application')
        aboutAction.triggered.connect(self.about)

        addAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/web.png"), 'Add', self)
        addAction.setShortcut('Ctrl+N')
        addAction.setStatusTip('Add record')
        addAction.triggered.connect(self.showDialog)

        showAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/web.png"), 'Show', self)
        showAction.setShortcut('Ctrl+L')
        showAction.setStatusTip('Show records')
        showAction.triggered.connect(self.showList)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        menubar = self.menuBar()
        aboutMenu = menubar.addMenu('&About')
        aboutMenu.addAction(aboutAction)


        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        toolbar = self.addToolBar('Add')
        toolbar.addAction(addAction)

        toolbar = self.addToolBar('Show')
        toolbar.addAction(showAction)



        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)

    man = Manage()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
