import random

# rand = random.randint(0,9)
rand = 4

print('Guess the number!')

print('In this game you will have to guess the number between 0 and 9 within 5 attemps')
print()
print('You will be told if the number you have guessed is close or far in relation to the number which is chosen')

numberArr = [1,2,3,4,5,6,7,8,9,0]
positionArr = ['first','second','third','fourth','last']

attempts = 0

    # guess 1
while attempts < 5:


    g1 = int(input('Choose your ' + positionArr[attempts] +' number:'))

    if g1 == rand and g1 in numberArr:
        print('You guessed the number')
        exit()
    elif g1 in numberArr:
        if g1 in numberArr[rand - 2:rand + 2]:
            print('Your guess was close')
        elif g1 in numberArr[rand - 4: rand + 3]:
            print('Your guess was not close but not too far')
        else:
            print('Your guess was far')
    else:
        print('Not a valid number')
            
    attempts += 1

if attempts == 5:
    randCheck = input('Do you want to see the number chosen? :')
    if randCheck == 'Yes' or randCheck == 'yes':
        print('The number was\n',rand)
    else:
        exit()
else:
    print('yo')