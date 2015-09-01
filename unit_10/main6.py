#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

Employee demo class
"""
import sys, os
import employee
from PyQt4 import QtGui, QtCore


class ModalWind(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ModalWind, self).__init__(parent)

        self.fname = QtGui.QLineEdit()
        self.lname = QtGui.QLineEdit()
        self.city = QtGui.QLineEdit()
        self.zid = QtGui.QLineEdit()

        grid = QtGui.QFormLayout()
        grid.addRow('First Name',self.fname)
        grid.setSpacing(10)
        grid.addRow('Last Name',self.lname)
        grid.setSpacing(10)
        grid.addRow('City',self.city)
        grid.setSpacing(10)
        grid.addRow('ID',self.zid)

        # OK and Cancel buttons
        self.buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.check)
        self.buttons.rejected.connect(self.reject)

        grid.addWidget(self.buttons)
        
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Add new employee")
    def check(self):
        if str(self.zid.text()) == "12345": # do actual login check
            self.accept()
        else:
            pass # or inform the user about bad username/password

    
class Staff(object):

    def __init__(self):
        self.employee_list = []

    def add_employee(self, first_name, last_name, ID, city, base_pay, shift, hours):
        new_emp = employee.Employee(first_name, last_name, ID, city, base_pay, shift, hours)
        self.employee_list.append(new_emp)

class Manage(QtGui.QMainWindow):

    

    def __init__(self,mystaff):

        super(Manage, self).__init__()
        self.textEdit = QtGui.QTextEdit()
        
        self.mystaff = mystaff


        self.initUI()

    def setEmp(self,fname,lname,city,zid):
        self.fname = fname
        self.lname = lname
        self.city = city
        self.zid = zid
        self.textEdit.append(self.fname+self.lname+self.city+self.zid)


    def about(self):
        QtGui.QMessageBox.warning(self, 'Janus TITLE', 'Janus Nic Aplication')
    

        self.setToolTip('About Aplication')
        messages_widget.show()

    def showDialog(self):

        win = ModalWind(self)
        win.show()
        if not win.exec_(): 
            sys.exit(-1) 
        else:
            self.setEmp(win.fname.text(),win.lname.text(),win.city.text(),win.zid.text())
            
            self.mystaff.add_employee(win.fname.text(), win.lname.text(), 123, win.city.text(), 1010, 1, 8)
            #self.mystaff.add_employee('Boby', 'Ban', 234, 'Denwer', 1100, 2, 8)
        

    def showList(self):
        
        self.mystaff.add_employee('Mary', 'Ann', 123, 'Denwer', 1010, 1, 8)
        self.mystaff.add_employee('Boby', 'Ban', 234, 'Denwer', 1100, 2, 8)

        for ind, emp in enumerate(self.mystaff.employee_list):
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
    mystaff = Staff()
    man = Manage(mystaff)


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
