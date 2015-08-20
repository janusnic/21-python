# -*- coding:utf-8 -*-

# Перегрузка математических операций.
# Создаем класс-точку, имеем точку в двухмерном пространстве:

class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y
    # Сравнение
    def __eq__(self, other):
    	if not isinstance(other, Point):
    		return NotImplemented
    	return self._x == other._x and self._y == other._y

    	
    def __ne__(self, other):
    	return not (self == other)

    # hash
    def __hash__(self):
    	return hash((self._x, self._y))

    # Арифметика
    # Точки можно складывать и вычитать.
    def __add__(self, other):
    	if not isinstance(other, Point):
    		return NotImplemented
    	return Point(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
    	if not isinstance(other, Point):
    		return NotImplemented
    	return Point(self._x - other._x, self._y - other._y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

# 
print Point(1, 2) == Point(1, 2)
print Point(1, 2) == 1
print {Point(1, 2): 0}
print {Point(1, 2): 0}

Point(1, 2) + Point(2, 3)
print Point(3, 5)

Point(1, 2) - Point(2, 3)
print Point(-1, -1)