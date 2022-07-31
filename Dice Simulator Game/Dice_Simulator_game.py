import random
while True:
    print(' ')
    print('1.Roll The Dice \t\t 2.Exit')
    user = int(input('What you want to do?\n'))
    if user == 1:
        number = random.randint(1,6)
        print(' ')
        print(number)
    else:
        break