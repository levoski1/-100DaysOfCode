#!/usr/bin/python3

import sys

'''
add
view
delete
'''

def add_student(filename):
    try:
        with open(filename,'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except Exception as e: 
        print(f'{e}: File does\'t exist')

'''
def view(filename):
    try:
        with open(filename):
'''
add_student('text.txt')
