user_input = input("Input: ")
output = ""

for char in user_input:
    if char.lower() not in ["a", "e", "i", "o", "u"]:
       output += char

print(output)