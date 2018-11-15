# Lab 11: Simple Calculator, version 2
def operation(operator, operand1, operand2):
    operand1 = float(operand1)
    operand2 = float(operand2)
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
    return solution

def result(solution):
    if solution == 'Invalid entry.':
        print(solution)
    else:
        print(f'{operand1} {operator} {operand2} = {solution}')

while True:
    operator = input('What operation would you like to perform? \nOr type \'done\' to exit.\n').strip()
    if operator == 'done':
        break
    operand1 = input('What is the first number?\n').strip()
    operand2 = input('What is the second number?\n').strip()
    result(operation(operator, operand1, operand2))
