ENGLISH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ROT_13 =  'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

def encrypt(string):
    rotated = ''
    for i in range(len(string)):
        english_index = ENGLISH.find(string[i])
        if english_index > -1:
            rotated += ROT_13[english_index]
        else:
            rotated += string[i]
    return rotated

def decrypt(string):
    decrypted = ''
    for i in range(len(string)):
        rot13_index = ROT_13.find(string[i])
        if rot13_index > -1:
            decrypted += ENGLISH[rot13_index]
        else:
            decrypted += string[i]
    return decrypted


def repl():
	while True:
		while True:
			operation = input('Would you like to (e)ncrypt or (d)ecrypt a message? ').lower().strip()
			if operation in ['e', 'encrypt', 'd', 'decrypt']:
				break

		if operation.startswith('e'):
			user_input = input('Enter a message you would like to encrypt:\n')
			print(encrypt(user_input))
		else:
			user_input = input('Enter a message you would like to decrypt:\n')
			print(decrypt(user_input))

		while True:
			play_again = input('Would you like to play again? ').lower().strip()
			if play_again in ['y', 'yes', 'n', 'no']:
				break

		if play_again.startswith('n'):
			break

repl()
