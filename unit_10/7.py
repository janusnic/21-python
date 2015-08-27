#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
