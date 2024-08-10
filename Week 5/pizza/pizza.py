import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a csv file")
        else:
            print(try_csv(sys.argv[1]))




def try_csv(input):
    try:
        with open(input, "r") as file:
            reader = csv.reader(file)
            return tabulate(reader, headers="firstrow", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")







if __name__ == "__main__":
    main()

