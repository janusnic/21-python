# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]

# Создаем первый инстанс класса Person:
ivan = Person('Иван Petrov')

# Создаем второй инстанс класса Person:
john = Person('John Sidorov', job='dev', pay=100000)

print ivan.name
print john.name

print ivan.lastName()
print john.lastName()


