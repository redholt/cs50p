import sys
import requests
import json

def main():
    try:
        if len(sys.argv) == 1:
            sys.exit('Missing command-line argument')
        else:
            x = float(sys.argv[1])
            y = get_price()
            calc = x * y
            print(f'${calc:,.4f}')
    except ValueError:
        sys.exit('Command-line argument is not a number')


def get_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    out = response.json()
    return(out['bpi']['USD']['rate_float'])



main()