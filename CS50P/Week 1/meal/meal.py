def main():
    answer = input('What time is it? ')
    name =  convert(answer)
    if name >= 7 and name <= 8:
        print('breakfast time')
    elif name >= 12 and name <= 13:
        print('lunch time')
    elif name >= 18 and name <= 19:
        print('dinner time')

def convert(t):
    hours, minutes = t.split(':')
    minutes = float(minutes) / 60
    return float(hours) + minutes


if __name__ == "__main__":
    main()