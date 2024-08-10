def main():
    v = input('Please enter your simple equation ')
    return calc(v)

def calc(n):
    x, y, z = n.split(' ')
    if str(y) == '+':
        print(float(x) + float(z))
    elif str(y)  == '-':
         print(float(x) - float(z))
    elif str(y)  == '/' and float(z) == 0:
        z = 1
        print(float(x) / float(z))
    elif str(y)  == '/':
        print(float(x) / float(z))
    elif str(y) == '*':
        print(float(x) * float(z))



main()