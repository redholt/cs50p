import random

def main():
    x = get_level()
    count = 0
    score = 0
    tries = 0
    while count < 10:
        count += 1
        a = generate_integer(x)
        b = generate_integer(x)
        c = a + b
        while True:
            d = input(f'{a} + {b} = ')
            try:
                d = int(d)
                if d != c:
                    raise ValueError
                else:
                    score += 1
                    break

            except ValueError:
                print('EEE')
                tries += 1
                if tries == 3:
                    print(f'{a} + {b} = {c}')
                    tries = 0
                    break
                else:
                    pass


    print(f'Score: {score}')


def get_level():
    while True:
        x = input('Level: ')
        try:
            x = int(x)
            if x in [1,2,3]:
                return x
            else:
                pass
        except(ValueError,KeyError):
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)




if __name__ == '__main__':
    main()