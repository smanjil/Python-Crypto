# implement caesar cipher 

# function that performs both encryption and decryption according to user requirement

def helper(message , key , mode):
	LETTERS = 'abcdefghijklmnopqrstuvwxyz'
	translated = ''
	message = message.lower()
	for symbol in message:
		if symbol in LETTERS:
			num = LETTERS.find(symbol)
			if mode == 'E' or mode == 'e':
				num += key
			elif mode == 'D' or mode == 'd':
				num -= key
			if num >= len(LETTERS):
				num -= len(LETTERS)
			elif num < 0:
				num += len(LETTERS)
			translated += LETTERS[num]
		else:
			translated += symbol
	return translated.upper()

message = raw_input("Enter message : ")
mode = raw_input("Enter E/e for encrypt and D/d for decrypt : ")
key = input("Enter the encryption key(1-26) : ")

print helper(message , key , mode)



	







