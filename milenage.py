from helpers import *
import testdata as td
#from Crypto.Cipher import AES #pycryptodome
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes



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

""" 
def old_Ek(key, m):
	assert(len(m) == 16)
	aes: AES = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(m)
 """
def Ek(key, m):
	assert(len(m) == 16)
	cipher = Cipher(algorithms.AES(key), modes.ECB())
	encryptor = cipher.encryptor()
	ct = encryptor.update(m) + encryptor.finalize()
	return ct

def Dk(key, ct):
	assert(len(ct) == 16)
	cipher = Cipher(algorithms.AES(key), modes.ECB())
	decryptor = cipher.decryptor()
	m = decryptor.update(ct) + decryptor.finalize()
	return m


def milenage(K: bytes, RAND: bytes, SQN: bytes, AMF: bytes, OP: bytes):
	OPc: bytes = xor(OP, Ek(K, OP))
	TEMP : bytes = Ek(K, xor(RAND, OPc))
	IN1: bytes = SQN + AMF + SQN + AMF
	
	OUT1: bytes = xor(Ek(K, xor(TEMP, rot(xor(IN1, OPc), r1), c1)), OPc)
	OUT2: bytes = xor(Ek(K, xor(rot(xor(TEMP, OPc), r2), c2)), OPc)
	OUT3: bytes = xor(Ek(K, xor(rot(xor(TEMP, OPc), r3), c3)), OPc)
	OUT4: bytes = xor(Ek(K, xor(rot(xor(TEMP, OPc), r4), c4)), OPc)
	OUT5: bytes = xor(Ek(K, xor(rot(xor(TEMP, OPc), r5), c5)), OPc)
	
	f1: bytes = OUT1[:8]
	f2: bytes = OUT2[8:16]
	f3: bytes = OUT3
	f4: bytes = OUT4
	f5: bytes = OUT2[:6]

	return f1, f2, f3, f4, f5


def reverse(K: bytes, RAND: bytes, OP: bytes, OUT3: bytes) -> bytes:
	OPc: bytes = xor(OP, Ek(K, OP))
	TEMP : bytes = Ek(K, xor(RAND, OPc))

	#OUT3: bytes = xor(Ek(K, xor(rot(xor(TEMP, OPc), r3), c3)), OPc)
	count = 16
	
	for i in range(count):
		IN3: bytes = xor(OUT3, OPc)
		IN3: bytes = Dk(K, IN3)
		IN3: bytes = xor(IN3, c3)
		IN3: bytes = rot(IN3, i*8, right=False)
		IN3: bytes = xor(IN3, OPc)
		if (TEMP == IN3):
			print(i*8)


def run_test():
	for i in range(6):
		test_data: dict = td.load_data(i+1)
		print(test_data['K'])
		break
		f1, f2, f3, f4, f5 = milenage(
								test_data['K'], 
								test_data['RAND'], 
								test_data['SQN'], 
								test_data['AMF'], 
								test_data['OP']
							)
		ex_f1: bytes = test_data['f1']
		ex_f2: bytes = test_data['f2']
		ex_f3: bytes = test_data['f3']
		ex_f4: bytes = test_data['f4']
		ex_f5: bytes = test_data['f5']

		print(f"Running test nr: {i+1}")
		print(f"f1 passed: {f1 == ex_f1}")
		print(f"f2 passed: {f2 == ex_f2}")
		print(f"f3 passed: {f3 == ex_f3}")
		print(f"f4 passed: {f4 == ex_f4}")
		print(f"f5 passed: {f5 == ex_f5}")
		print()

if __name__ == "__main__":

	#Define Constants
	r1: int = 64
	r2: int = 0
	r3: int = 32
	r4: int = 64
	r5: int = 96
	c1, c2, c3, c4, c5 = create_c()
	
	run_test()



