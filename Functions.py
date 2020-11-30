# def name_of_function():
'''
Docstring explains function.
'''

def say_hello(name='Default'):
	print("Hello " + name)
	

say_hello("sudha")
say_hello()

def add_num(num1,num2):
	return num1+num2

result = add_num(5,6)
print(result)

str = add_num('10','20')
print(str)

#Using Logical statements like if, for, while in functions
#check a single number is even

def check_even(num):
	if num%2 == 0:
		return 'even'
	else:
		return 'odd'


ans = check_even(24)
print(ans)

# passing a list to a method
def check_even_list(num_list):
	for num in num_list:
		if num % 2 == 0:
			return True
		else:
			pass

	return False

ans = check_even_list([1,3,5])
print(ans)

ans = check_even_list([2,4,6])
print(ans)


#return a list of even number in given list

def return_even_list(num_list):

	even_numbers = []

	for num in num_list:
		if num % 2 == 0:
			even_numbers.append(num)

		else:
			pass

	return even_numbers


list = return_even_list([1,2,3,4,5,6])
print(list)

