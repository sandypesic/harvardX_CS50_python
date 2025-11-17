import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")
    
    file_name = sys.argv[1]

    if not file_name.endswith(".py"):
        sys.exit("Not a Python file.")

    try:
        with open(file_name) as file:
            LOC_counter = 0
            for line in file:
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                LOC_counter += 1
            print(LOC_counter)
    except FileNotFoundError:
        sys.exit("File does not exist.")


if __name__ == "__main__":
    main()