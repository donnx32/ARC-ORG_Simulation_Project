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

# Temporary dictionary to store the current binary respectively.
temp_dict = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 
			 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'm': ''}

def to_unsigned(dec):
	return bin(dec)[2:]

def to_unpacked(dec):
	string = ""

	for num in decimal_list:
		if len(bin(int(num))[2:]) < 8:
			string += "0" *  (8 - len(bin(int(num))[2:]))

		string += bin(int(num))[2:]

	return string

def to_packed(dec):
	string = ""
	d_list = list(str(dec))
	for num in d_list:
		if len(bin(int(num))[2:]) < 4:
			string += "0" *  (4 - len(bin(int(num))[2:]))

		string += bin(int(num))[2:]

	return string
	
# Zero extends the decimal making it divisible by 3 stores it into a global variable decimal_list
def zero_extend_dec():	
	global decimal_list
	n = 3 - (len(decimal_list) % 3)
	
	if n != 3:
		for x in range(n):
			decimal_list.insert(0, '0')

# Stores the bin parameter to a global temporary dictionary where each binary digits is stored into its respective key. E.i. a, b , c, d, etc...
def to_temp_dict(bin):
	global temp_dict
	temp_list = list(bin)

	i = 0
	
	for key, value, in temp_dict.items():
		temp_dict[key] = temp_list[i]
		i += 1

# Return a list of AEI
def get_aei():
	global temp_dict
	temp_list = []
	
	temp_list.append(temp_dict['a'])
	temp_list.append(temp_dict['e'])
	temp_list.append(temp_dict['i'])

	return temp_list

# Return a densely packed from a packed BCD stored in a global variable.
def dpd_decode(aei_list):
	string = ""
	global temp_dict
	
	for e in dpd_dict[tuple(aei_list)]:	
		if e == 0:
			string += "0"
		elif e == 1:
			string += "1"
		else:
			string += temp_dict[e]
	
	return string

# Iterates as many as required and generates a final densely packed BCD output. Uses a global variable decimal_list
def to_densely_packed():
	global decimal_list
	string = ""
	dec = ""

	zero_extend_dec()

	for x in range(int(len(decimal_list)/3)):
		for y in range(3):
			dec += str(decimal_list.pop(0))
			
		to_temp_dict(to_packed(str(dec)))
		string += dpd_decode(get_aei())
		dec = ""
		
	return string

# Infinite loop for the main program. input 0 to exit.
def run():
	global decimal_list
	
	while True:
		try:
			dec = int(input("Input: "))
			
			if dec == 0:
				break
				
			decimal_list = list(str(dec))

			print("Unsigned = " + to_unsigned(dec))
			print("Unpacked = " + to_unpacked(dec))
			print("Packed = " + to_packed(dec))
			print("Densely Packed = " + to_densely_packed())
			print("")

			decimal_list = []
		
		except:
			print("Please input a number")

# Main
if __name__=='__main__':
	run()