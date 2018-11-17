# Lab 20: Credit Card Validation, version 2
def validate(credit_card):
    num_list = list(credit_card)
    int_list = []
    for i in range(len(num_list)):
        int_list.append(int(num_list[i]))
    check_digit = int_list.pop()
    int_list.reverse()
    for i in range(0, len(int_list), 2):
        int_list[i] *= 2
    for i in range(len(int_list)):
        if int_list[i] > 9:
            int_list[i] -= 9
    sum_digits = list(str(sum(int_list)))
    sum_list = []
    for i in range(len(sum_digits)):
        sum_list.append(int(sum_digits[i]))
    if sum_list[1] == check_digit:
        print('Valid!')
    else:
        print('Invalid.')

validate(input('Enter your credit card number: ').replace(' ', ''))
