
# implement playfair cipher

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
		   'Q','R','S','T','U','V','W','X','Y','Z']

def get_key():
	key = raw_input("Enter the text : ").upper()
	check_repeated_alpha(key)
	
def check_repeated_alpha(key):
	newWord = ""
	for sym in key:
		if sym.isalpha() and sym not in newWord:
			newWord += sym
	gen_matrix(newWord)
	
	
def gen_matrix(newWord):
	matrix = []
	for char in newWord:
		if char in letters and char not in matrix:
			matrix.append(char)	
	for char in letters:
		if char not in matrix :
			matrix.append(char)
	for char in matrix:
		if char is "I" or char is "J":
			if char not in newWord:
				matrix.remove(char)
	print matrix
		
def get_message():
	message = []
	message = raw_input("Enter message : ")
	#print "\n" + message
	sub = []
	pair = []
	space_li = ""
		
	for char in message:
		if ord(char) >= 97 and ord(char) <= 122:
			space_li += char
	#print space_li
				
			
	if len(space_li) % 2 == 0:
		pair = space_li[:2]
		new = space_li[2:]
		sub.append(pair)
		while(len(new) != 0):
			pair = new[:2]
			new = new[2:]		
			sub.append(pair)
		print "\n" + str(sub)
	else:
		space_li += 'x'
		print space_li 
		pair = space_li[:2]
		new = space_li[2:]
		sub.append(pair)
		while(len(new) != 0):
			pair = new[:2]
			new = new[2:]		
			sub.append(pair)		
		print "\n" + str(sub) 

		
get_key()
get_message()


	
