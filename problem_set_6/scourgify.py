import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    
    before_file = sys.argv[1]
    after_file = sys.argv[2]

    try:
        with open(before_file) as before:
            reader = csv.DictReader(before)
            students = []

            for row in reader:
                last, first = row["name"].split(", ")
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

        with open(after_file, "w", newline="") as after:
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)
         
    except FileNotFoundError:
        sys.exit("File does not exist.")


if __name__ == "__main__":
    main()