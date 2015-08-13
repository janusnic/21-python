# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

# Создаем первый инстанс класса Person:
ivan = Person('Иван')

# Создаем второй инстанс класса Person:
john = Person('John', job='dev', pay=100000)

print ivan.name
print john.name

print ivan.job
print john.job

Person.lastName = None

ivan.lastName = 'Ivanov'
john.lastName = 'Sidorov'

print ivan.lastName
print john.lastName


