## Grocery List

## Get item from user

## Add item to a variable dict

## Print list on ctrl + d in alphabetical order and quantity of items


list = {}

while True:
    try:
        item = input().lower()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1
    except(EOFError):
        for x in sorted(list.keys()):
            print(list[x], x.upper())
        break







