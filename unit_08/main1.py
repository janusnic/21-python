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

class Staff(object):

    def __init__(self):
        self.employee_list = []

    def add_employee(self, first_name, last_name, ID, city, base_pay, shift, hours):
        new_emp = employee.Employee(first_name, last_name, ID, city, base_pay, shift, hours)
        self.employee_list.append(new_emp)

def make_list(mystaff):
    pass

def search_emp(s):
    pass

def get_input():
    pass

def print_emp_details(e_name, mystaff):
    pass

def print_staff():
    pass

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
            break
        else:
            print_menu()
