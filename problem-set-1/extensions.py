user_input = input("File name: ").strip().lower()
if user_input[-4:] == ".gif" or user_input[-4:] == ".png":
    print("image/" + user_input[-3:])
elif user_input[-4:] == ".jpg" or user_input[-5:] == ".jpeg":
    print("image/jpeg")
elif user_input[-4:] == ".pdf" or user_input[-4:] == ".zip":
    print("application/" + user_input[-3:])
elif user_input[-4:] == ".txt":
    print("text/" + user_input[-3:])
else:
    print("application/octet-stream")