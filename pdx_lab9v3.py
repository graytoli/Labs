# Lab 9: Unit Converter, version 3
print("Convert feet, miles, meters, kilometers, yards, or inches to meters.")

user_input = input("Enter the distance and units to be converted: ").strip().split()

number = float(user_input[0])

units = user_input[1]

if units in ['ft', 'feet', 'foot']:
    convert = number * 0.3048
elif units in ['mi', 'miles', 'mile']:
    convert = number * 1609.34
elif units in ['m', 'meters', 'meter']:
    convert = number * 1
elif units in ['km', 'kilometers', 'kilometer']:
    convert = number * 1000
elif units in ['yd', 'yards', 'yard']:
    convert = number * 0.9144
elif units in ['in', 'inches', 'inch']:
    convert = number * 0.0254
else:
    convert = "Input invalid."

if convert == "Input invalid.":
    print(convert)
else:
    print(f"{' '.join(user_input)} is {round(convert, 4)} meters.")
