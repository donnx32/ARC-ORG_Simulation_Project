decimal_list = []

# Densely Packed Decimal Encoding Dictionary
dpd_dict = {('0','0','0'): ['b', 'c', 'd', 'f', 'g', 'h', 0, 'j', 'k', 'm'],
            ('0','0','1'): ['b', 'c', 'd', 'f', 'g', 'h', 1, 0, 0, 'm'],
			('0','1','0'): ['b', 'c', 'd', 'j', 'k', 'h', 1, 0, 1, 'm'],
			('0','1','1'): ['b', 'c', 'd', 1, 0, 'h', 1, 1, 1, 'm'],
			('1','0','0'): ['j', 'k', 'd', 'f', 'g', 'h', 1, 1,0, 'm'],
			('1','0','1'): ['f', 'g', 'd', 0, 1, 'h', 1, 1, 1, 'm'],
			('1','1','0'): ['j', 'k', 'd', 0, 0, 'h', 1, 1, 1, 'm'],
			('1','1','1'): [0, 0, 'd', 1, 1, 'h', 1, 1, 1, 'm']}

def to_unsigned(dec):
	return bin(dec)[2:]

def to_unpacked(dec):
	string = ""

	for num in decimal_list:
		if len(bin(int(num))[2:]) < 8:
			string += "0" *  (8 - len(bin(int(num))[2:]))

		string += bin(int(num))[2:] + " "

	return string

def to_packed(dec):
	string = ""

	for num in decimal_list:
		if len(bin(int(num))[2:]) < 4:
			string += "0" *  (4 - len(bin(int(num))[2:]))

		string += bin(int(num))[2:] + " "

	return string

def to_densely_packed(dec):
	p = to_packed(dec)
	bool = True
	t = []
	f = []
	string = ""
	temp_dict = {'a': '',
				 'b': '',
				 'c': '',
				 'd': '',
				 'e': '',
				 'f': '',
				 'g': '',
				 'h': '',
				 'i': '',
				 'j': '',
				 'k': '',
				 'm': ''}
	
	# Loop to get a, e, i and store to list file
	# and loop to store all elements to t
	for c in p:
		t.append(c)
		if bool:
			f.append(c)
			bool = False
		if c == " ":
			bool = True
	try:	
		i = 0
		for key, value, in temp_dict.items():
			if t[i] == " ":
				i += 1

			temp_dict[key] = t[i]
			i += 1
			
		i = 1
	
		for e in dpd_dict[tuple(f)]:
			if e == 0:
				string += "0"
			elif e == 1:
				string += "1"
			else:
				string += temp_dict[e]
			
			# For spaces
			if i == 3:
				string += " "
			elif i == 6:
				string += " "
			i += 1
	except:
		string = "Decimal is not 3 digits... :'("
	return string

def run():
	global decimal_list
	while True:
		dec = int(input("Input: "))
		decimal_list = list(str(dec))

		print("Unsigned = " + to_unsigned(dec))
		print("Unpacked = " + to_unpacked(dec))
		print("Packed = " + to_packed(dec))
		print("Densely Packed = " + to_densely_packed(dec))
		print("")

		decimal_list = []

if __name__=='__main__':
	run()