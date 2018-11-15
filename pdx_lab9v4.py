# Lab 9: Unit Converter, version 4
print("Welcome to the Conversion Calculator!")

def first_step(units, number):
    if units in ['ft', 'feet', 'foot']:
        first_step = number * 0.3048
    elif units in ['mi', 'miles', 'mile']:
        first_step = number * 1609.34
    elif units in ['m', 'meters', 'meter']:
        first_step = number * 1
    elif units in ['km', 'kilometers', 'kilometer']:
        first_step = number * 1000
    elif units in ['yd', 'yards', 'yard']:
        first_step = number * 0.9144
    elif units in ['in', 'inches', 'inch']:
        first_step = number * 0.0254
    return first_step

def second_step(first_step):
    if desired_units in ['ft', 'feet', 'foot']:
        converted = first_step / 0.3048
    elif desired_units in ['mi', 'miles', 'mile']:
        converted = first_step / 1609.34
    elif desired_units in ['m', 'meters', 'meter']:
        converted = first_step / 1
    elif desired_units in ['km', 'kilometers', 'kilometer']:
        converted = first_step / 1000
    elif desired_units in ['yd', 'yards', 'yard']:
        converted = first_step / 0.9144
    elif desired_units in ['in', 'inches', 'inch']:
        converted = first_step / 0.0254
    return converted

while True:
    original_units = input("Enter the distance and units to be converted: ").strip().split()
    orig_num = float(original_units[0])
    orig_units = original_units[1]

    desired_units = input("Enter the units you want to convert to: ").strip()

    possible_units = ['ft', 'feet', 'foot', 'mi', 'miles', 'mile', 'm', 'meters', 'meter', 'km', 'kilometers', 'kilometer', 'yd', 'yards', 'yard', 'in', 'inches', 'inch']

    if orig_units and desired_units in possible_units:
        first = first_step(orig_units, orig_num)
        second = second_step(first)
        print(f"{' '.join(original_units)} is {round(second, 4)} {desired_units}.")
        break
    else:
        print('Invalid entry. Try again to convert between ft, mi, m, km, yd, and in.')
