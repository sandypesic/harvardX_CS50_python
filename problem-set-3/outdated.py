def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    month_to_num = {month: f"{i:02}" for i, month in enumerate(months, start = 1)}

    while True:
        date_input = input("Date: ").strip()

        try:
            if "/" in date_input:
                month, day, year = date_input.split("/")
                month = f"{int(month):02}"
                day = f"{int(day):02}"
                year = str(int(year))
                print(f"{year}-{month}-{day}")
                break

            else:
                parts = date_input.split(" ")
                if len(parts) != 3:
                    raise ValueError

                month_name = parts[0]
                day = parts[1].replace(",", "")
                year = parts[2]

                if month_name not in month_to_num:
                    raise ValueError

                month = month_to_num[month_name]
                day = f"{int(day):02}"
                year = str(int(year))
                print(f"{year}-{month}-{day}")
                break

        except (ValueError, IndexError):
            continue


main()
