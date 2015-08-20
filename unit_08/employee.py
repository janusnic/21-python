# -*- coding: utf-8 -*-

#set global constant
SHIFT_2 = 0.05
SHIFT_3 = 0.10


class Employee(object):
    """ Класс сотрудники компании.

    """
    # initialize method calls superclass
    def __init__(self,*args):
        self.__first_name  = args[0]
        self.__last_name  = args[1]
        self.__ID = args[2]
        self.__city = args[3]
        self.__base_pay = args[4]
        self.__shift = args[5]
        self.__hours=args[6]


    def get_name(self):
        s = ' '
        return s.join((self.__first_name, self.__last_name))

    def sethours(self,hours):
        self.__hours=hours

    def gethours(self):
        return self.__hours

    hours=property(gethours,sethours)

    @property
    def base_pay(self):
        return self.__base_pay

    @base_pay.setter
    def base_pay(self, new_salary):
        if new_salary < 0:
            raise ValueError('salary must be positive')
        self.__base_pay = new_salary

    #show_pay overrides the superclass and displays hourly pay rates
    def show_pay(self):
        if self.__shift == 1:
            return (self.__base_pay*self.__hours)
        elif self.__shift == 2:
            return  (self.__base_pay * SHIFT_2 + self.__base_pay)*self.__hours
        elif self.__shift == 3:
            return  (self.__base_pay * SHIFT_3 + self.__base_pay)*self.__hours

    def __repr__(self):
        obj_representation = "{}, {}, {}, {}, {}, {}, {}".format(self.__ID, self.__first_name, self.__last_name, self.__city,  self.__base_pay,  self.__shift,  self.__hours)
        return obj_representation
