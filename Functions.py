# def name_of_function():
'''
Docstring explains function.
'''

def say_hello(name='Default'):
	print("Hello " + name)
	

say_hello("sudha")
say_hello()
say_hello()

def add_num(num1,num2):
	return num1+num2

result = add_num(5,6)
print(result)

str = add_num('10','20')
print(str)

#check a single number is even

def check_even(num):
	if num%2 == 0:
		return 'even'
	else:
		return 'odd'


ans = check_even(24)
print(ans)