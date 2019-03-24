# Lab 13: ROT Cipher, version 2

ENGLISH = 'abcdefghijklmnopqrstuvwxyz'

def decipher(string, n, decode=False):
    if decode:
        n= -n
    coded = ''
    for i in range(len(string)):
        idx = ENGLISH.find(string[i].lower())
        if idx > -1:
            rotate_idx = (idx + n) % 26
            coded += ENGLISH[rotate_idx]
        else:
            coded += string[i]
    return coded

def repl():
    while True:
        while True:
            operation = input('Would you like to (e)ncrypt or (d)ecrypt a message? ').lower().strip()
            if operation in ['e', 'encrypt', 'd', 'decrypt']:
                break

        while True:
            try:
                n = int(input('To what degree of rotation do you want the text encrypted? ').strip())
                break
            except ValueError:
                pass

        if operation.startswith('e'):
            user_input = input('Enter a message you would like to encrypt:\n')
            print(decipher(user_input, n))
        else:
            user_input = input('Enter a message you would like to decrypt:\n')
            print(decipher(user_input, n, decode=True))

        while True:
            play_again = input('Would you like to play again? ').lower().strip()
            if play_again in ['y', 'yes', 'n', 'no']:
                break

        if play_again.startswith('n'):
            break

repl()
