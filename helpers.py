def rot(x: bytes|bytearray, r: int, right: bool = False) -> bytes:
	'''
	x: Bytes to rotate, can be of any length
	r: How many BITS to rotate, must be divisible by 8
	right: Wheter to rotate the bits left or right, default right
	'''
	bytearr: bytearray = bytearray(x)
	assert(r % 8 == 0)
	rot_amount : int = int(r/8)
	if right:
		for _ in range(rot_amount):
			bytearr.insert(0, bytearr.pop(-1))
	else:
		for _ in range(rot_amount):
			bytearr.append(bytearr.pop(0))
	return bytes(bytearr)


def xor(*args: bytes):
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
	

def bin2hex(binstr: str) -> str:
	'''
	Converts a binary str into a hex str \n
	"11001001" -> "c9"
	'''
	binstr : str = binstr.replace(" ", "")
	if (len(binstr) % 8 != 0):
		for i in range(8 - (len(binstr) % 8)):
			binstr = "0" + binstr
	byte_arr: bytearray = bytearray(0)
	for i in range(int(len(binstr)/8)):
		byte_arr.append(int(binstr[i*8:i*8+8], 2))
	return bytes(byte_arr).hex()

def is_bin(string: str) -> bool:
	'''
	Check if string is in binary
	'''
	string  = string.replace(" ", "")
	for i in range(len(string)):
		if (string[i] != "0" and string[i] != "1"):
			return False
	return True


#For testing that the functions work
if __name__ == '__main__':
	print(bin2hex("11001001"))

	