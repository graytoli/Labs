# Lab 22: Compute Automated Readability Index, version 1
import string
import math

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th grade'},
     6: {'ages': '10-11', 'grade_level':    '5th grade'},
     7: {'ages': '11-12', 'grade_level':    '6th grade'},
     8: {'ages': '12-13', 'grade_level':    '7th grade'},
     9: {'ages': '13-14', 'grade_level':    '8th grade'},
    10: {'ages': '14-15', 'grade_level':    '9th grade'},
    11: {'ages': '15-16', 'grade_level':   '10th grade'},
    12: {'ages': '16-17', 'grade_level':   '11th grade'},
    13: {'ages': '17-18', 'grade_level':   '12th grade'},
    14: {'ages': '18-22', 'grade_level':      'college'}
}

with open('ume_san.txt') as file:
    text = file.read()

translator = str.maketrans('', '', string.punctuation)
word_list = text.translate(translator).split()

def num_char(text):
    """ Calculates the number of characters in string or text, exlcuding all non-alphanumeric characters and spaces
    """
    all_char = ''.join(char for char in text if char.isalnum())
    return len(all_char)

def num_sentences(text):
    """ Calculates the number of sentences in a string or text by counting the number of occurrences of sentence-ending punctuation
    """
    sentence_count = 0
    sent_punct = ['.', '?', '!']
    for char in text:
        if char in sent_punct:
            sentence_count += 1
    return sentence_count

def ari_score(char, words, sent):
    return 4.71 * (char / words) + 0.5 * (words / sent) - 21.43

def main():
    ari_rounded = math.ceil(ari_score(num_char(text), len(word_list), num_sentences(text)))

    grade_placement = ari_scale[ari_rounded]

    print(f"""The ARI for this text is {ari_rounded}.
This corresponds to a(n) {grade_placement['grade_level']} level of difficulty suitable for the average {grade_placement['ages']} year old.
""")

main()
