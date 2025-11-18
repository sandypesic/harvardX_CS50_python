import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    m1 = m1 or "00"
    m2 = m2 or "00"

    h1, m1 = int(h1), int(m1)
    h2, m2 = int(h2), int(m2)

    if not (1 <= h1 <= 12 and 0 <= m1 <= 59):
        raise ValueError("Invalid start time.")
    if not (1 <= h2 <= 12 and 0 <= m2 <= 59):
        raise ValueError("Invalid end time.")

    if p1 == "AM":
        h1_24 = 0 if h1 == 12 else h1
    else:
        h1_24 = 12 if h1 == 12 else h1 + 12

    if p2 == "AM":
        h2_24 = 0 if h2 == 12 else h2
    else:
        h2_24 = 12 if h2 == 12 else h2 + 12

    return f"{h1_24:02}:{m1:02} to {h2_24:02}:{m2:02}"


if __name__ == "__main__":
    main()