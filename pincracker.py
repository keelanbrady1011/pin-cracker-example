# PIN CRACKER
#! /etc/bin/pythn3

import base64

def main():
	hashed_pass = input("Enter Encrpyted PIN >> ")
	hashed_pass_bytes = hashed_pass.encode("utf-8")
	hashed_pass_string = str(hashed_pass_bytes)
	result = decrypt(hashed_pass_string)

def decrypt(hash1):
	
#	takes in hashed input, bruteforces using numbers 
#	list, encodes numbers with b64 and compares with 
#	hash input. If it is incorrect it will keep going,
#	if correct it will return the value of the 
#	decrypted hash to the "result" value
	
	correct = False
	a = 0
	b = 0
	c = 0
	d = 0

	while correct == False:
		attempt = str(a) + str(b) + str(c) + str(d)
		attempt_bytes = attempt.encode("utf-8")
		encoded_bytes = base64.b64encode(attempt_bytes, altchars=None)
		encoded = str(encoded_bytes)
		print("Trying PIN [" + attempt + "]... ", end='')
#		print(" [" + encoded + " : " + hash1 + "] ", end='') # for debugging

		if encoded != hash1:
			if d == 9:
				if c == 9:
					if b == 9:
						if a == 9:
							if b == 9 and c == 9 and d == 9:
								correct = True
								print('PIN NOT FOUND')
								break
						else:
							b = 0
							a = a + 1
					else:
						c = 0
						b = b + 1

				else:
					d = 0
					c = c + 1
			else:
				d = d + 1
			print("WRONG.")
		else:
			print("FOUND!!\n")
			print("THE PIN IS " + attempt)
			correct = True


if __name__ == '__main__':
	main()