# -*- coding: utf-8 -*-

class Person(object):
    """ A simple class representing a person object.

    """
    #initialize name, ID number, city
    def __init__(self, fname, lname, ID, city):
        self.__ID = ID
        self.__first_name  = fname
        self.__last_name  = lname
        self.__city = city

    def _getName(self):
        s = ' '
        return s.join((self.__first_name, self.__last_name))

    #display person name
    def show_person(self):
        print('Name:', self._getName())
        print('ID:', self.__ID)
        print('City:', self.__city)

john = Person('John', 'Sidorov', 123456, 'NYC')
john.show_person()

print john._getName()

print john._Person__city
