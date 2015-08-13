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
print 'a.__dict__=', a.__dict__ 

print 'a.foo()=', 
a.foo() 

print 'a.__class__=', a.__class__ 

class B(object):
    qux = 'B'
    def __init__(self):
        self.name = 'B object'
    def bar(self):
         print 'bar'

print '''
class B(object):
    qux = 'B'
    def __init__(self):
        self.name = 'B object'
    def bar(self):
         print 'bar'

    '''
a.__class__ = B
print 'a.__class__ = B'

print 'Значение a.name осталось прежним, т.е. __init__ не вызывался при смене класса.'
print 'a.__dict__=', a.__dict__ 

print 'Доступ к классовым переменным и методам «прошлого» класса A пропал'
print 'А вот классовые переменные и методы класса B доступы:'
a.bar() # bar
print 'a.qux=',a.qux # 'B'