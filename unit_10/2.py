#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
