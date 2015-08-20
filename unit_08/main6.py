#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

import employee

def print_menu():
    print('1. Список всех сотрудников')
    print('2. Добавить запись о сотруднике')
    print('3. Удалить запись')
    print('4. Просмотреть запись')
    print('5. Отредактировать запись')
    print('6. Поиск записей')
    print('7. Выход')
    print

'''функция диалога.
Первым аргументом принимаем ответ пользователя,
вторым - выдаём сообщение при неверном вводе'''
def answer(prompt, choice='Только Yes или no!'):
        while True:
                result = raw_input(prompt)
                if result in ('y', 'Y', 'yes', 'Yes'):
                        print '\nВы выбрали "YES" - заканчиваем\n'
                        '''тут можно использовать оператор break вместо return
                        так же и в ответе No'''
                        return False

                elif result in ('n', 'N', 'no', 'No'):
                        print "\nВы выбрали NO - Я продолжаю работу...\n"

                        print_menu()
                        return True
                else:

                        print(choice)

class Staff(object):

    def __init__(self):
        self.employee_list = []

    def add_employee(self, first_name, last_name, ID, city, base_pay, shift, hours):
        new_emp = employee.Employee(first_name, last_name, ID, city, base_pay, shift, hours)
        self.employee_list.append(new_emp)

def make_list(mystaff):

    #get number of hourly employees
    hours = int(input('\nПродолжительность рабочего дня '))

    #get input
    first_name, last_name, ID, city = get_input()

    base_pay = input('Оплата за час: ')

    shift = input('Рабочая смена 1,2, или 3: ')
    #create object
    mystaff.add_employee(first_name, last_name, ID, city, base_pay, shift, hours)

def search_emp(s):
    pass

def get_input():
    #input name

    first_name = input("Имя сотрудника: ")
    #validate
    while first_name == '':
        print('\n Имя сотрудника required.  Try again.')
        first_name = input("Имя сотрудника: ")
    last_name = input("Фамилия сотрудника: ")
    #validate
    while last_name == '':
        print('\n Фамилия сотрудника required.  Try again.')
        last_name = input("Фамилия сотрудника: ")

    ID_valid = False

    ID = input("Идентификатор сотрудника: ")

    while ID_valid == False:
        try:
            ID = float(ID)
            if ID > 0:
                ID_valid = True
            else:
                print("\nID должен быть > 0.  Пробуем еще.")
                ID = input("Идентификатор сотрудника: ")
        except ValueError, NameError:
            print("\nID должен быть числом.  Пробуем еще..")
            ID = input("Идентификатор сотрудника:: ")

    #get city
    city = input("Место жительства: ")

    #return values
    return first_name, last_name, ID, city


def print_emp_details(e_name, mystaff):
    for emp in mystaff.employee_list:
        if emp.get_name() == e_name:
            print(emp)

def print_staff():
    for emp in mystaff.employee_list:
        print(emp)

if __name__ == '__main__':

    menu_choice = 0
    print_menu()
    mystaff = Staff()

    while True:
        menu_choice = raw_input("Выберите пункт меню (1-7): ")
        if menu_choice == '1':
            print_staff()
        elif menu_choice == '2':
            make_list(mystaff)
        elif menu_choice == '3':
            print("Удалить запись")
            name = input("Имя сотрудника: ")
            remove_number(name)
        elif menu_choice == '4':
            print("Просмотреть запись")
            e_name = input("Имя сотрудника: ")
            print_emp_details(e_name, mystaff)
        elif menu_choice == '5':
            filename = input("Запись для редактирования: ")
            edit_emp(filename)
        elif menu_choice == '6':
            search_str = input("Критерий поиска: ")
            search_emp(search_str)
        elif menu_choice == '7':
            try:
                if  (answer("\nВы уверены, что хотите закончить работу? ('y' или 'n', Ctrl+C для выхода) ")==False):
                    break
            except (KeyboardInterrupt, EOFError):
                exit('\nВыход\n')

        else:
            print_menu()
