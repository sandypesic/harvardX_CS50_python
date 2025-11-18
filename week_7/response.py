from validator_collection import validators, errors


def main():
    print(validate(input("What's your email address? ")))


def validate(email):
    try:
        validators.email(email)
        return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"
    except Exception:
        return "Invalid"


if __name__ == "__main__":
    main()
