user_input = input("File name: ").strip().lower()

match user_input:
    case _ if user_input.endswith(".gif"):
        print("image/gif")
    case _ if user_input.endswith(".png"):
        print("image/png")
    case _ if user_input.endswith(".jpg") | user_input.endswith(".jpeg"):
        print("image/jpeg")
    case _ if user_input.endswith(".pdf"):
        print("application/pdf")
    case _ if user_input.endswith(".zip"):
        print("application/zip")
    case _ if user_input.endswith(".txt"):
        print("text/plain")
    case _:
        print("application/octet-stream")