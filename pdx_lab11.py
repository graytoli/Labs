# Lab 11: Simple Calculator, version 1
operator = input('What operation would you like to perform? ').strip()
operand1 = float(input('What is the first number? ').strip())
operand2 = float(input('What is the second number? ').strip())


if operator == '+':
    solution = operand1 + operand2
elif operator == '-':
    solution = operand1 - operand2
elif operator in ['*', 'x']:
    solution = operand1 * operand2
elif operator == '/':
    solution = operand1 / operand2
else:
    solution = 'Invalid entry.'

if solution == 'Invalid entry.':
    print(solution)
else:
    print(f'{operand1} {operator} {operand2} = {solution}')
