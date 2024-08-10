def main():
    words = input('Enter your text: ')
    convert(words)

def convert(val):
    return print(val.replace(':)', '🙂').replace(':(', '🙁'))

main()