#range, only stop
for num in range(10):
	print(num)

#range , start, stop
for num in range(2, 10):
	print(num)

#range , start, stop, step
for num in range(2, 10, 2):
	print(num)

print(list(range(0, 11, 2)))

#Generator is a special type of function, it will generate information instead of saving it all to memory.

index_count = 0

for letter in 'abcde':
	print('At index {} the letter is {}'.format(index_count, letter))
	index_count += 1

#enumerate as list
index = 0
word = 'abcde'

for letter in word:
	print(word[index])
	index += 1

for item in enumerate(word):
	print(item)


for index, letter in enumerate(word):
	print(index)
	print(letter)
	print('\n')


#zipping lists using zip function

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
	print(item)


print(list(zip(mylist1, mylist2)))

#in keyword

print('x' in [1, 2,3])

print('a' in 'a world')

d = {'mykey' : 123}

print(123 in d.values())

#min function

mylist = [10,20,30, 40, 50]

print(min(mylist))

print(max(mylist))

#random shuffle function

mylist = [1,2,3,4,5,6,7,8,9]

from random import shuffle

random_list = shuffle(mylist)

print(mylist)

from random import randint

print(randint(0,100))

mynum = randint(1,10)

print(mynum)

a = int(input('Enter a number: '))

b = int(input('Enter a number: '))

print(f'Sum of a and b is, {a+b}')



