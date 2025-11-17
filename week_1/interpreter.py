user_input = input("Expression: ")

x_string, y_string, z_string = user_input.split()

x = int(x_string)
z = int(z_string)

if y_string == "+":
    result = x + z
elif y_string == "-":
    result = x - z
elif y_string == "*":
    result = x * z
elif y_string == "/":
    result = x / z

print(f"{result:.1f}")