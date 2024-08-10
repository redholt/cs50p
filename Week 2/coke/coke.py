def main():
    cost = 50
    while cost > 0:
        cost = cost - cash()
        if cost > 0:
            print('Amount Due:',cost)
        else:
            print('Change Owed:',abs(cost))


# Function to check coin is accepted, convert to 0 if not

def cash():
    n = int(input('Input Coin:'))
    if n in [25,10,5]:
        return n
    else:
        return 0


main()




