# Lab 8: Make Change, version 1
amount = int(input("Enter the value in pennies: "))

quarters = amount // 25

dimes = (amount - (quarters * 25)) // 10

nickels = (amount - (quarters * 25) - (dimes * 10)) // 5

pennies = (amount - (quarters * 25) - (dimes * 10) - (nickels * 5))

print(f"You have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")
