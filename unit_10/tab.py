from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

def main():

    app 	= QtGui.QApplication(sys.argv)
    tabs	= QtGui.QTabWidget()
    pushButton1 = QtGui.QPushButton("QPushButton 1")
    pushButton2 = QtGui.QPushButton("QPushButton 2")

    tab1	= QtGui.QWidget()
    tab2	= QtGui.QWidget()
    tab3	= QtGui.QWidget()

    vBoxlayout	= QtGui.QVBoxLayout()
    vBoxlayout.addWidget(pushButton1)
    vBoxlayout.addWidget(pushButton2)

    #Resize width and height
    tabs.resize(250, 150)

    #Move QTabWidget to x:300,y:300
    tabs.move(300, 300)

    #Set Layout for Third Tab Page
    tab3.setLayout(vBoxlayout)

    tabs.addTab(tab1,"Tab 1")
    tabs.addTab(tab2,"Tab 2")
    tabs.addTab(tab3,"Tab 3")

    tabs.setWindowTitle('PyQt QTabWidget Add Tabs and Widgets Inside Tab')
    tabs.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
