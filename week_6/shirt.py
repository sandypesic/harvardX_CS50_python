import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    valid_extensions = (".jpg", ".jpeg", ".png")

    if not input_file.lower().endswith(valid_extensions):
        sys.exit("Invalid input.")
    if not output_file.lower().endswith(valid_extensions):
        sys.exit("Invalid input.")
    if input_file.lower().split(".")[-1] != output_file.lower().split(".")[-1]:
        sys.exit("Input and output have different extensions.")

    try:
        shirt = Image.open("shirt.png")
        input_img = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("File does not exist.")

    input_cropped = ImageOps.fit(input_img, shirt.size)
    input_cropped.paste(shirt, shirt)
    input_cropped.save(output_file)


if __name__ == "__main__":
    main()