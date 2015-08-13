# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __del__(self):
        print "Удаляется record %s " % self.name

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay) 
    def giveRaise(self, percent, bonus=100):
        Person.giveRaise(self, percent + bonus)
 
# Создаем первый инстанс класса Person:
ivan = Person('Иван Petrov')

# Создаем второй инстанс класса Person:
john = Person('John Sidorov', job='dev', pay=100000)
john.giveRaise(.10)

tom = Manager('Tom Jones', 50000)

print tom

# Начисляем мегапремиальные:
tom.giveRaise(.10)
print tom
