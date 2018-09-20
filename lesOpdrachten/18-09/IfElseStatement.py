userName = input('Enter your name: ')
userAge = eval(input('Enter your age: '))

if userAge >= 18:
    print("{}, you can {} vote".format(userName, userAge))
else:
    print("{}, you can't vote".format(userName))
