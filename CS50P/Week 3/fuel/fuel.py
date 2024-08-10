## Get user to input a fraction and return a % rounded to whole number.
## If below 1% return E, if above 99% return F
## Handle errors to continue prompting the user for a correct fraction


def main():
    x = get_frac()
    if x >= 0 and x <= 0.01:
        print('E')
    elif x >= .99 and x <= 1:
        print('F')
    else:
        print(round(x * 100),'%', sep='')


def get_frac():
    while True:
        z = input('Fraction: ')
        try:
            x,y = z.split('/')
            x = int(x)
            y = int(y)
            c = x / y
            if c <= 1:
                return c
        except (ValueError, ZeroDivisionError):
            pass





main()
