# implementation of hill cipher


key = []

def get_key():
    for i in range(3):
        key.append([])
        for j in range(3):
            inp = input("Enter {0} , {1} element : "  .format(i , j))
            #print type(inp)
            key[i].append(inp)
    print key
    get_plain_text()

def get_plain_text():
    first = ""
    second = ""
    third = ""
    i = 0
    plain = raw_input("Enter your message : ")
    space_li = ""
    for char in plain:
        if ord(char) >= 97 and ord(char) <= 122:
	    space_li += char
    print list(split_by_n(space_li , 3))
    
    
def split_by_n( space_li , n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]
    


get_key()