# 21-python

# PyQt4 - тулкит для разработки GUI приложений.
Он представляет из себя смесь языка программирование Pythonи библиотеки Qt. Qt – одна из наиболее мощных библиотек. Официальный сайт PyQt www.riverbankcomputing.co.uk разработан Филом Томпсоном.
PyQt4 представляет из себя набор модулей Пайтон. Она содержит более 300 классов и почти 6000 функций и методов. Это мультиплатформенный тулкит. Он работает на всех основных операционных системах, включая Unix, Windows и MacOS. Начиная с версии PyQt4 GPL доступна для всех поддерживаемых платформ.

- Так как тулкит содержит большое количество классов, они распределены в несколько модулей.
1. Модуль QtCore содержит ядро не-gui функциональности. Этот модуль используется для работы со временем, файлами и папками, различными типами даных, потоками, адресами URL, mime типами, потоками процессов.
2. Модуль QtGui содержит графические компоненты и связанные классы. Сюда включены, например, кнопки, окна, строки состояния, панели инструментов, полосы прокрутки, изображения (bitmap), цвета, шрифты и др.
3. МодульQtNetwork содержит классы для сетевого программирования. Эти классы позволяют писать TCP/IP и UDP клиенты и серверы. Они делают сетевое программирование легче и более доступным.
4. Модуль QtXml содержит классы для работы с xml файлами. Он предоставляет реализации API SAX и DOM.
5. Модуль QtSvg предоставляет классы для отображения содержимого SVG файлов. Масштабируемая векторная графика (SVG) – это язык описания двумерной графики и графических приложений на языке XML.
6. МодульQtOpenGL используется для построения 3D и 2D графики с помощью библиотеки OpenGL. Модуль дает возможность бесшовной интеграции библиотек QtGui и OpenGL.
7. Модуль QtSql содержит классы для работы с базами данных.

# Простой пример
Он отображает небольшое окошко. Мы сможем изменить его размеры. Распахнуть на весь экран. Минимизировать.
```

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""

import sys
from PyQt4 import QtGui


def main():

    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
- Подключаем необходимые модули. Основные GUI виджеты находятся в библиотеке QtGui.
app = QtGui.QApplication(sys.argv)

- Каждое приложение PyQt4 должно создать объект Qapplication. Этот объект находится в модуле QtGui. Параметр sys.argv это список аргументов командной строки. Скрипты на Пайтон могут быть запущены из консоли, и с помощью аргументов мы можем контролировать запуск приложения.
widget = QtGui.QWidget()

- Qwidget это базовый класс для всех объектов интерфейса пользователя для PyQt4. Мы используем стандартный конструктор для Qwidget, который не имеет родителя. Виджет у которого нет родительского является окном.

- Метод resize() изменяет размеры виджета. В данном случае 250 пикселей по ширине и 150 по высоте.

widget.resize(250, 150)

- Здесь мы устанавлиаем заголовок окна на simple.
widget.setWindowTitle('simple')

- Метод show() отображает окно на экране.
```
widget.show()

