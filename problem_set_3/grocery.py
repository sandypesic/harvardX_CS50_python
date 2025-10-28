from collections import Counter


def main():
    grocery_list = []

    try:
        while True:
            item = input().upper()
            grocery_list.append(item)
    except EOFError:
        pass

    counts = Counter(grocery_list)
    for item in sorted(counts):
        print(f"{counts[item]} {item}")


main()