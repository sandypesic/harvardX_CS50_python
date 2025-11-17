import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})){3}$"
    if re.match (pattern, ip):
        return True
    return False


if __name__ == "__main__":
    main()