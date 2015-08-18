# 21-python

- Объектно-ориентированное программирование на Python
[Особенности ООП в Python](https://slides.com/janusnicon/class-inside/)

# основные идеи ООП:
1. наследование. Возможность выделять общие свойства и методы классов в один класс верхнего уровня (родительский). Классы, имеющие общего родителя, различаются между собой за счет включения в них различных дополнительных свойств и методов.

2.  Инкапсуляция. Свойства и методы класса делятся на доступные из вне (опубликованные) и недоступные (защищенные). Защищенные атрибуты нельзя изменить, находясь вне класса. Опубликованные же атрибуты также называют интерфейсом объекта, т. к. с их помощью с объектом можно взаимодействовать.

3.  Полиморфизм. Полиморфизм подразумевает замещение атрибутов, описанных ранее в других классах: имя атрибута остается прежним, а реализация уже другой. Полиморфизм позволяет специализировать (адаптировать) классы, оставляя при этом единый интерфейс взаимодействия.

# Особенности ООП в Python
1.  Любое данное — это объект. Число, строка, список, массив и др. — все является объектом. Бывают объекты встроенных классов, а бывают объекты пользовательских классов. Для единого механизма взаимодействия предусмотрены методы перегрузки операторов.

2.  Класс — это тоже объект с собственным пространством имен.  

3.  Инкапсуляции в Python не уделяется особого внимания. В других языках программирования обычно нельзя получить напрямую доступ к свойству, описанному в классе. Для его изменения может быть предусмотрен специальный метод. В Python же это легко сделать, просто обратившись к свойству класса из вне. Несмотря на это в Python все-таки предусмотрены специальные способы ограничения доступа к переменным в классе.

# Инкапсуляция
```
  class Person(object):
      """docstring for Foo
           Одиночное подчеркивание в начале имени атрибута говорит о том,
           что переменная или метод не предназначен для использования
           вне методов класса, однако атрибут доступен по этому имени
      """

      #initialize name, ID number, city
      def __init__(self, fname, lname, ID, city):
          self.__ID = ID
          self.__first_name  = fname
          self.__last_name  = lname
          self.__city = city

      def _getName(self):
          s = ' '
          return s.join((self.__first_name, self.__last_name))

      #display Person name
      def show_person(self):
          print('Name:', self._getName())
          print('ID:', self.__ID)
          print('City:', self.__city)

  john = Person('John', 'Sidorov', 123456, 'NYC')

  print john._getName()


  ```
  Двойное подчеркивание в начале имени атрибута:
  атрибут становится недоступным по этому имени.

```

print john.__city

```
Однако полностью это не защищает, так как атрибут всё равно остаётся доступным под именем

```
_ИмяКласса__ИмяАтрибута
print john._Person__city

```
# Проверка способа запуска модуля

```
if __name__ == '__main__':
    # Create an person
    john = Person(
        fname='John', lname='Paw', city="NYC", ID=223344
    )
    mary = Person(
        fname='Mary', lname='Sue', city='LA', ID=113344
    )

```
- Как получить список всех атрибутов объекта

```
print dir(mary)

```
- __doc__ : Class documentation string or None if undefined.

```

print "Person.__doc__:", Person.__doc__

#__name__: Class name
print "Person.__name__:", Person.__name__

#__module__: Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print "Person.__module__:", Person.__module__

#__bases__ : A possibly empty tuple containing the base classes, in the order
#of their occurrence in the base class list.
print "Person.__bases__:", Person.__bases__

#__dict__ : Dictionary containing the class's namespace
print "Person.__dict__:", Person.__dict__

print '+++++Mary has+++++'
print "mary.__doc__:", mary.__doc__

print "mary.__module__:", mary.__module__
print "mary.__dict__:", mary.__dict__

# print "mary.__name__:", mary.__name__
# print "mary.__bases__:", mary.__bases__


```
- Как получить список всех публичных атрибутов объекта

Сделать это можно или с помощью списковых выражений (list comprehension):
```
print [arg for arg in dir(Person) if not arg.startswith('_')]

```
или воспользоваться функцией filter:
```
print filter(lambda x: not x.startswith('_'), dir(Person))

```

- Как получить список методов объекта
```
print [arg for arg in dir(Person) if callable(getattr(Person, arg))]

```
или
```
print filter(lambda arg: callable(getattr(Person, arg)), dir(Person))

```
1. __new__(cls, [...)
Это первый метод, который будет вызван при инициализации объекта. Он принимает в качестве параметров класс и потом любые другие аргументы, которые будут переданы в __init__. __new__ используется весьма редко, но иногда бывает полезен, в частности, когда класс наследуется от неизменяемого (immutable) типа, такого как кортеж (tuple) или строка.

2. __init__(self, [...)
Инициализатор класса. Ему передаётся всё, с чем был вызван первоначальный конструктор. __init__ почти повсеместно используется при определении классов.

3. __del__(self)
__del__ это деструктор. __del__ всегда вызывается по завершении работы интерпретатора.

4. __format__(self, formatstr)
Определяет поведение, когда экземпляр класса используется в форматировании строк нового стиля. Это может быть полезно для определения собственных числовых или строковых типов, которым вы можете предоставить какие-нибудь специальные опции форматирования.

```
def __format__(self, formatstr):
    return formatstr

    def __format__(self, format_spec):
        if isinstance(format_spec, unicode):
            return unicode(str(self))
        else:
            return str(self)

    #display name
    def show_person(self):
        print 'Name', format(self._getName(),'<9')
        print 'ID:', format(self.__ID,'<9')
        print('City:', self.__city)

    def getfName(self):
        fmt = ':>30'
        return format(self.__first_name, fmt)

```
5. __hash__(self)
Определяет поведение функции hash(), вызыванной для экземпляра вашего класса. Метод должен возвращать целочисленное значение, которое будет использоваться для быстрого сравнения ключей в словарях. Заметьте, что в таком случае обычно нужно определять и __eq__ тоже. Руководствуйтесь следующим правилом: a == b подразумевает hash(a) == hash(b).

6. __getattr__(self, name)
Вы можете определить поведение для случая, когда пользователь пытается обратиться к атрибуту, который не существует (совсем или пока ещё). Это может быть полезным для перехвата и перенаправления частых опечаток, предупреждения об использовании устаревших атрибутов, или хитро возвращать AttributeError, когда это вам нужно.

7. __setattr__(self, name, value)
В отличии от __getattr__, __setattr__ решение для инкапсуляции. Этот метод позволяет вам определить поведение для присвоения значения атрибуту, независимо от того существует атрибут или нет. То есть, вы можете определить любые правила для любых изменений значения атрибутов.

8. __delattr__
Это то же, что и __setattr__, но для удаления атрибутов, вместо установки значений.

9. __getattribute__(self, name)
__getattribute__ может использоваться только с классами нового типа. Этот метод позволяет вам определить поведение для каждого случая доступа к атрибутам (а не только к несуществующим, как __getattr__(self, name)). Он страдает от таких же проблем с бесконечной рекурсией, как и его коллеги (на этот раз вы можете вызывать __getattribute__ у базового класса, чтобы их предотвратить). Он  главным образом устраняет необходимость в __getattr__, который в случае реализации __getattribute__ может быть вызван только явным образом или в случае генерации исключения AttributeError.

10. __reduce__(self)
 __reduce__() вызывается когда сериализуется объект, в котором этот метод был определён. Он должен вернуть или строку, содержащую имя глобальной переменной, содержимое которой сериализуется как обычно, или кортеж. Кортеж может содержать от 2 до 5 элементов: вызываемый объект, который будет вызван, чтобы создать десериализованный объект, кортеж аргументов для этого вызываемого объекта, данные, которые будут переданы в __setstate__ (опционально), итератор списка элементов для сериализации (опционально) и итератор словаря элементов для сериализации (опционально).

11. __reduce_ex__(self, protocol)
Иногда полезно знать версию протокола, реализуя __reduce__. И этого можно добиться, реализовав вместо него __reduce_ex__. Если __reduce_ex__ реализован, то предпочтение при вызове отдаётся ему.

12. __sizeof__(self)
Определяет поведение функции sys.getsizeof(), вызыванной на экземпляре вашего класса. Метод должен вернуть размер вашего объекта в байтах. Он главным образом полезен для классов, определённых в расширениях на C.


# Перегрузка операторов Наследование

calling the parent class's __init__ method

```

class Employer(Person):
    """ An employer is a person who runs a company.

    """
    # The name of the company

    def __init__(self, fname, lname, ID, city,company_name):
        Person.__init__(self, fname, lname, ID, city)
        self.company_name = company_name



# Проверка способа запуска модуля

if __name__ == '__main__':
    # Create an employee with a boss
    boss_john = Employer(
        fname='John', lname='Paw', city="NYC", ID=223344, company_name="Packrat's Cats"
    )

    boss_john .show_person()

```

# Проверка способа запуска модуля
```
if __name__ == '__main__':
    # Create an employee with a boss
    boss_john = Employer(
        fname='John', lname='Paw', city="NYC", ID=223344, company_name="Packrat's Cats"
    )

    boss_john .show_person()
    #__name__: Class name
    print "Employer.__name__:", Employer.__name__

    #__dict__ : Dictionary containing the class's namespace
    print "boss_john.__dict__:", boss_john.__dict__

    def show_person(self):
        Person.show_person(self)
        print('Company Name:',self.company_name)

```
Use super() instead of calling the parent class's __init__ method. It makes multiple inheritance a bit easier.

```
class Employer(Person):
    """ An employer is a person who runs a company.

    """
    # The name of the company
    def __init__(self,fname, lname, ID, city, company_name):
        super(Employer, self).__init__(fname, lname, ID, city)
        self.company_name = company_name
```

- super(self.__class__, self)

```
class Employer(Person):
    """ An employer is a person who runs a company.

    """
    # The name of the company
    def __init__(self,fname, lname, ID, city, company_name):
        super(self.__class__, self).__init__(fname, lname, ID, city)
        self.company_name = company_name

    def show_person(self):
        super(self.__class__, self).show_person()
        print('Company Name:',self.company_name)
```
- using kwargs, and then pop

```
class Employer(Person):
    """ An employer is a person who runs a company.

    """
    # The name of the company
    def __init__(self,*args, **kwargs):
        self.company_name = kwargs.pop('company_name')
        super(self.__class__, self).__init__(*args, **kwargs)

```
- using kwargs
```
class Person(object):
    """ A simple class representing a person object.

    """

    def __init__(self, *args, **kwargs):
        self.__ID = kwargs['ID']
        self.__first_name  = kwargs['fname']
        self.__last_name  = kwargs['lname']
        self.__city = kwargs['city']
```
- class Employee

```
class Employee(Person):
    """ An employee is person with a boss and a phone number.

    """
    # initialize method calls superclass
    def __init__(self,*args, **kwargs):
        self.__base_pay = kwargs['base_pay']
        self.__shift = kwargs['shift']
        super(self.__class__, self).__init__(*args, **kwargs)


        employee_mary = Employee( fname='Mary', lname='Sue', city="NYC", ID=113344, base_pay=10000, shift=2)

        #__dict__ : Dictionary containing the class's namespace
        print "employee_mary.__dict__:", employee_mary.__dict__

```

- show_pay перезагрузка superclass

```
#set global constant
SHIFT_2 = 0.05
SHIFT_3 = 0.10


    def show_pay(self):
        if self.__shift == 1:
            print('My salary is ', self.__base_pay)
        elif self.__shift == 2:
            print('My salary is ', (self.__base_pay * SHIFT_2) + self.__base_pay)
        elif self.__shift == 3:
            print('My salary is ', (self.__base_pay * SHIFT_3) + self.__base_pay)

...
  employee_mary = Employee( fname='Mary', lname='Sue', city="NYC", ID=113344, base_pay=10000, shift=2)
  employee_mary.show_pay()

```
- property

```
def __init__(self):
    self._name = ''

def fget(self):
    print "Getting: %s" % self._name
    return self._name

def fset(self, value):
    print "Setting: %s" % value
    self._name = value.title()

def fdel(self):
    print "Deleting: %s" %self._name
    del self._name
name = property(fget, fset, fdel, "I'm the property.")


```

- property decorator

```
@property
def base_pay(self):
    return self.__base_pay

@base_pay.setter
def base_pay(self, new_salary):
    if new_salary < 0:
        raise ValueError('salary must be positive')
    self.__base_pay = new_salary


    employee_mary = Employee( fname='Mary', lname='Sue', city="NYC", ID=113344, base_pay=10000, shift=2)
      employee_mary.base_pay = 15000
      print employee_mary.base_pay
      employee_mary.show_pay()

  ```

  - Аналогично можно перегрузить метод deleter:

```

    @base_pay.deleter
    def base_pay(self):
        del self.__base_pay
```
- Динамические свойства

```
def addProperty(self, attribute):
      # create local setter and getter with a particular attribute name
      getter = lambda self: self._getProperty(attribute)
      setter = lambda self, value: self._setProperty(attribute, value)

      # construct property attribute and add it to the class
      setattr(self.__class__, attribute, property(fget=getter, \
                                                  fset=setter, \
                                                  doc="Auto-generated method"))

  def _setProperty(self, attribute, value):
      print "Setting: %s = %s" %(attribute, value)
      setattr(self, '_' + attribute, value.title())

  def _getProperty(self, attribute):
      print "Getting: %s" %attribute
      return getattr(self, '_' + attribute)

      employee_mary.addProperty('phone')
      employee_mary.phone = '123 456 777'
      print employee_mary.phone  

```
# Перегрузка операторов, строковое представление

- __str__(self)
Определяет поведение функции str(), вызванной для экземпляра вашего класса.

```
class Command(object):
    def __init__(self, *employees):
        self.employees = employees
        self.cost = sum(employee.cost for employee in employees)
        self.level = max(employee.cost for employee in employees)

    def __add__(self, other):
        if isinstance(other, Employee):
            return Command(other, *self.employees)

    def __str__(self):
        return 'Command (cost={b.cost}, level={b.level}) {b.employees}'.format(b=self)

```
- __repr__(self)
Определяет поведение функции repr(), вызыванной для экземпляра вашего класса. Главное отличие от str() в целевой аудитории. repr() больше предназначен для машинно-ориентированного вывода (более того, это часто должен быть валидный код на Питоне), а str() предназначен для чтения людьми.

```
def __add__(self, other):
    if isinstance(other, self.__class__):
        return Command(self, other)

def __repr__(self):
    return '{u.name} (cost={u.cost}, level={u.level})'.format(u=self)

```
- __unicode__(self)
Определяет поведение функции unicode(), вызыванной для экземпляра вашего класса. unicode() похож на str(), но возвращает строку в юникоде. Будте осторожны: если клиент вызывает str() на экземпляре вашего класса, а вы определили только __unicode__(), то это не будет работать. Постарайтесь всегда определять __str__() для случая, когда кто-то не имеет такой роскоши как юникод.


# Магические методы сравнения

- __cmp__(self, other)
Самый базовый из методов сравнения. Он, в действительности, определяет поведение для всех операторов сравнения (>, ==, !=, итд.), но не всегда так, как вам это нужно (например, если эквивалентность двух экземпляров определяется по одному критерию, а то что один больше другого по какому-нибудь другому). __cmp__ должен вернуть отрицательное число, если self < other, ноль, если self == other, и положительное число в случае self > other. Но, обычно, лучше определить каждое сравнение, которое вам нужно, чем определять их всех в __cmp__. Но __cmp__ может быть хорошим способом избежать повторений и увеличить ясность, когда все необходимые сравнения оперерируют одним критерием.

- __eq__(self, other)
Определяет поведение оператора равенства, ==.

- __ne__(self, other)
Определяет поведение оператора неравенства, !=.

- __lt__(self, other)
Определяет поведение оператора меньше, <.

- __gt__(self, other)
Определяет поведение оператора больше, >.

- __le__(self, other)
Определяет поведение оператора меньше или равно, <=.

- __ge__(self, other)
Определяет поведение оператора больше или равно, >=.

# Числовые магические методы

- __pos__(self)
Определяет поведение для унарного плюса (+some_object)

- __neg__(self)
Определяет поведение для отрицания(-some_object)

- __abs__(self)
Определяет поведение для встроенной функции abs().

- __invert__(self)
Определяет поведение для инвертирования оператором ~. Для объяснения что он делает смотри статью в Википедии о бинарных операторах.

- __round__(self, n)
Определяет поведение для встроенной функции round(). n это число знаков после запятой, до которого округлить.

- __floor__(self)
Определяет поведение для math.floor(), то есть, округления до ближайшего меньшего целого.

- __ceil__(self)
Определяет поведение для math.ceil(), то есть, округления до ближайшего большего целого.

- __trunc__(self)
Определяет поведение для math.trunc(), то есть, обрезания до целого.

# Обычные арифметические операторы

- __add__(self, other)
Сложение.

- __sub__(self, other)
Вычитание.

- __mul__(self, other)
Умножение.

- __floordiv__(self, other)
Целочисленное деление, оператор //.

- __div__(self, other)
Деление, оператор /.

- __truediv__(self, other)
Правильное деление. Заметьте, что это работает только когда используется from __future__ import division.

- __mod__(self, other)
Остаток от деления, оператор %.

- __divmod__(self, other)
Определяет поведение для встроенной функции divmod().

- __pow__
Возведение в степень.

- __lshift__(self, other)
Двоичный сдвиг влево, оператор <<.

- __rshift__(self, other)
Двоичный сдвиг вправо, оператор >>.

- __and__(self, other)
Двоичное И, оператор &.

- __or__(self, other)
Двоичное ИЛИ, оператор |.

- __xor__(self, other)
Двоичный xor, оператор ^.

# Отражённые арифметические операторы

- __radd__(self, other)
Отражённое сложение.

- __rsub__(self, other)
Отражённое вычитание.

- __rmul__(self, other)
Отражённое умножение.

- __rfloordiv__(self, other)
Отражённое целочисленное деление, оператор //.

- __rdiv__(self, other)
Отражённое деление, оператор /.

- __rtruediv__(self, other)
Отражённое правильное деление. Заметьте, что работает только когда используется from __future__ import division.

- __rmod__(self, other)
Отражённый остаток от деления, оператор %.

- __rdivmod__(self, other)
Определяет поведение для встроенной функции divmod(), когда вызывается divmod(other, self).

- __rpow__
Отражённое возведение в степерь

- __rlshift__(self, other)
Отражённый двоичный сдвиг влево

- __rrshift__(self, other)
Отражённый двоичный сдвиг вправо

- __rand__(self, other)
Отражённое двоичное И, оператор &.

- __ror__(self, other)
Отражённое двоичное ИЛИ, оператор |.

- __rxor__(self, other)
Отражённый двоичный xor, оператор ^.


# Составное присваивание

- __iadd__(self, other)
Сложение с присваиванием.

- __isub__(self, other)
Вычитание с присваиванием.

- __imul__(self, other)
Умножение с присваиванием.

- __ifloordiv__(self, other)
Целочисленное деление с присваиванием, оператор //=.

- __idiv__(self, other)
Деление с присваиванием, оператор /=.

- __itruediv__(self, other)
Правильное деление с присваиванием.

- __imod_(self, other)
Остаток от деления с присваиванием

- __ipow__
Возведение в степерь с присваиванием

- __ilshift__(self, other)
Двоичный сдвиг влево с присваиванием, оператор <<=.

- __irshift__(self, other)
Двоичный сдвиг вправо с присваиванием, оператор >>=.

- __iand__(self, other)
Двоичное И с присваиванием, оператор &=.

- __ior__(self, other)
Двоичное ИЛИ с присваиванием, оператор |=.

- __ixor__(self, other)
Двоичный xor с присваиванием, оператор ^=.

# Магические методы преобразования типов

- __int__(self)
Преобразование типа в int.

- __long__(self)
Преобразование типа в long.

- __float__(self)
Преобразование типа в float.

- __complex__(self)
Преобразование типа в комплексное число.

- __oct__(self)
Преобразование типа в восьмеричное число.

- __hex__(self)
Преобразование типа в шестнадцатиричное число.

- __index__(self)
Преобразование типа к int, когда объект используется в срезах (выражения вида [start:stop:step]). Если вы определяете свой числовый тип, который может использоваться как индекс списка, вы должны определить __index__.

- __trunc__(self)
Вызывается при math.trunc(self). Должен вернуть своё значение, обрезанное до целочисленного типа (обычно long).

- __coerce__(self, other)
Метод для реализации арифметики с операндами разных типов. __coerce__ должен вернуть None если преобразование типов невозможно. Если преобразование возможно, он должен вернуть пару (кортеж из 2-х элементов) из self и other, преобразованные к одному типу.
