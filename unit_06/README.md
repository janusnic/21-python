# 21-python

[Объектно-ориентированное программирование на Python](https://slides.com/janusnicon/python-oop/)

## Принципы ООП

- Все данные представляются объектами
- Программа является набором взаимодействующих объектов, посылающих друг другу сообщения
- Каждый объект имеет собственную часть памяти и может иметь в составе другие объекты
- Каждый объект имеет тип
- Объекты одного типа могут принимать одни и те же сообщения (и выполнять одни и те же действия)

## Определение класса
```
class имя_класса(надкласс1, надкласс2, ...):
        # определения атрибутов и методов класса
```

У класса могут быть базовые (родительские) классы (надклассы), которые (если они есть) указываются в скобках после имени определяемого класса.

## Минимально возможное определение класса выглядит так:
```
    class A:
        pass

```

В терминологии Python члены класса называются экземплярами, функции класса — методами, а поля класса — свойствами (или просто атрибутами).

Определения методов аналогичны определениям функций, но методы всегда имеют первый аргумент, называемый по широко принятому соглашению self:

```
    class A:
        def m1(self, x):
            # блок кода метода
```

Определения атрибутов — обычные операторы присваивания, которые связывают некоторые значения с именами атрибутов.
```
    class A:
        attr1 = 2 * 2

```
В языке Python класс не является чем-то статическим после определения, поэтому добавить атрибуты можно и после:
```
    class A:
        pass

    def myMethod(self, x):
        return x * x

    A.m1 = myMethod
    A.attr1 = 2 * 2
```
## Создание экземпляра

Для создания объекта — экземпляра класса (то есть, инстанцирования класса), достаточно вызвать класс по имени и задать параметры конструктора:
```
    class Point:
         def __init__(self, x, y, z):
             self.coord = (x, y, z)
         def __repr__(self):
             return "Point(%s, %s, %s)" % self.coord
>>> p = Point(0.0, 1.0, 0.0)
>>> p
Point(0.0, 1.0, 0.0)

```
## метод __new__
Переопределив классовый метод __new__, можно контролировать процесс создания экземпляра. Этот метод вызывается до метода __init__ и должен вернуть новый экземпляр, либо None (в последнем случае будет вызван __new__ родительского класса). Метод __new__ используется для управления созданием неизменчивых (immutable) объектов, управления созданием объектов в случаях, когда __init__ не вызывается, например, при десериализации (unpickle). Следующий код демонстрирует один из вариантов реализации шаблона Одиночка:
```
>>> class Singleton(object):
        obj = None                           # Атрибут для хранения единственного экземпляра
        def __new__(cls,*dt,**mp):           # класса Singleton.
           if cls.obj is None:               # Если он еще не создан, то
              cls.obj = object.__new__(cls,*dt,**mp) # вызовем __new__ родительского класса
           return cls.obj                    # вернем синглтон
...
>>> obj = Singleton()
>>> obj.attr = 12
>>> new_obj = Singleton()
>>> new_obj.attr                       
12
>>> new_obj is obj                     # new_obj и obj - это один и тот же объект
True
```

## Конструктор и деструктор

Специальные методы вызываются при создании экземпляра класса (конструктор) и при удалении класса (деструктор). В языке Python реализовано автоматическое управление памятью, поэтому деструктор требуется достаточно редко, для ресурсов, требующих явного освобождения.
```

class Line:
    def __init__(self, p1, p2):
        self.line = (p1, p2)
    def __del__(self):
        print "Удаляется линия %s - %s" % self.line
>>> l = Line((0.0, 1.0), (0.0, 2.0))
>>> del l
Удаляется линия (0.0, 1.0) - (0.0, 2.0)
>>>
```
## Инкапсуляция и доступ к свойствам
Все значения в Python являются объектами, инкапсулирующими код (методы) и данные и предоставляющими пользователям общедоступный интерфейс. Методы и данные объекта доступны через его атрибуты.

## Сокрытие информации о внутреннем устройстве объекта
Сокрытие информации о внутреннем устройстве объекта выполняется в Python на уровне соглашения между программистами о том, какие атрибуты относятся к общедоступному интерфейсу класса, а какие — к его внутренней реализации. Одиночное подчеркивание в начале имени атрибута говорит о том, что метод не предназначен для использования вне методов класса (или вне функций и классов модуля), однако, атрибут все-таки доступен по этому имени. Два подчеркивания в начале имени дают несколько большую защиту: атрибут перестает быть доступен по этому имени.

Особым случаем является наличие двух подчеркиваний в начале и в конце имени атрибута. Они используются для специальных свойств и функций класса (например, для перегрузки операции). Такие атрибуты доступны по своему имени, но их использование зарезервировано для специальных атрибутов, изменяющих поведение объекта.

## Доступ к атрибуту может быть как прямой:
```
class A(object):
    def __init__(self, x):          # атрибут получает значение в конструкторе
        self.x = x

a = A(5)
print a.x
a.x = 5
```
Так и с использованием свойств с заданными методами для получения, установки и удаления атрибута:

```
class A(object):
    def __init__(self, x):
        self._x = x
    def getx(self):                 # метод для получения значения
        return self._x
    def setx(self, value):          # присваивания нового значения
        self._x = value
    def delx(self):                 # удаления атрибута
        del self._x                 
    x = property(getx, setx, delx, "Свойство x")    # определяем x как свойство

a = A(5)      
print a.x      # Синтаксис доступа к атрибуту при этом прежний
a.x = 5

```
## Наследование
Python поддерживает как одиночное наследование, так и множественное, позволяющее классу быть производным от любого количества базовых классов.
```
>>> class Par1(object):                # наследуем один базовый класс - object
        def name1(self): return 'Par1'
>>> class Par2(object):
        def name2(self): return 'Par2'
>>> class Child(Par1, Par2):           # создадим класс, наследующий Par1, Par2 (и, опосредованно, object)
        pass
>>> x = Child()
>>> x.name1(), x.name2()               # экземпляру Child доступны методы из Par1 и Par2
'Par1','Par2'
```


## Полиморфизм
В Python все методы являются виртуальными, что является естественным следствием разрешения доступа на этапе исполнения.

```
>>> class Parent(object):
        def isParOrPChild(self) : return True
        def who(self) : return 'parent'
>>> class Child(Parent):
        def who(self): return 'child'
>>> x = Parent()
>>> x.who(), x.isParOrPChild()
('parent', True)
>>> x = Child()
>>> x.who(), x.isParOrPChild()
('child', True)
```
Явно указав имя класса, можно обратиться к методу родителя (как впрочем и любого другого объекта).
```
>>> class Child(Parent):
        def __init__(self):
            Parent.__init__(self)
```
В общем случае для получения класса-предка применяется функция super.

```
class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()

```

## __class__ 

```
def foo(): pass

print foo.__class__ 

>&lt;type 'function'&gt;

print foo.__dict__ 
> {}

print (42).__dict__ 

>Traceback (most recent call last): File "&lt;stdin&gt;", line 1, in &lt;module&gt; AttributeError: 'int' object has no attribute '__dict__'

print (42).__class__ 

> &lt;type 'int'&gt;

class A(object):
    qux = 'A'
    def __init__(self, name):
        self.name=name
    def foo(self):
        print 'foo'

a = A('a')
```

## У a тоже есть __dict__ и __class__:
```
print a.__dict__   

> {'name': 'a'}
print a.__class__  

> &lt;class '__main__.A'&gt;

print type(a) 

> &lt;class '__main__.A'&gt;

print a.__class__ is type(a) # True
```
## Класс и тип — это одно и то же.
```
print a.__class__ is type(a) is A 

> True
```
## Пример. Переопределим класс объекта a:
```
class B(object):
    qux = 'B'
    def __init__(self):
        self.name = 'B object'
    def bar(self):
         print 'bar'

print a.__dict__ 

> {'name': 'a'}

print a.foo() 

> foo

print a.__class__ 
> &lt;class '__main__.A'&gt;

a.__class__ = B

print a.__class__ 
> &lt;class '__main__.B'&gt;

```
## Смотрим, что поменялось.

Значение a.name осталось прежним, т.е. __init__ не вызывался при смене класса.
```
print a.__dict__ # {'name': 'a'}
```
- Доступ к классовым переменным и методам «прошлого» класса A пропал:
> a.foo() 
> Traceback (most recent call last): File "&lt;stdin&gt;", line 1, in &lt;module&gt; AttributeError: 'B' object has no attribute 'foo'
А вот классовые переменные и методы класса B доступы:
```
print a.bar() # bar
print a.qux # 'B'
```
Работа с атрибутам объекта: установка, удаление и поиск, равносильна вызову встроенных функций settattr, delattr, getattr:
```
a.x = 1
print a.x
setattr(a, 'x', 1)
print a.x

del a.x
> print a.x
> delattr(a, 'x')
> print a.x

> print a.x
> getattr(a, 'x')

При этом стоит стоит понимать, что setattr и delattr влияют и изменяют только сам объект (точнее a.__dict__), и не изменяют класс объекта.

qux — является классовой переменной, т.е. она «принадлежит» классу B, а не объекту a:
```
print a.qux 
>  'B'
print a.__dict__ 
> {'name': 'a'}
```
если мы попытаемся изменить (установить) атрибут, setattr поместит его в __dict__, специфичный для данного, конкретного объекта.
```
b = B()
print b.qux 
> 'B'
a.qux = 'myB'
print a.qux 
> 'myB'
print a.__dict__ 

> {'qux': 'myB', 'name': 'a'}
print b.qux 
> 'B'
```
 Ну и раз есть 'qux' в __dict__ объекта, его можно удалить с помощью delattr:

> del a.qux

После удаления, a.qux будет возвращать значение классовой переменной:
```
print a.qux 
> 'B'
print a.__dict__ # {'name': 'a'}
```
Правда __dict__ у классов не совсем словарь
```
print A.__dict__ 

> &lt;dictproxy object at 0x1111e88&gt;
```
__dict__ ответственен за доступ к внутреннему пространству имен, в котором хранятся методы, дескрипторы, переменные, свойства и прочее:
```
print dict(A.__dict__) 

> {'__module__': '__main__', 'qux': 'A', '__dict__': &lt;attribute '__dict__' of 'A' objects&gt;, 'foo': &lt;function foo at 0x7f7797a25c08&gt;, '__weakref__': &lt;attribute '__weakref__' of 'A' objects&gt;, '__doc__': None}
print A.__dict__.keys() # ['__module__', 'qux', '__dict__', 'foo', '__weakref__', '__doc__']&lt;
```
# Класс является объектом.
```
class A(object):
    pass


print isinstance(A, object) 
> True
```
# Число — это тоже объект.
```
print isinstance(42, object) 
> True
```
# Класс — это класс (т.е. тип).
```
print isinstance(A, type) 
> True
```
А вот число классом (типом) не является. (Что такое type будет пояснено позже)
```
print isinstance(42, type) 
> False
```
Ну и a — тоже обычный объект.
```
a = A()
print isinstance(a, A) 
> True
print isinstance(a, object) 
> True
print isinstance(a, type) 
> False
```
И у A всего один прямой родительский класс — object.
```
print A.__bases__ 
> (&lt;type 'object'&gt;,)
```
Часть специальных параметров можно даже менять:
```
print A.__name__ 
> 'A'
A.__name__ = 'B'
print A 
> &lt;class '__main__.B'&gt;
```
С помощью getattr получаем доступ к атрибутам класса:
```
print A.qux 
> 'A'
print A.foo 
> &lt;unbound method A.foo&gt;

class A(object):
    qux = 'A'
    def __init__(self, name):
        self.name=name
    def foo(self):
        print 'foo'

a = A
b = A

print b.qux 
> 'A'
print A.qux 
> 'A'
```
Меняем атрибут qux у класса A. И соответственно должны поменяться значения, которые возвращают экземпляры класса A — a и b:
```
A.qux='B'
print a.qux 
> 'B'
print b.qux 
> 'B'
```
Точно так же в рантайме к классу можно добавить метод:
```
A.quux = lambda self: 'i have quux method'
print A.__dict__['quux'] 
> &lt;function &lt;lambda&gt; at 0x7f7797a25b90&gt;
print A.quux 
> &lt;unbound method A.&lt;lambda&gt;&gt;
```
И доступ к нему появится у экземпляров:
```
print a.quux() 
> 'i have quux method'
```
объявим класс:
```
class A(object):
    pass
```
 Для класса A не определены ни __new__, ни __init__. В соответствии с алгоритмом поиска атрибутов для класса (типа), который не стоит путать с алгоритмом поиска атрибутов для обычных объектов, когда класс не найдет их в своем__dict__, он будет искать эти методы в __dict__ своих базовых (родительских) классах.

 Класс А имеет в качестве родителя встроенный класс object. Таким образом он будет их искать в object.__dict__
```
print object.__dict__['__init__'] 
> &lt;slot wrapper '__init__' of 'object' objects&gt;
print object.__dict__['__new__'] 
> &lt;built-in method __new__ of type object at 0x82e780&gt;
```

 Раз есть такие методы, значит, получается, что a = A() аналогичен последовательности вызовов:
```
a = object.__new__(A)
object.__init__(a)
```
В общем виде, используя super, который как раз и реализует алгоритм поиска атрибутов по родительским классам [1]:
```
a = super(A, A).__new__(A)
super(A, A).__init__(a)
```
# Пример.
```
class A(object):
    def __new__(cls):
        obj = super(A, cls).__new__(cls)
        print 'created object', obj
        return obj
    def __init__(self):
        print 'initing object', self
A()

> created object &lt;__main__.A object at 0x1620ed0&gt;
> initing object &lt;__main__.A object at 0x1620ed0&gt;
> &lt;__main__.A object at 0x1620ed0&gt;
```