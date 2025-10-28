def main():
    names = []

    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    n = len(names)
    if n == 1:
        adieu_str = names[0]
    elif n == 2:
        adieu_str = f"{names[0]} and {names[1]}"
    else:
        adieu_str = ", ".join(names[:-1]) + f", and {names[-1]}"

    print(f"Adieu, adieu, to {adieu_str}")


if __name__ == "__main__":
    main()