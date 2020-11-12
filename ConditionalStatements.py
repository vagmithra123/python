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