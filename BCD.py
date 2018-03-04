'''	BCD representation: 
	Input: Decimal; 
	Output: Unsigned binary, 
			Unpacked BCD, 
			Packed BCD, 
			Densely Packed BCD
'''

if __name__=='__main__':
	while True:
		dec = int(input("Input: "))
		ub = bin(dec)
		print("Unsigned binary = " + ub[2:len(ub)])