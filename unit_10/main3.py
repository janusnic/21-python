#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

Employee demo class
"""
import sys, os
import employee
from PyQt4 import QtGui

class Staff(object):

    def __init__(self):
        self.employee_list = []

    def add_employee(self, first_name, last_name, ID, city, base_pay, shift, hours):
        new_emp = employee.Employee(first_name, last_name, ID, city, base_pay, shift, hours)
        self.employee_list.append(new_emp)

class Manage(QtGui.QMainWindow):

    def __init__(self):

        super(Manage, self).__init__()
        self.textEdit = QtGui.QTextEdit()


        self.initUI()

    def showDialog(self):

        first_name = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter first name:')
        last_name = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter last name:')
        base_pay = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter base pay:')
        shift = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter shift:')
        hours = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter hours:')

        if ok:
            pass
            #self.le.setText(str(text))

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
