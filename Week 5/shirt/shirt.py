import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        inp = os.path.splitext(sys.argv[1])
        out = os.path.splitext(sys.argv[2])
        types = [".jpg", ".png", ".jpeg"]
        if out[1].lower() not in types:
            sys.exit("Invalid output")
        elif inp[1].lower() != out[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            image_convert(sys.argv[1], sys.argv[2])

def image_convert(x, y):
    try:
        shirt = Image.open("shirt.png")
        picture = Image.open(x)
        size = shirt.size
        new = ImageOps.fit(picture, size)
        new.paste(shirt, mask=shirt)
        new.save(y)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
