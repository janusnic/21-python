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
        self.name = ' '.join((self.__first_name, self.__last_name))

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
        self.__hours=kwargs['hours']
        self.cost = kwargs['cost']
        self.level = kwargs['level']

        super(self.__class__, self).__init__(*args, **kwargs)

    def sethours(self,hours):
        self.__hours=hours

    def gethours(self):
        return self.__hours

    hours=property(gethours,sethours)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Command(self, other)

    def __repr__(self):
        return '{u.name} (cost={u.cost}, level={u.level})'.format(u=self)

    def addProperty(self, attribute):
        # create local setter and getter with a particular attribute name
        getter = lambda self: self._getProperty(attribute)
        setter = lambda self, value: self._setProperty(attribute, value)

        # construct property attribute and add it to the class
        setattr(self.__class__, attribute, property(fget=getter, \
                                                    fset=setter, \
                                                    doc="Auto-generated method"))

    def _setProperty(self, attribute, value):
        print "Setting: %s = %s" %(attribute, value)
        setattr(self, '_' + attribute, value.title())

    def _getProperty(self, attribute):
        print "Getting: %s" %attribute
        return getattr(self, '_' + attribute)


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
            print('My salary is ', self.__base_pay*self.__hours)
        elif self.__shift == 2:
            print('My salary is ', ((self.__base_pay * SHIFT_2) + self.__base_pay)*self.__hours)
        elif self.__shift == 3:
            print('My salary is ', ((self.__base_pay * SHIFT_3) + self.__base_pay)*self.__hours)

class Command(object):
    def __init__(self, *employees):
        self.employees = employees
        self.cost = sum(employee.cost for employee in employees)
        self.level = max(employee.cost for employee in employees)

    def __add__(self, other):
        if isinstance(other, Employee):
            return Command(other, *self.employees)

    def __str__(self):
        return 'Command (cost={b.cost}, level={b.level}) {b.employees}'.format(b=self)


# Проверка способа запуска модуля

if __name__ == '__main__':
    # Create an employee with a boss
    boss_john = Employer(fname='John', lname='Paw', city="NYC", ID=223344, company_name="Packrat's Cats")

    boss_john .show_person()
    employee_mary = Employee( fname='Mary', lname='Sue', city="NYC", ID=113344, hours=0, base_pay=10000, shift=2,cost=15, level=2)
    employee_mary.base_pay = 15000
    employee_mary.hours = 40
    employee_mary.addProperty('phone')
    employee_mary.phone = '123 456 777'

    print employee_mary.name

    print employee_mary


    #__dict__ : Dictionary containing the class's namespace
    print "employee_mary.__dict__:", employee_mary.__dict__
