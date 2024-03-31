#!/usr/bin/python3

import sys


def view_student(filename):
    try:
        with open(filename,'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError: 
        print('File does\'t exist')


def add_student(filename,add):
    try:
        with open(filename,'a',encoding='utf-8') as f:
            f.write(add + '\n')
            print(f"successfully added {add}")
    except FileNotFoundError:
        print('Class File Not found')


def delete_student(filename,delete):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            lines = f.readlines()
            empty_line = []

            for line in lines:
                if line.strip() != delete:
                    empty_line.append(line)

                else:
                    print(f'Sussfully deleted {line}')
                    del line

        with open(filename,'w',encoding='utf-8') as f:
            f.writelines(empty_line)   
            

    except FileNotFoundError:
        return




filename = 'class.txt'
arg = sys.argv

try:
    if int(arg[1]) == 1:
        view_student(filename)

    elif int(arg[1]) == 2:
        add = input('What do you want to add? ')
        add_student(filename,add)

    elif int(arg[1]) == 3:
        delete = input('Who do you want to delete? ')
        delete_student(filename,delete)

except :
    print('\n')
    print('''
                    Available Option
    1. view Student
    2. Add student
    3. Delete student
          
''')
    print('hint: python pld.py 3')
