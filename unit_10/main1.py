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

class Manage(QtGui.QWidget):

    def __init__(self):

        super(Manage, self).__init__()

        self.initUI()

    def initUI(self):
        mystaff = Staff()
        mystaff.add_employee('Mary', 'Ann', 123, 'Denwer', 1010, 1, 8)
        mystaff.add_employee('Boby', 'Ban', 234, 'Denwer', 1100, 2, 8)

        item = []

        for ind, emp in enumerate(mystaff.employee_list):
            item.append(ind)
            item[ind] = QtGui.QLabel(str(emp), self)
            item[ind].move(15, 10*(1+ind))

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)

    man = Manage()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
