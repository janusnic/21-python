# -*- coding: utf-8 -*-
#set global constant
SHIFT_2 = 0.05
SHIFT_3 = 0.10

class Person(object):
    """ A simple class representing a person object.

    """

    def __init__(self, *args, **kwargs):
        self.__ID = kwargs['ID']
        self.__first_name  = kwargs['fname']
        self.__last_name  = kwargs['lname']
        self.__city = kwargs['city']

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
    def __init__(self,*args, **kwargs):
        self.company_name = kwargs.pop('company_name')
        super(self.__class__, self).__init__(*args, **kwargs)

    def show_person(self):
        super(self.__class__, self).show_person()
        print('Company Name:',self.company_name)


class Employee(Person):
    """ An employee is person with a boss and a phone number.

    """
    # initialize method calls superclass
    def __init__(self,*args, **kwargs):
        self.__base_pay = kwargs['base_pay']
        self.__shift = kwargs['shift']
        super(self.__class__, self).__init__(*args, **kwargs)

    #show_pay overrides the superclass and displays hourly pay rates
    def show_pay(self):
        if self.__shift == 1:
            print('My salary is ', self.__base_pay)
        elif self.__shift == 2:
            print('My salary is ', (self.__base_pay * SHIFT_2) + self.__base_pay)
        elif self.__shift == 3:
            print('My salary is ', (self.__base_pay * SHIFT_3) + self.__base_pay)

# Проверка способа запуска модуля

if __name__ == '__main__':
    # Create an employee with a boss
    boss_john = Employer(fname='John', lname='Paw', city="NYC", ID=223344, company_name="Packrat's Cats")

    boss_john .show_person()
    employee_mary = Employee( fname='Mary', lname='Sue', city="NYC", ID=113344, base_pay=10000, shift=2)
    employee_mary.show_pay()

    #__dict__ : Dictionary containing the class's namespace
    print "employee_mary.__dict__:", employee_mary.__dict__
