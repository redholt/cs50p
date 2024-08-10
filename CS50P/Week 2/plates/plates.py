def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

## Check if is_valid using other functions

def is_valid(s):
    if first(s) and length(s) and endnum(s) and punc(s):
        return True
    else:
        return False

## Check first 2 letters are not numbers

def first(s):
     if s[0:2].isalpha():
         return True
     else:
         return False

## Check string between 2 and 6 characters

def length(s):
    if len(s) >=2 and len(s) <=6:
        return True
    else:
        return False

## Check numbers are at the end of the plate

def endnum(s):
    num = True
    for i in s:
        if i == '0' and num == True:
            return False
        if i.isdigit():
            num = False
        if i.isalpha() and num == False:
            return False
    else:
        return True

## Check no periods, spaces or punctuation marks are in str

def punc(s):
    if s.isalnum():
        return True
    else:
        return False

main()