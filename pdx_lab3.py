# Lab 3: Grading, attempt 1

grade = float(input("What was the student's score overall? "))

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

if letter_grade != 'F' and grade % 10 >= 7:
    print(letter_grade + '+')
elif letter_grade != 'F' and grade % 10 <= 3:
    print(letter_grade + '-')
else:
    print(letter_grade)
