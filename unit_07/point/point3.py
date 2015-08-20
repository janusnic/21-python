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


    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

# 
print Point(1, 2) == Point(1, 2)
print Point(1, 2) == 1
