import sys

'''
A python code that add list of student in Back-end Gurus to a file using command line.
'''

todo_list = []


try:
    if int(sys.argv[1]) == 1:
        try:
            print('You can only add one item at a time.')
            add = input('What do you wish to Add? ')
            todo_list.append(add)
            with open('student.txt','a',encoding = 'UTF-8') as f:
                for do in todo_list:
                    f.write(f'{do} ')
            print(f'You have successfully added {add} to the file')
        except:
            print(f'Sorry Unable to add {add} to the file')

    
    elif int(sys.argv[1]) == 2:
        try:
            with open('student.txt','r',encoding = 'UTF-8') as f:
                read = f.read()
                print(read)
        except:
            print(f'Sorry Unable to read Empty file')


    elif int(sys.argv[1]) == 3:
        try:
            delete = input('Who do you want to delete? ')
            with open('student.txt','r', encoding='UTF-8') as f:
                lines = []
            for line in f:
                if delete not in line:
                    lines.append(line)

# Write the modified contents back to the file
            with open('student.txt', 'w', encoding='UTF-8') as f:
                for line in lines:
                    f.write(line)
        except:
            print(f'Sorry! somthing happened')
        
        

except:
    print('''
          Menu Option:

    1. Add Task
    2. View Task
    3. Delete Task
    4. Exit  

                
            ''')
    print('Hint: python to_do_list.py <number from option>')