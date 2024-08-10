import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
            sys.exit("Not a csv file")
        else:
            try_files(sys.argv[1], sys.argv[2])



def try_files(x, y):
    try:
        with open(x) as input:
            reader = csv.DictReader(input)
            with open(y, "w") as output:
                amended = csv.DictWriter(output, fieldnames = ["first", "last", "house"])
                amended.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    amended.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()

