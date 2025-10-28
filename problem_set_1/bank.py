user_input = input("Greeting: ").strip().lower()
if user_input[:5] == "hello":
    print("$0")
elif user_input[:1] == "h":
    print("$20")
else:
    print("$100")
