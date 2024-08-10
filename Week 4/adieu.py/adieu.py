import inflect
import sys

p = inflect.engine()

names = []

while True:
    try:
        name = input('Name: ')
        names.append(name)

    except(EOFError):
        print()
        names = p.join((names))
        print(f'Adieu, adieu, to {names}')
        break