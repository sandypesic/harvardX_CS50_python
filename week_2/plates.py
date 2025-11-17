def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0':
                return False
            if not s[i:].isdigit():
                return False
            break
    if not s.isalnum():
        return False
    return True


if __name__ == "__main__":
    main()