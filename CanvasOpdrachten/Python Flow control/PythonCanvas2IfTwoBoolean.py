#Opdracht 2 'and' in if statement

#Declareren user variables
age = eval(input('Enter your age: '))
passport = input('Do you have a dutch nationality? yes/no: ')

#If statement
if age >= 18 and 'yes' in passport:
    #print succes message
    print('Congrats! You\'re eglible of voting!')
