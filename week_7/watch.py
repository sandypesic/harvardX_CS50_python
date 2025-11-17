import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    if matches := re.search(pattern, s):
        return f"https://youtu.be/{matches.group(1)}"
    return None


if __name__ == "__main__":
    main()
