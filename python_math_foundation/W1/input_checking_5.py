#Homework 1.1

def input_5_checking ():
    user_input = int(input('Please enter your number: '))
    if user_input < 5:
        print('less than 5')
    else:
        print('higher than that')

input_5_checking()