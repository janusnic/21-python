# -*- coding: utf-8 -*-
print '''
объявим класс:

class A(object):
    pass
'''
class A(object):
    pass

print '''
Точно так же в рантайме к классу можно добавить метод:
A.quux = lambda self: 'i have quux method'
'''

A.quux = lambda self: 'i have quux method'
print A.__dict__['quux'] # &lt;function &lt;lambda&gt; at 0x7f7797a25b90&gt;
print A.quux # &lt;unbound method A.&lt;lambda&gt;&gt;

print 'И доступ к нему появится у экземпляров:'
a = A()
print a.quux() # 'i have quux method'


print '''
Для класса A не определены ни __new__, ни __init__. 
В соответствии с алгоритмом поиска атрибутов для класса (типа), 
который не стоит путать с алгоритмом поиска атрибутов 
для обычных объектов, когда класс не найдет их в своем__dict__, 
он будет искать эти методы в __dict__ своих базовых (родительских) классах.
'''

print '''
Класс А имеет в качестве родителя встроенный класс object. 
Таким образом он будет их искать в object.__dict__
'''

print object.__dict__['__init__'] # &lt;slot wrapper '__init__' of 'object' objects&gt;
print object.__dict__['__new__'] # &lt;built-in method __new__ of type object at 0x82e780&gt;


print '''
 Раз есть такие методы, значит, получается, что a = A 
 аналогичен последовательности вызовов:

a = object.__new__(A)
object.__init__(a)
'''
a = object.__new__(A)
object.__init__(a)

print '''
В общем виде, используя super, 
который как раз и реализует алгоритм поиска 
атрибутов по родительским классам :
'''
a = super(A, A).__new__(A)
super(A, A).__init__(a)

# Пример.

class A(object):
    def __new__(cls):
        obj = super(A, cls).__new__(cls)
        print 'created object', obj
        return obj
    def __init__(self):
        print 'initing object', self
A()