sys.exit(app.exec())
```
В конце мы запускаем основной цикл приложения. Отсюда начинается обработка событий. Приложение получает события от оконной системы и распределяет их по виджетам. Когда цикл заканчивается, и если мы вызовем метод exit(), то наше окно (главный виджет) будет уничтожено. Метод sys.exit() гарантирует чистый выход. Окружение будет проинформировано о том, как приложение завершилось.

2. Иконка приложения
Иконка программы это просто маленькое изображение, которое обычно отображаетяс в левом верхнем углу заголовка.
```
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
```

В предыдущем примере код был процедурным. Пайтон поддерживает как процедурный, так и объекто-ориентированные стили программирования. Программирование на PyQt4 предполагает ООП программирование.
```
class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
```
Три наиболее важные вещи в объекто-ориентированном программировании это классы, данные и методы. Здесь мы создаем новый класс Icon. Класс Icon наследован от класса QtGui.QWidget. Это значит, что мы должны вызвать два конструктора: во-первых, для класса Icon и, во-вторых, для наследованного класса.
```
self.setGeometry(300, 300, 250, 150)
self.setWindowTitle('Icon')
self.setWindowIcon(QtGui.QIcon('icons/web.png'))
```
Все три класса наследованы от класса QtGui.QWidget. Метод setGeometry() делает две вещи: он определяет положение окна и его размеры. Первые два параметра это координаты по оси X и Y соответственно. Третий задает ширину окна, а четвёртый высоту. Последний метод setWindowIcon() устанавливает иконку программы. Чтобы сделать это, мы создаём объект QIcon.

- В качестве параметра передаётся путь до файла иконки.
exitAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/close.png"), 'Exit', self)

3. Всплывающая подсказка
Мы можем создать всплывающую подсказку для любого виджета.
```
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

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
- В этом примере, мы показываем подсказку для виджета Qwidget.
self.setToolTip('This is a QWidget widget')

- Для создания подсказки вызываем метод setToolTip(). Можно использовать html тэги для форматирования.
QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))

4. Закрытие окна
QPushButton(string text, QWidget parent = None)

- Это конструктор QPushButton, который мы будем использовать в нашем примере. Параметр text – это текст, который будет отображаться на кнопке, parent – тот виджет, на который мы поместим кнопку. В нашем случае это Qwidget.
```
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

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
Мы создаём кнопку и распологаем её на виджете также, как мы размещали виджет на экране.
```
self.connect(quit, QtCore.SIGNAL('clicked()'),
QtGui.qApp, QtCore.SLOT('quit()'))
```
Система обработки событий в PyQt4 построена на механизме сигналов и слотов. Если мы щёлкнем на кнопке, то будет послан сигнал clicked(). Слот может быть как слотом PyQt4 так и любым возможным для языка Пайтон. Метод QtCore.QObject.connect() соединяет сигнал и слот. В нашем случае слот является предопределённым слотов PyQt4.

5.  Окно сообщений
Обычно, при щелчке на кнопке закрытия в заголовке окна виджет закрывается. Иногда нам нужно изменить это действие. Например, если у нас открыт файл в редакторе с которым мы сделали какие-то изменения. В этом случае мы показываем пользователю сообщение для подтверждения выбранного действия.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()


    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

```
Когда мы закрываем виджет, генерируется событие QCloseEvent. Для изменения поведения виджета нам нужно изменить обработчик события QCloseEvent.
```
reply = QtGui.QMessageBox.question(self, 'Message',

    "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
```
Мы выводим сообщение с двумя кнопками “Да” и “Нет”. Первая строка ('Message') выводится в заголовке окна, вторая – текст сообщения. Возвращаемое значение хранится в переменной reply.
```
if reply == QtGui.QMessageBox.Yes:
    event.accept()
else:
    event.ignore()
```
Здесь мы проверяем возвращаемое значение: если щелкнули по кнопке “yes”, то мы принимаем стандартный обработчик, иначе – игнорируем закрытие.

# Управление расположением виджетов
 Управление расположением это то, как мы размещаем виджеты на форме. Тут есть два пути: использование абсолютного позиционирования (absolute positioning) или же использование классов расположения (layout classes).

6. Абсолютное позиционирование
Программист указывает положение и размер каждого виджета в пикселях. Когда вы используете абсолютное расположение вы должны понимать несколько вещей:
размер и положение виджета не изменяется при изменении размеров окна
приложение может выглядеть различно на разных платформах
изменение шрифта в вашем приложении может испортить расположение
если вы решаете изменить раскладку, вы должны полностью повторить её, что отнимает много времени
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
Мы просто вызываем метод move() для изменения положения виджетов, в нашем случае это QLabel. Мы располагаем их согласно координатам X и Y. Начало системы координат находится в левом верхнем углу окна. Координата X растёт справа налево, а Y сверху вниз. 

