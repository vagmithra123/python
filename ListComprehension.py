# List Comprehensions are a unique way of quickly creating a list with Python

mystring = 'hello'

mylist = []

for letter in mystring:
	mylist.append(letter)

print(mylist)

mylist = [letter for letter in mystring]

print(mylist)

mylist = [letter for letter in 'Word']

print(mylist)

mylist = [num for num in range(0,11)]

print(mylist)

mylist = [num**2 for num in range(0,11)] #To square numbers

print(mylist)

#To get only even numbers

mylist = [(num %2 == 0) for num in range(0,11)]

print(mylist)

mylist = [x**2 for x in range(0,11) if x%2 == 0]

print(mylist)


celcius = [0, 10, 20, 34.5]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]

print(fahrenheit)










