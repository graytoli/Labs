# Lab 15: Number to Phrase, version 2
ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens =  {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

def int_to_english(num_int):
    num_int = int(num_int)
    if num_int < 0 or num_int > 999:
        print('Invalid entry.')
    elif num_int == 0:
        print('zero')
    elif 9 < num_int < 20:
        teens_eng = teens.get(num_int)
        print(teens_eng)
    else:
        if num_int > 99:
            hundreds_digit = num_int // 100
            remaining_digits = num_int % 100
            hundreds_eng = ones.get(hundreds_digit)
            if remaining_digits == 0:
                print(hundreds_eng + ' hundred')
            elif 9 < remaining_digits < 20:
                    teens_eng = teens.get(remaining_digits)
                    print(hundreds_eng + ' hundred ' + teens_eng)
            else:
                tens_digit = remaining_digits // 10
                ones_digit = remaining_digits % 10
                if tens_digit > 1:
                    tens_eng = tens.get(tens_digit)
                    if ones_digit > 0:
                        ones_eng = ones.get(ones_digit)
                        print(hundreds_eng + ' hundred ' + tens_eng + ' ' + ones_eng)
                    else:
                        print(hundreds_eng + ' hundred ' + tens_eng)
                else:
                    ones_eng = ones.get(ones_digit)
                    print(hundreds_eng + ' hundred and ' + ones_eng)
        else:
            tens_digit = num_int // 10
            ones_digit = num_int % 10
            if tens_digit > 1:
                tens_eng = tens.get(tens_digit)
                if ones_digit > 0:
                    ones_eng = ones.get(ones_digit)
                    print(tens_eng + '-' + ones_eng)
                else:
                    print(tens_eng)
            else:
                ones_eng = ones.get(ones_digit)
                print(ones_eng)


num_int = input('Enter a number from 0 to 99: ').strip()
int_to_english(num_int)
