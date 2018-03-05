def to_unsigned(dec):
	return bin(dec)[2:]

def to_unpacked(dec):
	return "?"
	
def to_packed(dec):
	dec_list = list(str(dec))
	string = ""

	for num in dec_list:
		if len(bin(int(num))[2:]) < 4:
			string += "0" *  (4 - len(bin(int(num))[2:]))

		string += bin(int(num))[2:] + " "

	return string
	
def to_densely_packed(dec):
	return "?"

def run():
	while True:
		dec = int(input("Input: "))
		print("Unsigned = " + to_unsigned(dec))
		print("Unpacked = " + to_unpacked(dec))
		print("Packed = " + to_packed(dec))
		print("Densely Packed = " + to_densely_packed(dec))

if __name__=='__main__':
	run()