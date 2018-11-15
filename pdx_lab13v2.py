ENGLISH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
user_rotation = int(input('What degree of rotation do you want the text encrypted? ').strip())

def encrypt(string):
    rotated = ''
    for i in range(len(string)):
        english_index = ENGLISH.index(string[i])
        rotated += ENGLISH[english_index + user_rotation]
    return rotated

def decrypt(string):
    decrypted = ''
    for i in range(len(string)):
        rot_index = ENGLISH.index(string[i])
        decrypted += ENGLISH[rot_index - user_rotation]
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
