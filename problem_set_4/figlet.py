import pyfiglet
import sys
import random


def main():
    args = sys.argv[1:]
    text = input("Input: ")

    f = pyfiglet.Figlet()

    if len(args) == 0:
        font = random.choice(f.getFonts())
        f.setFont(font=font)
    elif len(args) == 2:
        if args[0] not in ["-f", "--font"]:
            sys.exit("Invalid first argument. Use -f or --font.")
        font = args[1]
        if font not in f.getFonts():
            sys.exit(f"Font '{font}' not found.")
        f.setFont(font=font)
    else:
        sys.exit("Wrong number of arguments. Use zero or two arguments.")

    print(f.renderText(text))


if __name__ == "__main__":
    main()