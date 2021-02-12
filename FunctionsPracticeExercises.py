''' LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5'''

def lesser_of_two_evens(a, b):
	if a%2 == 0 and b%2 == 0:
		return min(a,b) 
	elif a%2 == 0 || b%2 == 0:
		return max(a,b)



''' ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False'''

def animal_crackers(text):
	x = text.split()
	return x[0][0] == x[1][0]:
		

''' MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False'''

def makes_twenty(a,b):
	return (a+b) == 20 or a == 20 or b == 20

''' OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald '''

def old_macdonald(name):
	if len(name) > 3:
		return name[:3].capitalize() + name[3:].capitalize()
	else:
		return 'Name is too short!'


''' MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
'''

def master_yoda(text):
	return " ".join(reversed(text.split()))

''' ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
'''

def almost_there(n):
	return ((abs(100 - n) <= 10) or (abs(200 -n) <= 10))

''' FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''

def has_33(nums):
	for i in range(0, len(nums) -1):
		if nums[i] == 3 and nums[i+1] == 3:
			return True

	return False

''' 
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''

def paper_doll(text):
	return (text[0: len(text)] * 3)

'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''

def blackjack(a,b,c):
	if sum(a,b,c) <= 21:
		return sum((a,,b,c))
	elif sum ((a,b,c)) >= 21 and 11 in (a,b,c):
		return sum((a,,b,c)) - 10
	else:
		return 'BUST'


