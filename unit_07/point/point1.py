# -*- coding:utf-8 -*-

# Перегрузка математических операций.
# Создаем класс-точку, имеем точку в двухмерном пространстве:

class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y
    # Сравнение
    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

# попытка сравнить точку с не-точкой (Point(1, 2) == 1) выбросит исключениеAttributeError
print Point(1, 2) == Point(1, 2)
