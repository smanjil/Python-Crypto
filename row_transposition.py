
import math

def main():
    
    message = raw_input("Enter message : ")
    key = input("Enter key : ")
    helper(message , key)

def helper(message , key):
    
    space_li = ""
    
    for char in message:
        if ord(char) >= 97 and ord(char) <= 122:
            space_li += char
            
    length = len(space_li)
    print "message length : " , length
    
    no_of_cols = len(str(key))
    print "no of cols(key) : " , no_of_cols
    
    div = float(length) / float(no_of_cols)
    print "div : " , div
    
    no_of_rows = int(math.ceil(div))
    print "no of rows : " , no_of_rows
    
    cipher = []    
    
    k = 0
    
    for i in range(int(no_of_rows)):
        cipher.append([])
        for j in range(no_of_cols):
            if k < length:
                cipher[i].append(space_li[k])
                k += 1
            else:
                cipher[i].append('*')
    print cipher
    
    mes = ""
    for i in range(no_of_rows):
		for j in range(no_of_cols):
			mes += cipher[i][j]
    print mes
    
    enc = ""
    
    for i in range(no_of_cols):
		k = i
		if k < len(mes):
			enc += mes[k]
			k += no_of_cols
		
		print enc
			
    

if __name__ == '__main__':
    main()




