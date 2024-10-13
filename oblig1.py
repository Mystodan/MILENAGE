from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from testdata import load_data_from_pdf

def xor(*args: bytes):
	'''
	Takes in any number of bytes objects, all of which must be of same length, 
	and performs an xor operation on them, returning a single bytes object.
	'''
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

def rot(x: bytes|bytearray, r: int, right: bool = False) -> bytes:
	'''
	x: Bytes to rotate, can be of any length
	r: How many BITS to rotate, must be divisible by 8
	right: Wheter to rotate the bits left or right, default left
	'''
	assert(r % 8 == 0), "rotation amount (r) must be divisible by 8"

	rot_amount : int = int(r/8)
	bytearr: bytearray = bytearray(x)
	if right:
		for _ in range(rot_amount):
			bytearr.insert(0, bytearr.pop(-1))
	else:
		for _ in range(rot_amount):
			bytearr.append(bytearr.pop(0))
	return bytes(bytearr)


def Ek(key: bytes, m: bytes) -> bytes:
	'''
	Encrypts input m using a block chiper using the input key, returns encrypted block in bytes
	'''
	assert(len(m) == 16), "m must be 128 bits long or 16 bytes"
	cipher = Cipher(algorithms.AES(key), modes.ECB())
	encryptor = cipher.encryptor()
	ct = encryptor.update(m) + encryptor.finalize()
	return ct

def f1(K: bytes, RAND: bytes, SQN: bytes, AMF: bytes, OP: bytes):	#Returns MAC-A (64-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	SQN: 48-bit sequence number \n
	AMF: 16-bit authentication managment field \n
	---
	returns MAC-A: 64-bit network authentication code
	'''
	#Define constants
	r1: int = 64
	c1: bytearray = bytearray(16)

	#Compute OPc and TEMP as described in 3GPP TS 35.206
	OPc: bytes = xor(OP, Ek(K, OP)) 		#OPc = OP ⊕ E[OP]k
	TEMP : bytes = Ek(K, xor(RAND, OPc)) 	#TEMP = E[RAND ⊕ OPC]k
	
	IN1 : bytes = SQN + AMF + SQN + AMF
	OUT1 : bytes = xor(OPc, IN1)
	OUT1 : bytes = rot(OUT1, r1)
	OUT1 : bytes = xor(OUT1, TEMP, c1)
	


	""" out : bytes = rot(xor(OPc, IN1), r1)
	out : bytes = xor(out, TEMP, c1)
	return xor(OPc, Ek(K, out))[:8]
 """

def f2(K: bytes, RAND: bytes, OP: bytes):	#Returns RES (64-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	---
	returns RES: 64-bit signed response
	'''
	#Define constants
	OPc: bytes = xor(OP, Ek(K, OP))
	TEMP : bytes = Ek(K, xor(RAND, OPc))

	r2: int = 0
	c2: bytearray = bytearray(16)
	c2[15] = 1

	out = rot(xor(TEMP, OPc), r2)
	out = Ek(K, (xor(out, c2)))
	out = xor(out, OPc)
	return out[8:]


def f3(K: bytes, RAND: bytes, OP: bytes):	#Returns CK (128-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	---
	returns CK: 128-bit confidentiality key
	'''
	#Define constants
	r3: int = 32
	c3: bytearray = bytearray(16)
	c3[15] = 2

	OPc: bytes = xor(OP, Ek(K, OP))
	TEMP : bytes = Ek(K, xor(RAND, OPc))

	return xor(Ek(K, xor(rot(xor(TEMP, OPc), r3), c3)), OPc)


def f4(K: bytes, RAND: bytes, OP: bytes):	#Returns IK (128-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	---
	returns IK: 128-bit integrity key
	'''
	#Define constants
	r4: int = 64
	c4: bytearray = bytearray(16)
	c4[15] = 4

	OPc: bytes = xor(OP, Ek(K, OP))
	TEMP : bytes = Ek(K, xor(RAND, OPc))
	
	return xor(Ek(K, xor(rot(xor(TEMP, OPc), r4), c4)), OPc)


def f5(K: bytes, RAND: bytes, OP: bytes):	#Returns AK (48-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	---
	returns AK: 48-bit anonymity key
	'''
	r2: int = 0
	c2: bytearray = bytearray(16)
	c2[15] = 1

	OPc: bytes = xor(OP, Ek(K, OP))
	TEMP : bytes = Ek(K, xor(RAND, OPc))
	out = rot(xor(TEMP, OPc), r2)
	out = Ek(K, (xor(out, c2)))
	out = xor(out, OPc)
	return out[:6]



