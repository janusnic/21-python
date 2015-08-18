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

    def __format__(self, format_spec):
        if isinstance(format_spec, unicode):
            return unicode(str(self))
        else:
            return str(self)

    #display name
    def show_person(self):
        print 'Name', format(self._getName(),'<9')
        print 'ID:', format(self.__ID,'<9')
        print('City:', self.__city)


class Employer(Person):
    """ An employer is a person who runs a company.

    """
    # The name of the company
    def __init__(self,fname, lname, ID, city, company_name):
        super(Employer, self).__init__(fname, lname, ID, city)
        self.company_name = company_name

    def show_person(self):
        Person.show_person(self)
        print('Company Name:',self.company_name)


# Проверка способа запуска модуля

if __name__ == '__main__':
    # Create an employee with a boss
    boss_john = Employer(
        fname='John', lname='Paw', city="NYC", ID=223344, company_name="Packrat's Cats"
    )

    boss_john .show_person()
    #__name__: Class name
    print "Employer.__name__:", Employer.__name__

    #__dict__ : Dictionary containing the class's namespace
    print "boss_john.__dict__:", boss_john.__dict__
