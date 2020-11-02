# Tuples r immutable
# we use parentheses
#create tuple
t = (1, 2,3)
print(f'Type of t is {type(t)}')

#check length
print(f'Length of t is {len(t)}')

#Accessing tuple with index
print(f'Item at index 2 of t is {t[2]}')

#using count method
print(f"Number of 1's in t are {t.count(1)}")

#using index method
print(f'Index of 2 in t is {t.index(2)}')

#