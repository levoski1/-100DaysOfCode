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
        print('File Not found')

        
def edit_student(filename, remove, replace):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            modified_lines = []

            for line in lines:
                if line.strip() == remove:
                    modified_lines.append(replace + '\n')  # Append the replacement content in a new line
                    print(f'Successfully Edited {remove} to {replace}')
                else:
                    modified_lines.append(line)

        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

            

    except FileNotFoundError:
        print(f'Sorry! File doesn\'t exist')

def delete_student(filename,delete):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            lines = f.readlines()
            empty_line = []

            for line in lines:
                if line.strip() != delete:
                    empty_line.append(line)
                    

                else:
                    print(f'Sussfully deleted {LSline}')
                    del line
                

        with open(filename,'w',encoding='utf-8') as f:
            f.writelines(empty_line)   
            

    except FileNotFoundError:
        print('Sorry! File doesn\'t exist')





filename = 'ext.txt'
arg = sys.argv

try:
    if int(arg[1]) == 1:
        view_student(filename)

    elif int(arg[1]) == 2:
        add = input('What do you want to add? ')
        add_student(filename,add)
        
    elif int(arg[1]) == 3:
        modify = input('Who do you want to modifiy? ')
        replace = input('Who do you want to replace? ')

        edit_student(filename,modify,replace)

    
    elif int(arg[1]) == 4:
        delete = input('Who do you want to delete? ')
        delete_student(filename,delete)

except:
    print("\n")
    print('''
                    Available Option
    1. view Student
    2. Add student
    3. Edit Student
    4. Delete student
          
''')
    print("hint: python file_name 3")

