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

    #display employee name
    def show_person(self):
        print('Name:', self._getName())
        print('ID:', self.__ID)
        print('City:', self.__city)

# Проверка способа запуска модуля

if __name__ == '__main__':
    # Create an person
    john = Person(
        fname='John', lname='Paw', city="NYC", ID=223344
    )
    mary = Person(
        fname='Mary', lname='Sue', city='LA', ID=113344
    )

    print 'список всех  всех публичных атрибутов объекта Person: '

    print [arg for arg in dir(Person) if not arg.startswith('_')]
    print filter(lambda x: not x.startswith('_'), dir(Person))

    print 'список всех  всех публичных атрибутов объекта mary: '

    print [arg for arg in dir(mary) if not arg.startswith('_')]
    print 'список методов объекта'
    print [arg for arg in dir(Person) if callable(getattr(Person, arg))]
    print filter(lambda arg: callable(getattr(mary, arg)), dir(mary))
