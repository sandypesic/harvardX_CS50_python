def convert(user_input):
    output = user_input.replace(':)', '🙂').replace(':(', '🙁')
    return output

def main():
    user_input = input("Write something! ")
    print(convert(user_input))

main()