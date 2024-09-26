def rot(x: bytes|bytearray, r: int, right: bool = True) -> bytes:
	'''
	x: Bytes to rotate, can be of any length
	r: How many BITS to rotate, must be divisible by 8
	right: Wheter to rotate the bits left or right, default right
	'''
	bytearr: bytearray = bytearray(x)
	assert(r % 8 == 0)
	rot_amount = r/8
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
def b2a(b: bytes) -> str:
	'''Bytes to ascii. For 16 bytes objects only'''
	print(len(b))
	assert len(b) == 16
	tmp = list()
	for i in range(len(b)):
		tmp.append(f"{b[i]:02x}")
	return "".join(tmp)+"\n"


def xor(a: bytes, b: bytes) -> bytes:
	pass


#For testing that the functions work
if __name__ == '__main__':
	bits: bytes = b"1234567890123456"
	print(int.from_bytes(bits))
	print(b2a(bits))
	