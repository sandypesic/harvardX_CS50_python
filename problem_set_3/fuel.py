def main():
    fraction = get_frac("Fraction: ")
    percentage = round(fraction * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_frac(prompt):
    while True:
        try:
            frac = input(prompt)
            x, y = frac.split('/')
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            return x / y

        except (ValueError, ZeroDivisionError):
            pass


main()
