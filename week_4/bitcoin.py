import sys
import requests


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.exit("Missing command-line argument.")

    try:
        n = float(args[0])
    except ValueError:
        sys.exit("Command-line argument is not a number.")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=e43dbe7ee1a56e4d4a6ca963915aa5665d8ef8eeaf7058114e0a4115467ccf2a")
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except (requests.RequestException, KeyError, TypeError, ValueError):
        sys.exit("Error fetching Bitcoin price.")

    cost = price * n
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()