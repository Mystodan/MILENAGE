from helpers import *
import testdata as td
from Crypto.Cipher import AES
from Crypto import Random





'''
	List of Symbols:
	= 			The Assignment operator
	^ / *			The bitwise exclusive-OR operation.
	||			The concatenation of the two operands. (+ should also work)
	E[x]k		The Result of applying a block cipher encryption to the input value x using the key k
	rot(x,r) 	The result of cyclically rotating the 128-bit value x by r bit positions towards the most significant bit.
	X[i]		the ith bit in the variable X.

	List of Variables:
	AK		a 48-bit anonymity key that is the output of either of f5 and f5*.
	AMF		a 16-bit authentication managment field that is the input to f1 and f1*.
	c1, c2, c3, c4, c5		128-bit constants, which are XORed onto intermediate variables
	CK		a 128-bit confidentiality key that is the output of f3
	IK		a 128-bit integrity key that is the output of f4
	IN1		a 128-bit valye constructed from SQN and AMF that is used in the conputation of f1 and f1*
	K		a 128-bit subscriber key that is the input to f1, f1*, f2, f3, f4, f5, and f5*
	MAC-A	a 64-bit network authentication code that is the output of f1
	MAC-S	a 64-bit resynchronisation authentication code that is the output of f1*
	OP		a 128-bit Operator Variant Algorithm Configuration Field that is a component of f1, f1*, f2, f3, f4, f5 and f5*
	OPc		a 128-bit value derived from OP and K and used within the computation of the functions
	OUT1, OUT2, OUT3, OUT4, OUT5		128-bit computed values from which the outputs of f1, f1*, f2, f3, f4, f5 and f5* are obtained
	r1, r2, r3, r4, r5		integers in the range 0-127 inclusive, which defines the amounts by which intermediate varables are cyclically rotated. Always divisible by 8
	RAND	a 128-bit random challenge that is an input to f1, f1*, f2, f3, f4, f5, and f5*
	RES		a 64-bit signed response that is the output of f2
	SQN		a 48-bit sequence number that is an input to f1 or f1*
	TEMP	a	128-bit value used in the computations of the functions
'''

def Ek(key, plaintext):
	assert(len(plaintext) == 16)
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(plaintext)


def f1(K: bytes, RAND: bytes, SQN: bytes, AMF: bytes):	#Returns MAC-A (64-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	SQN: 48-bit sequence number \n
	AMF: 16-bit authentication managment field \n
	---
	returns MAC-A: 64-bit network authentication code
	'''
	ROPc : bytes = Ek(K, xor(OPc, RAND))
	out : bytes = SQN + AMF + SQN + AMF
	out : bytes = rot(xor(OPc, out), r1)
	out : bytes = xor(out, ROPc, c1)
	return xor(OPc, Ek(K, out))[:8]


def f2(K: bytes, RAND: bytes):	#Returns RES (64-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	---
	returns RES: 64-bit signed response
	'''
	pass


def f3(K: bytes, RAND: bytes):	#Returns CK (128-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	---
	returns CK: 128-bit confidentiality key
	'''
	pass


def f4(K: bytes, RAND: bytes):	#Returns IK (128-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	---
	returns IK: 128-bit integrity key
	'''
	pass


def f5(K: bytes, RAND: bytes):	#Returns AK (48-bits)
	'''
	K: 128-bit subscriber key \n
	RAND: 128-bit random challenge \n
	---
	returns AK: 48-bit anonymity key
	'''
	pass






		
	



if __name__ == "__main__":
	test_data: dict = td.load_data(1)
	#Define input variables for f1, f2, f3, f4, and f5
	K: bytes = test_data['K']
	RAND: bytes = test_data['RAND']
	SQN: bytes = test_data['SQN']
	AMF: bytes = test_data['AMF']

	#Other variables
	OP: bytes = test_data['OP']
	OPc: bytes = test_data['OPc']

	#Define expected outputs
	ex_out_f1: bytes = test_data['f1']
	ex_out_f2: bytes = test_data['f2']
	ex_out_f3: bytes = test_data['f3']
	ex_out_f4: bytes = test_data['f4']
	ex_out_f5: bytes = test_data['f5']

	#Define Constants
	r1: int = 64
	r2: int = 0
	r3: int = 32
	r4: int = 64
	r5: int = 96

	c1, c2, c3, c4, c5 = create_c()

	print(f"f1:		{f1(K, RAND, SQN, AMF)}\nexpected f1:	{ex_out_f1}")
	print(f"f1 gives expected output: {f1(K, RAND, SQN, AMF) == ex_out_f1}")