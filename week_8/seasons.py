from datetime import date
import sys
import inflect


def main():
    birthday = get_date()
    minutes = calc_minutes(birthday)
    words = convert(minutes)
    print(words)


def get_date():
    user_input = input("Date of Birth: ")
    try:
        year, month, day = map(int, user_input.split("-"))
        return date(year, month, day)
    except ValueError:
        sys.exit("Invalid date.")


def calc_minutes(birthday):
    delta = date.today() - birthday
    minutes = int(delta.days * 24 * 60)
    return minutes


def convert(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="")


if __name__ == "__main__":
    main()