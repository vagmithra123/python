#print even or odd number
#if and elif
num = 6
if(num % 2 == 0):
	print(f'{num} is even')
else:
	print(f'Number is odd {num}')



#for
mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
	if num % 2 == 0:
		print(num)
	else:
		print(f'{num} is odd')

#tuple unpacking
mylist = [(1,2,3), (5,6,7), (8,9,10)]
for a,b,c in mylist:
	print(a)
	print(b)
	print(c)


#iterating through a dict
d = {'k1':1, 'k2':2,'k3':3}

for item in d:
	print(item) 

#to print all items
for item in d.items():
	print(item)

#To print all tuples
for key,value in d.items():
	print(key)
	print(value)

#to print all values
for value in d.values():
	print(value)

#to iterate through a string
for _ in 'Hello World':
	print('Cool!')