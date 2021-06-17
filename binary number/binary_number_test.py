def function_number_binary_1(num):
	if num >= 1:
		function_number_binary_1(num // 2)
	print(num % 2,end="")

def function_number_binary_2(n):
    return bin(n).replace("0b","")

def functio_number_binary_3(number):
	return "{0:b}".format(int(number))

if __name__ == '__main__': 

	input_1 = 8
	input_2 = 18
	input_3 = 18
	print(function_number_binary_1(input_2))
	print(function_number_binary_2(input_2))
	print(functio_number_binary_3(input_2))