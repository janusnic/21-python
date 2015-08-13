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
print '''
Работа с атрибутам объекта: 
	установка, удаление и поиск, 
	равносильна вызову встроенных функций 
	settattr, delattr, getattr:

    '''
print 'атрибут объекта установка a.x = 1:'
a.x = 1 
print a.x 
print 'атрибут объекта установка setattr(a, "x", 100):'
setattr(a, 'x', 100)
print a.x 
print 'атрибут объекта поиск getattr(a,"x"):'
print getattr(a,'x')
print 'атрибут объекта удаление del a.x | delattr(a,"x"):'
delattr(a,'x')
print 'getattr(a,"x") - AttributeError: "A" object has no attribute "x"'
# print getattr(a,'x')
#del a.x 
print 'a.qux= ', a.qux

print '''
 если мы попытаемся изменить (установить) атрибут, 
 setattr поместит его в __dict__, 
 специфичный для данного, конкретного объекта.
 b = A()
 print b.qux # 'A'
 a.qux = 'myB'
 print a.qux # 'myB'
 print a.__dict__ # {'qux': 'myB', 'name': 'a'}
 print b.qux # 'A'

    '''

b = A
print b.qux # 'A'
a.qux = 'myB'
print a.qux # 'myB'
print a.__dict__ # {'qux': 'myB', 'name': 'a'}
print b.qux # 'A'




