def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    result = (int(hours)) + int(minutes) / 60
    match result:
        case _ if 7 <= result <= 8:
            print("Breakfast time!")
        case _ if 12 <= result <= 13:
            print("Lunch time!")
        case _ if 18 <= result <= 19:
            print("Dinner time!")

main()