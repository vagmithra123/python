#sets are unordered collections of unique elements


#creating set
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(f'Elements of my_set are {my_set}')




new_set = {1, (1,2), 'Hello'}
print(f'Elements of new_set are {new_set}')

#Adding multiple elements to sets

my_set.update([4,5,6])
print(f'Elements of my_set are {my_set}')

my_set.update([4,5], {1,9,8})
print(f'Elements of my_set are {my_set}')

unique_elements = set('HelloWorld')

print(unique_elements)

unique_elements.pop()

print(f'unique_elements are popping {unique_elements}')

