def rot(x: bytes|bytearray, r: int, right: bool = True) -> bytes:
	'''
	x: Bytes to rotate, can be of any length
	r: How many BITS to rotate, must be divisible by 8
	right: Wheter to rotate the bits left or right, default right
	'''
	bytearr: bytearray = bytearray(x)
	assert(r % 8 == 0)
	rot_amount : int = int(r/8)
	if right:
		for i in range(rot_amount):
			bytearr.insert(0, bytearr.pop(-1))
	else:
		for i in range(rot_amount):
			bytearr.append(bytearr.pop(0))
	return bytes(bytearr)


def a2b(s: str) -> bytes:
	'''
	Turns a hex string into bytes, same as the bytes.fromhex() method
	'''
	s = s.replace(" ", "")
	assert(len(s) % 2 == 0)
	bytelist: list = list()
	for i in range(0, len(s), 2):
		bytelist.append(int("0x"+s[i]+s[i+1], 16))
	return bytes(bytelist)


#Something doesn't work here, don't know what. Copied from Milenage PowerPoint 
#bytes.decode("ascii") should work instead 
def b2a(b: bytes) -> str:
	'''
	Bytes to ascii. For 16 bytes objects only
	'''
	assert len(b) == 16
	tmp = list()
	for i in range(len(b)):
		tmp.append(f"{b[i]:02x}")
	return "".join(tmp)+"\n"

#Working xor function for 2 variables, newer ones can xor any amount
def old_xor(a: bytes, b: bytes) -> bytes:
    '''
    Takes in two variables: bytes and xor's them by 
    first converting them to int (basically binary)
    
    returns: bytes that have been xor'd
    '''
    return int.to_bytes(int.from_bytes(a)^int.from_bytes(b))

def old_too_xor(*args: bytes) -> bytes:
    '''
    Takes in any number of arguments (at least 1) and xors each of them.
    Works by first converting them to integers, xoring the integers, then returning bytes
    '''
    assert (len(args) > 0), "xor must get at least 1 argument"
    bin_int : int = 0
    for arg in args:
        bin_int = bin_int ^ int.from_bytes(arg)
    return int.to_bytes(bin_int)

def WIP_xor(*args: bytes) -> bytes:
	assert(len(args) > 0), "xor must get at least 1 argument"
	if len(args) == 1:
		return args[0]
	for n in range(len(args)-1):
		pass

def works_xor(a: bytes, b: bytes) -> bytes:
	assert(len(a) == len(b)), "Args bust be same length"
	byte_arr: bytearray = bytearray(len(a))
	for i in range(len(a)):
		byte_arr[i] = a[i] ^ b[i]
	return bytes(byte_arr)

def xor(*args : bytes) -> bytes:
	'''
	Takes in any number of bytes objects and xors them, they must all be of the same length.
	Returns a single bytes object that's the result of xoring all inputs
	'''
	assert(len(args) > 0), "xor must get at least 1 argument"
	#Checks if all input arguments are the same length
	args_len: int = len(args[0])
	for arg in args:
		if len(arg) != args_len:
			raise ValueError
	
	#If there's only one argument, return that
	if len(args) == 1:
		return args[0]
	
	#If there's two arguments, xor those and return the result
	elif len(args) == 2:
		byte_arr: bytearray = bytearray(len(args[0]))
		for i in range(len(args[0])):
			byte_arr[i] = args[0][i] ^ args[1][i]
		return bytes(byte_arr)

	#If there are more than two arguments, split the args list into multiple
	#smaller lists, and run this xor function on them recursivly
	else:
		args_left: list = args[0:int(len(args)/2)]
		args_right: list = args[int(len(args)/2):]
		left : bytes = xor(*args_left)
		right : bytes = xor(*args_right)
		return xor(left, right)
			
def xor2(*args: bytes):
	assert(len(args) > 0), "xor must get at least 1 argument"
	if len(args) == 1:
		return args[0]
	for i in range(len(args)):
		if len(args[i]) != len(args[0]):
			raise ValueError
	byte_arr: bytearray = bytearray(len(args[0]))
	for arg in args:
		for i in range(len(arg)):
			byte_arr[i] = byte_arr[i] ^ arg[i]
	return bytes(byte_arr)


def change_char(string: str, char: str, index: int) -> str:
    '''
    Changes char at index in a given string
    
    string: string to modify
    char: character to change to
    index: at which index to change the character
    
    returns: string with changed value
    '''
    assert (len(string) > index), "index must be within scope"
    assert (len(char) == 1), "char must be of length 1"
    new_str: str = ""
    for i in range(len(string)):
        if i != index:
            new_str += string[i]
        else:
            new_str += char
    return new_str


def bit_str_to_bytes(string: str) -> bytes|int:
	'''
	Turns a string of bits into bytes. "101" -> b"\\x05".

	Input string must consist of only 1s and 0s.
	'''
	out_int: int = 0
	#Check is string only contains 1s and 0s
	for i in range(len(string)):
		if string[i] != "0" and string[i] != "1":
			raise ValueError("input string must be in bit format")
	for count, value in enumerate(string[::-1]):
		out_int += int(value) * (2**count)
	return int.to_bytes(out_int)


def create_c() -> tuple:
	'''
	Creates all 5 c constants and returns them as a tuple, needs to be unpacked
	'''
	base_array: bytearray = bytearray(16)
	c1 = base_array.copy()

	c2 = base_array.copy()
	c2[15] = 1

	c3 = base_array.copy()
	c3[15] = 2

	c4 = base_array.copy()
	c4[15] = 4

	c5 = base_array.copy()
	c5[15] = 8

	return c1, c2, c3, c4, c5
	




#For testing that the functions work
if __name__ == '__main__':
	bits: bytes = b"1234567890123456"
	#print(xor(b"\x01", b"\x01", b"\x10", b"\x10"))
	inputs: tuple = (b"afdefgju", b"oangosyq", b"agmkyhlo", b"12f34567", b"24681357",)
	print(xor(*inputs))
	print(xor2(*inputs))

	#print(create_c())
	