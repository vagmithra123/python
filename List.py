mylist = [1, 2,3]

print(mylist)

print(f'Elements of list are {mylist}')

print(f'Elements of list from index 1 are {mylist[1:]}')

newlist = [4,5]

print(f'Contatenating mylist and newlist {mylist + newlist}')


mylist[1] = 4

print(mylist)

#append
#pop
#sort
#reverse

print(f'List before appending 5 {mylist}')

mylist.append(5)

print(f'List after appending 5 {mylist}')

print(f'List before pop {mylist}')

mylist.pop()

print(f'List after popping {mylist}')

mylist.pop(1)

print(f'List after popping index 1 {mylist}')

mylist.append(6)

mylist.append(4)

print(f'List before sorting {mylist}')

mylist.sort()

print(f'List after sorting {mylist}')

print(f'List before reversing {mylist}')

mylist.reverse()

print(f'List after reversing {mylist}')