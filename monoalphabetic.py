# implement monoalphabetic cipher 

def helper(message , mode):
	map = {'a':'r' , 'b':'z' , 'c':'b' , 'd':'t' , 'e':'a' , 'f':'k' , 'g':'f' , 
		   'h':'c' , 'i':'p' , 'j':'u' , 'k':'e' , 'l':'x' , 'm':'d' , 'n':'g' , 
		   'o':'i' , 'p':'j' , 'q':'y' , 'r':'h' , 's':'v' , 't':'w' , 'u':'q' , 
		   'v':'l' , 'w':'m' , 'x':'o' , 'y':'n' , 'z':'s'}
	translated = ''
	message = message.lower()
	for symbol in message:
		if symbol in map:
			if mode == 'e' or mode == 'E':
				translated += map[symbol]
			elif mode == 'd' or mode == 'D':
				for key,value in map.items():
					if symbol == value:
						translated += key
		else:
			translated += symbol
	return translated.upper()
	
message = raw_input("Enter message : ")
mode = raw_input("Enter E/e for encryption and D/d for decryption : ")

print helper(message , mode)

