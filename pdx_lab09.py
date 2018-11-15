# Lab 9: Unit Converter, version 1
user_input = float(input("Enter the distance in feet: "))

meters = round(user_input * 0.3048, 4)

print(f"{user_input} feet is {meters} meters.")
