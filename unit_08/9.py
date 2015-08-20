# -*- coding:utf-8 -*-

def shout(word="да"):
    return word.capitalize()+"!"

print shout() # выведет: 'Да!'

# Так как функция - это объект - связать её с переменнной,

scream = shout

print scream() # выведет: 'Да!'

# мы можем удалить "shout", и функция всё ещё будет доступна через переменную "scream"

del shout

try:
    print shout()
except NameError, e:
    print e     #выведет: "name 'shout' is not defined"

print scream() # выведет: 'Да!'
