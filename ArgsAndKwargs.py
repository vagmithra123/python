#  *args treats as a tuple. WE can pass as many args as we want.

def myfunc(*args):
	print(args)


myfunc(40,60,30,60)

#args can be any other keyword

def myfunc(*spam):
	for item in spam:
		print(item)


myfunc(4,5,6,7,8)

# ** kwargs Key worded arguments

def myfunc(**kwargs):
	if  'fruit' in kwargs:
		print('Myfruit of choice is {}'.format(kwargs['fruit']))
	else:
		print("I didn't find any fruit here")


myfunc(fruit = 'apple', veggie = 'lettuce')
