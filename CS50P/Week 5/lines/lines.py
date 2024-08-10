import sys
import csv


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")
    else:
        input = sys.argv[1]



try:
    linecount = 0
    with open(input, "r") as file:
        for line in file:
            if not (line.lstrip().startswith("#") or line.strip() == ""):
                linecount += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(linecount)






