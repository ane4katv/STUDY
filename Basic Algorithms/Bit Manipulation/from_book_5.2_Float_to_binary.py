# Python program to convert float 
# decimal to binary number 

# Function returns octal representation 
def float_bin(number, places = 3): 

	# split() seperates whole number and decimal 
	# part and stores it in two seperate variables 
	whole, dec_dec = str(number).split(".")

	# Convert both whole number and decimal 
	# part from string type to integer type 
	whole = int(whole) 
	dec_dec = int (dec_dec)

	# Convert the whole number part to it's 
	# respective binary form and remove the 
	# "0b" from it. 
	res = bin(whole).lstrip("0b") + "."

	# Iterate the number of times, we want 
	# the number of decimal places to be 
	for x in range(places): 

		# Multiply the decimal value by 2 
		# and seperate the whole number part 
		# and decimal part. Ex: if dec 0.27 and places = 3:
		# will go 3 loops from 0 27:  0 54 -> 1 08 -> 1 6
		dec_whole, dec_dec = str((decimal_converter(dec_dec)) * 2).split(".")

		# Convert the decimal part 
		# to integer again
		dec_dec = int(dec_dec)

		# Keep adding the integer parts 
		# receive to the result variable
		res += dec_whole

	return res 

# Function converts the value passed as 
# parameter to it's decimal representation 
def decimal_converter(num): 
	while num > 1: 
		num /= 10
	return num 


print(float_bin("3.27", 3))
