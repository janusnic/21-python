from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class MyTableView(QTableView):

  @pyqtSlot("QModelIndex")
  def ItemDoubleClicked(self,index):
    QMessageBox.information(None,"Hello!","You Double Clicked: \n"+index.data().toString())


def main():
    app 	= QApplication(sys.argv)
    tableView 	= MyTableView(None)
    model 	= QStringListModel()

    model.setStringList(QString("Item 1;Item 2;Item 3;Item 4").split(";"))
    tableView.setModel(model)
    tableView.setWindowTitle("QTableView Detect Double Click")
    tableView.show()

    QObject.connect(tableView,SIGNAL("doubleClicked(QModelIndex)"),
		    tableView,SLOT("ItemDoubleClicked(QModelIndex)"))
    return app.exec_()
if __name__ == '__main__':
  main()
