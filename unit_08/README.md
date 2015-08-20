# 21-python
- Построение системы управления записями сотрудников компании

[Исключения в Питоне](https://slides.com/janusnicon/except-in-python/)
```
class Employee(object):
    """ Класс сотрудники компании.

    """

    class Staff(object):

        def __init__(self):
            self.employee_list = []

        def add_employee(self, first_name, last_name, ID, city, base_pay, shift, hours):
            new_emp = employee.Employee(first_name, last_name, ID, city, base_pay, shift, hours)
            self.employee_list.append(new_emp)

```

# Исключения в Питоне
- Объектно-ориентированное программирование на Python Исключения в Питоне

# Errors
Существует (как минимум) два различимых вида ошибок: синтаксические ошибки (syntax errors) и исключения (exceptions).

# Синтаксические ошибки
```
while True print 'Hello world'
  File "<stdin>", line 1, in ?
    while True print 'Hello world'
                   ^
SyntaxError: invalid syntax
```

# Исключения

```
def fetcher(obj, index):
	return obj[index]

x = 'spam'
fetcher(x, 3)           # Like x[3] 'm'

fetcher(x, 4)

Traceback (most recent call last):
File "<stdin>", line 1, in ?
File "<stdin>", line 2, in fetcher
IndexError: string index out of range

```
Исключения представлены различными типами и тип исключения выводится в качестве части сообщения: в примере это типы ZeroDivisionError, NameError и TypeError. Часть строки, описывающая тип исключения — это имя произошедшего встроенного исключения. Такое утверждение истинно для всех встроенных исключений, но не обязано быть истинным для исключений, определённых пользователем (однако, само соглашение — довольно полезное). Имена стандартных исключений это встроенные идентификаторы (не ключевые слова).
Оставшаяся часть строки описывает детали произошедшего на основе типа исключения, которое было его причиной.
Предшествующая часть сообщения об ошибке показывает контекст, где произошло исключение, в форме стека вызовов. В общем случае она содержит стек, состоящий из списка строк исходного кода; тем не менее, в неё не войдут строки, прочитанные из стандартного ввода.

# Обработка исключений
Исключения свидетельствуют об ошибках и прерывают нормальный ход выполнения программы. Исключения возбуждаются с помощью инструкции raise. В общем случае инструкция raise имеет следующий вид:
raise Exception([value]), где Exception – тип исключения, а value – необязательное значение с дополнительной информацией об исключении.

```
Например:
raise RuntimeError(“Неустранимая ошибка”)

```

# Перехватить исключение можно с помощью инструкций try и except:

```
class Bad(Exception): pass

def doomed(): raise Bad()

try:
    doomed()
except Bad:
    print 'got Bad'

# got Bad

```

```
try:
    fetcher(x, 4)
except IndexError:
    print 'got exception' # got exception

def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print 'got exception'
    print 'continuing'

catcher() # got exception continuing
```

Если инструкция raise используется без дополнительных параметров, она повторно возбуждает последнее исключение (однако такой прием работает только в процессе обработки возникшего исключения).
Рассмотрим простейший пример: открытие файла. Если всё нормально — open(filename, 'r') возвращает объект этого самого файла Если файл не может быть открыт — выбрасывается исключение:
```
try:
    f = open(filename, 'r')
    try:
        print(f.read())
    finally:
        f.close()
except OSError as ex:
    print("Cannot process file", filename, ": Error is", ex)
```
Обратите внимание: файл нужно не только открыть но и закрыть после использования. Исключение может выбросить open (например, если файла нет на диске или нет прав на его чтение).
```
Traceback (most recent call last):
  File "fopen.py", line 5, in <module>
    f = open (filename, 'r')
IOError: [Errno 2] No such file or directory: 'file.txt'
</module>

```
Если файл открыт — читаем его через f.read(). Этот вызов тоже может выбросить исключение, но файл закрывать всё равно нужно. Поэтому необходим блок finally: f.close() должен быть вызван даже если f.read() сломался.

Исключения из обоих мест попадут в except OSError, где можно будет что-то сделать с ошибкой.
Питон делает явный выбор в пользу исключений перед возвратом кода ошибки в своём ядре и стандартной библиотеке.

# Типы исключений
```

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
  ```
- Самый базовый класс — BaseException. Он и его простые потомки (SystemExit, KeyboardInterrupt,GeneratorExit) не предназначены для перехвата обыкновенным программистом — только Питон и редкие библиотеки должны работать с этими типами. Нарушение правила ведет, например, к тому что программу невозможно корректно завершить.
Также не нужно перехватывать все исключения:
```
try:
    ...
except:
    ...
работает как

try:
    ...
except BaseException:
    ...
```
# используем операторы try и except, чтобы корректно и красиво завершить скрипт

```
'''функция диалога.
Первым аргументом принимаем ответ пользователя,
вторым - выдаём сообщение при неверном вводе'''

def answer(prompt, choice='Только Yes или no!'):
        while True:
                result = raw_input(prompt)
                if result in ('y', 'Y', 'yes', 'Yes'):
                        print '\nВы выбрали "YES" - заканчиваем\n'
                        '''тут можно использовать оператор break вместо return
                        так же и в ответе No'''
                        return False

                elif result in ('n', 'N', 'no', 'No'):
                        print "\nВы выбрали NO - Я продолжаю работу...\n"

                        print_menu()
                        return True
                else:

                        print(choice)
```

- при Ctrl+C (KeyboardInterrupt - SIGINT)
- или Ctrl+D (EOFError - SIGQUIT) команда
```
elif menu_choice == '7':
    try:
        if  (answer("\nВы уверены, что хотите закончить работу? ('y' или 'n', Ctrl+C для выхода) ")==False):
            break
    except (KeyboardInterrupt, EOFError):
        exit('\nВыход\n')
```

# Проиерка обязательных параметров

```
first_name = input("Имя сотрудника: ")
#validate
while first_name == '':
    print('\n Имя сотрудника required.  Try again.')
    first_name = input("Имя сотрудника: ")
last_name = input("Фамилия сотрудника: ")
#validate
while last_name == '':
    print('\n Фамилия сотрудника required.  Try again.')
    last_name = input("Фамилия сотрудника: ")

```

# Проверка допустимых значений параметров
```
ID_valid = False

      ID = input("Идентификатор сотрудника: ")

      while ID_valid == False:

          try:
              ID = float(ID)
              if ID > 0:
                  ID_valid = True
              else:
                  print("\nID должен быть > 0.  Пробуем еще.")
                  ID = input("Идентификатор сотрудника: ")
          except ValueError:
              print("\nID должен быть числом.  Пробуем еще..")
              ID = input("Идентификатор сотрудника:: ")
```



- Всё, что может быть нужно программисту — это Exception и унаследованные от него классы.

лучше ловить как можно более конкретные классы исключений
```
import os

filename = 'file.txt'
try:
    f = open (filename, 'r')
    try:
        print f.read()
    finally:
        f.close()
except (os.error, IOError) as ex:
    print "Cannot process file", filename, ": Error is", ex
```
нструкция finally служит для реализации завершающих действий, сопутствующих операциям, выполняемым в блоке try. Например:
```

try:
    # Выполнить некоторые действия

finally:

def print_staff():
    try:
        n = 0
        for emp in mystaff.employee_list:
            n += 1
            print(emp)

        if n==0 :
            raise MyError(2)
    except MyError as e:
        print '\nНет данных о сотрудниках :', e.value
    else:
        print  'Хранилище содержит ', n, ' строк'
    finally:
        print  'Дата проверки состояния записей ', datetime.now()

```
Блок finally не используется для обработки ошибок. Он используется для реализации действий, которые должны выполняться всегда, независимо от того, возникла ошибка или нет. Если в блоке try исключений не возникло, блок finally будет выполнен сразу же вcлед за ним. Если возникло исключение, управление сначала будет передано первой инструкции в блоке finally, а затем это исключение будет возбуждено повторно, чтобы обеспечить возможность его обработки в другом обработчике.
```
def fetcher(obj, index):
	return obj[index]

x = 'spam'
fetcher(x, 3)           # Like x[3] 'm'

try:
    fetcher(x, 3)
finally:
    print 'after fetch'


fetcher(x, 3)
print 'after fetch'

# KeyboardInterrupt.

while True:
    try:
        x = int(input("Введите, пожалуйста, число: "))
        break
    except ValueError:
        print("Ой!  Это некорректное число.  Попробуйте ещё раз...")
```
# Оператор try работает следующим образом:
- В начале исполняется блок try (операторы между ключевыми словами try и except).

- Если при этом не появляется исключений, блок except не выполняется и оператор try заканчивает работу.

- Если во время выполнения блока try было возбуждено какое-либо исключение, оставшаяся часть блока не выполняется.

- Затем, если тип этого исключения совпадает с исключением, указанным после ключевого слова except, выполняется блок except, а по его завершению выполнение продолжается сразу после оператора try-except.

- Если порождается исключение, не совпадающее по типу с указанным в блоке except — оно передаётся внешним операторам try; если ни одного обработчика не найдено, исключение считается необработанным (unhandled exception), и выполнение полностью останавливается и выводится сообщение.

# Оператор try может иметь более одного блока except
```
except (RuntimeError, TypeError, NameError):
    pass

```

# Исключения, определённые пользователем
```
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('Поймано моё исключение со значением:', e.value)

Поймано моё исключение со значением: 4

```
# Исключения, определённые пользователем
```
def print_staff():
    try:
        n = 0
        for emp in mystaff.employee_list:
            n += 1
            print(emp)

        if n==0 :
            raise MyError(2)
    except MyError as e:
        print '\nНет данных о сотрудниках :', e.value

```

# необязательный блок else
```
def print_staff():
    try:
        n = 0
        for emp in mystaff.employee_list:
            n += 1
            print(emp)

        if n==0 :
            raise MyError(2)
    except MyError as e:
        print '\nНет данных о сотрудниках :', e.value
    else:
        print  'Хранилище содержит ', n, ' строк'

```

При создании модуля, который может породить различные ошибки, обычной практикой будет создание базового класса для исключений, определённых в этом модуле, и подклассов для различных ошибочных состояний:

```
class Error(Exception):
    """Базовый класс для всех исключений в этом модуле."""
    pass

class InputError(Error):
    """Исключение порождается при ошибках при вводе.
     Атрибуты:
        expression -- выражение на вводе, в котором обнаружена ошибка
        message -- описание ошибки
    """
     def __init__(self, expression, message):
        self.expression = expression
        self.message = message
 class TransitionError(Error):
    """Порождается, когда операция пытается выполнить неразрешённый переход
    из одного состояния в другое.
     Attributes:
        previous -- состояние в начале перехода
        next -- новое состояние, попытка принять которое была принята
        message -- описание, по какой причине такой переход невозможен
    """
     def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```

# Семейство OSError

До Python 3.3 существовало много разных типов таких исключений: os.error, socket.error, IOError,WindowsError, select.error и т.д.
Это приводило к тому, что приходилось указывать несколько типов обрабатываемых исключений одновременно:

```
try:
    do_something()
except (os.error, IOError) as ex:
    pass
```
исключения операционной системы часто никак не проявляют себя при разработке.
Проблема решена в PEP 3151: пишите OSError и не ошибетесь (прочие имена оставлены для обратной совместимости и облегчения портирования кода на новую версию).

# У OSError есть атрибут errno, который содержит код ошибки.

Открываем файл, получаем OSError в ответ. Раньше мы должны были анализировать ex.errno чтобы понять, отчего произошла ошибка: может файла нет на диске, а может нет прав на запись — это разные коды ошибок (ENOENT если файла нет и EACCES или EPERM если нет прав).
Приходилось строить конструкцию вроде следующей:
```
try:
    f = open(filename)
except OSError as ex:
    if ex.errno == errno.ENOENT:
       handle_file_not_found(filename)
    elif ex.errno in (errno.EACCES, errno.EPERM):
       handle_no_perm(filename)
    else:
       raise  # обязательно выбрасывать не обработанные коды ошибки
```
Теперь иерархия расширилась. Полный список наследников OSError:
```
OSError
 +-- BlockingIOError
 +-- ChildProcessError
 +-- ConnectionError
 |    +-- BrokenPipeError
 |    +-- ConnectionAbortedError
 |    +-- ConnectionRefusedError
 |    +-- ConnectionResetError
 +-- FileExistsError
 +-- FileNotFoundError
 +-- InterruptedError
 +-- IsADirectoryError
 +-- NotADirectoryError
 +-- PermissionError
 +-- ProcessLookupError
 +-- TimeoutError
```
Наш пример можем переписать как:
```
try:
    f = open(filename)
except FileNotFound as ex:
    handle_file_not_found(filename)
except PermissionError as ex:
    handle_no_perm(filename)
```
