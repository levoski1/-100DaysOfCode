#!/usr/bin/python3



#DAY 1



from random import randint




def Random_num():
    ''' This function return a random number starting from 10 - 20
    '''
    return randint(1,10)

def Get():
    '''
    function that get input from user
    '''
    user = input("Guess a number: ")
    return user


random_num = Random_num()
print("Guess a secret number. You have 4 trials")
try:
    a = 0
    while (a < 4):
        print("ENTER A VALUE FROM 1 - 10  \n")
        get_num = int(Get())
        if get_num < random_num:
            print("""incorrect!!!
                  hint: Go higher
                  """)
        elif get_num > random_num:
            print("""incorrect!!!
                  hint: Go lower
                  """)
        else:
            print(f"Congratulation: Your value {get_num} is correct")
            break
        a += 1
except:
    print(f"Error: Please choose valid number")
