import random


while True:
    try:
        level = input('Level: ')
        level = int(level)
        if level <=0:
            pass
        else:
            break
    except (NameError, ValueError):
        pass

number = random.randint(1,level)

while True:

    try:
        guess = input('Guess: ')
        guess = int(guess)

        if guess < 0:
            pass
        elif guess < number:
            print('Too small!')
            pass
        elif guess > number:
            print('Too large!')
            pass
        else:
            print('Just right!')
            break

    except (NameError, ValueError):
        pass


