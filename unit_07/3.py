# -*- coding: utf-8 -*-
class A(object):
    qux = 'A'
    def __init__(self, name):
        self.name=name
    def foo(self):
        print 'foo'

a = A('a')
print '''
class A(object):
    qux = 'A'
    def __init__(self, name):
        self.name=name
    def foo(self):
        print 'foo'

a = A('a')
    '''

print '__dict__ у классов не совсем словарь'
print A.__dict__ 

print "__dict__ ответственен за доступ к внутреннему пространству имен, в котором хранятся методы, дескрипторы, переменные, свойства и прочее:"

print dict(A.__dict__) 
print A.__dict__.keys()

print "Класс является объектом."

print isinstance(A, object) # True

print "Число — это тоже объект."

print isinstance(42, object) # True

print "Класс — это класс (т.е. тип)."

print isinstance(A, type) # True

print 'А вот число классом (типом) не является. (Что такое type будет пояснено позже)'

print isinstance(42, type) # False

print "Ну и a — тоже обычный объект."

a = A
print isinstance(a, A) # True
print isinstance(a, object) # True
print isinstance(a, type) # False

print 'И у A всего один прямой родительский класс — object.'

print A.__bases__ # (&lt;type 'object'&gt;,)

print "Часть специальных параметров можно даже менять:"

print A.__name__ # 'A'
A.__name__ = 'B'
print A # &lt;class '__main__.B'&gt;

print "С помощью getattr получаем доступ к атрибутам класса:"

print A.qux # 'A'
A.foo # &lt;unbound method A.foo&gt;

a = A
b = A

print b.qux # 'A'
print A.qux # 'A'

print "Меняем атрибут qux у класса A. И соответственно должны поменяться значения, которые возвращают экземпляры класса A — a и b:"

A.qux='B'
print a.qux # 'B'
print b.qux # 'B'

