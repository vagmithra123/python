# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
x = st.split()
mylist = [word for word in x if word.startswith("s")]
print(mylist)



# Use range() to print all the even numbers from 0 to 10.

for num in range(0,11):
	if(num % 2 == 0):
		print(num)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mylist = [x for x in range(1,51) if (x%3 == 0)]
print(mylist)

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
x = st.split()
mylist = [word for word in x if (len(word) % 2 == 0)]
print(mylist)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

mylist = []
for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		mylist.append("FizzBuzz")
	elif num % 3 == 0:
		mylist.append("Fizz")
	elif num % 5 == 0:
		mylist.append("Buzz")
	else:
		mylist.append(num)

print(mylist)

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

mylist = [s[0] for s in st.split()]
print(mylist)




