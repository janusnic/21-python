# -*- coding:utf-8 -*-

# Перегрузка математических операций.
# Создаем класс-точку, имеем точку в двухмерном пространстве:

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

