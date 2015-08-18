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


    print 'список всех атрибутов Person: ', dir(Person)

    print 'список всех атрибутов объекта: ', dir(mary)

    #__doc__ : Class documentation string or None if undefined.
    print "Person.__doc__:", Person.__doc__

    #__name__: Class name
    print "Person.__name__:", Person.__name__

    #__module__: Module name in which the class is defined. This attribute is "__main__" in interactive mode.
    print "Person.__module__:", Person.__module__

    #__bases__ : A possibly empty tuple containing the base classes, in the order
    #of their occurrence in the base class list.
    print "Person.__bases__:", Person.__bases__

    #__dict__ : Dictionary containing the class's namespace
    print "Person.__dict__:", Person.__dict__

    print '+++++Mary has+++++'
    print "mary.__doc__:", mary.__doc__

    print "mary.__module__:", mary.__module__
    print "mary.__dict__:", mary.__dict__

    # print "mary.__name__:", mary.__name__
    # print "mary.__bases__:", mary.__bases__