# Меню и панели инструментов

7. Строка состояния
Строка состояния это виджет, который используется для отображения статусной информации.
```
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
```
8. Меню
Меню это один из самых видных частей GUI приложения. Это группа команд расположенных в различных меню. Тогда как в консольных приложениях вам необходимо помнить все тайные команды, здесь вам доступно большинство команд сгруппированных логически. Это принятый стандарт, который уменьшает время на изучение нового приложения.
```
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

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

```
Во-первых, мы создаём меню c помощью метода menuBar() класса QMainWindow. Затем, используя метод addMenu(), добавляем пункт меню File, после чего подключаем объект exit к созданному пункту.
# Панель инструментов
Меню объединяет все команды, которые мы можем использовать в приложении. Панели инструментов, в свою очередь, предоставляют быстрый доступ к наиболее часто употребляемым командам.

9.  GUI приложения управляются командами, и эти команды могут быть запущены из меню, контекстного меню, панели инструментов или с помощью горячих клавиш. PyQt упрощает разработку с введением действий (actions). Объект action может иметь текст меню, иконку, ярлык (клавиатурное сочетание), статусный текст, текст «What's This?» и всплывающую подсказку. В нашем примере мы определим объект action с иконкой, ярлыком и всплывающей подсказкой.
```
self.connect(self.exit, QtCore.SIGNAL('triggered()'),
QtCore.SLOT('close()'))
```
Здесь мы соединяем сигнал triggered() объекта action с предопределённым сигналом close().
```
self.toolbar = self.addToolBar('Exit')
self.toolbar.addAction(self.exit)
```
Создаём панель инструментов и устанавливаем на неё объект action.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/web.png"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
10. All
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QtGui.QAction(QtGui.QIcon(os.getcwd() + "/icons/close.png"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
11. QLabel
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        lbl1 = QtGui.QLabel('ZetCode', self)
        lbl1.move(15, 10)

        lbl2 = QtGui.QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QtGui.QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
12. Box Layout
Управление расположением с помощью классов раскладки является более гибким и практичным. Это предпочтительный способ расположения виджетов. Простые классы раскладки это QHBoxLayout и QVBoxLayout. Они располагают виджеты горизонтально и вертикально.
Представим, что мы хотим разместить две кнопки в правом нижнем углу формы. Чтобы создать такую раскладку мы будем использовать один горизонтальный и один вертикальный ящик (box). Необходимое пространство мы получим добавив фактор растяжения (stretch factor).
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
13.  QGridLayout
Самый универсальный класс раскладок это расположение таблицей. Эта раскладка делит пространство на строки и столбцы. Для её создания используется класс QgridLayout.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

```
В нашем примере, мы создаём таблицу кнопок. Одну ячейку оставляем пустой, добавляя один виджет QLabel.
```
grid = QtGui.QGridLayout()
```
Здесь мы создаём раскладку таблицей.
```
if j == 2:
    grid.addWidget(QtGui.QLabel(''), 0, 2)
else:
    grid.addWidget(button, pos[j][0], pos[j][1])
```
Чтобы добавить виджет в таблицу мы должны вызвать метод addWidget(), передав в качестве аргументов виджет, а также номера строки и столбца.


14. Виджеты могут занимать несколько строк или столбцов 
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
Создаём раскладку таблицей и указываем расстояние между виджетами.
```
grid.addWidget(reviewEdit, 3, 1, 5, 1)
```
Если мы добавляем виджет в раскладку, мы можем указать сколько строк или столбцов он объединяет. В нашем случае reviewEdit объединяет 5 строк.

15. QInputDialog
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')

        if ok:
            self.le.setText(str(text))

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
16. getOpenFileName
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code PyQt4

In this example, we create a simple
window in PyQt4.

"""
import sys, os
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
```
