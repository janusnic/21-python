# -*- coding:utf-8 -*-

while True:
    try:
        x = int(input("Введите, пожалуйста, число: "))
        break
    except NameError:
        print "Ой!  Это некорректное число.  Попробуйте ещё раз..."
