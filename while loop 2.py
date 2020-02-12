import random
a=random.randint(1,10)
while True:
    b=input('guess a number from 1-10:')
    if int(b) == a:
        print('correct')
        break  