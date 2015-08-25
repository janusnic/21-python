#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

import employee
from datetime import datetime, date, time

def print_menu():
    print('1. Список всех сотрудников')
    print('2. Добавить запись о сотруднике')
    print('3. Удалить запись')
    print('4. Просмотреть запись')
    print('5. Отредактировать запись')
    print('6. Заработная плата')
    print('7. Save')
    print('8. Load')
    print('9. Выход')
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

def edit_emp(mystaff):
        choice='Только 1,2,3,4!'
        e_name = raw_input("Имя сотрудника для редактирования: ")
        for emp in mystaff.employee_list:
            print emp.get_name()
            if emp.get_name() == e_name:
                while True:
                    result = raw_input(choice)
                    if result == '1':
                        emp.hours = int(input('\nПродолжительность рабочего дня '))
                        return True
                    elif result == '2':
                        emp.base_pay = input('Оплата за час: ')
                        return True
                    elif result == '3':
                        emp.shift = input('Рабочая смена 1,2, или 3: ')
                        return True
                    elif result == '4':
                        print "\nExit...\n"
                        return False
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

def search_emp(mystaff,e_name):
    for emp in mystaff.employee_list:
        if emp.get_name() == e_name:
            print 'Заработная плата сотрудника ',emp.get_name(), '=', emp.show_pay()
        else:
            print 'Сотрудник не найден'

def get_input():
    #input name

    first_name = raw_input("Имя сотрудника: ")
    #validate
    while first_name == '':
        print('\n Имя сотрудника required.  Try again.')
        first_name = raw_input("Имя сотрудника: ")

    last_name = raw_input("Фамилия сотрудника: ")
    #validate
    while last_name == '':
        print('\n Фамилия сотрудника required.  Try again.')
        last_name = raw_input("Фамилия сотрудника: ")

    ID_valid = False

    ID = raw_input("Идентификатор сотрудника: ")

    while ID_valid == False:
        try:
            ID = float(ID)
            if ID > 0:
                ID_valid = True
            else:
                print("\nID должен быть > 0.  Пробуем еще.")
                ID = input("Идентификатор сотрудника: ")
        except (ValueError, NameError):
            print("\nID должен быть числом.  Пробуем еще..")
            ID = input("Идентификатор сотрудника:: ")

    #get city
    city = raw_input("Место жительства: ")

    #return values
    return first_name, last_name, ID, city


def print_emp_details(e_name, mystaff):
    for emp in mystaff.employee_list:
        if emp.get_name() == e_name:
            print(emp)


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def save_to_db(filename,mystaff):
    out_file = open(filename, "wt")
    for emp in mystaff.employee_list:
        out_file.write(str(emp)+ "\n")
    out_file.close()

def load_from_db(filename,mystaff):
    lines = [line.rstrip('\n') for line in open(filename)]

    for line in lines:
        list = line.split(',')
        mystaff.add_employee(list[1],list[2], float(list[0]), list[3], int(list[4]), int(list[5]),int(list[6]))

def print_staff():
    try:
        n = 0
        for emp in mystaff.employee_list:
            n += 1
            print(emp)

        if n==0 :
            raise MyError(2)
    except MyError as e:
        print '\nНет данных о сотрудниках :', e.value
    else:
        print  'Хранилище содержит ', n, ' строк'
    finally:
        print  'Дата проверки состояния записей ', datetime.now()

if __name__ == '__main__':

    menu_choice = 0
    filename = 'staff.db'
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
            edit_emp(mystaff)
        elif menu_choice == '6':
            search_str = raw_input("Заработная плата сотрудника: ")
            search_emp(mystaff,search_str)
        elif menu_choice == '7':
            save_to_db(filename,mystaff)
        elif menu_choice == '8':
            load_from_db(filename,mystaff)
        elif menu_choice == '9':
            try:
                if  (answer("\nВы уверены, что хотите закончить работу? ('y' или 'n', Ctrl+C для выхода) ")==False):
                    break
            except (KeyboardInterrupt, EOFError):
                exit('\nВыход\n')

        else:
            print_menu()
