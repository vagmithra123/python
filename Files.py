#Opening file
myfile = open('myfile.txt')

#print(myfile.read())

myfile.seek(0)

#print(myfile.read())

myfile.seek(0)

newfile = open('/Users/shankar/Documents/test.txt')

print(newfile.read())

myfile.close()

newfile.close()

#One way of reading the file that is already open is to use with as

with open('myfile.txt') as my_new_file:
	contents = my_new_file.read()
print(contents)

with open('myfile.txt' , mode = 'r') as mfile:
	contents = mfile.read()
print(contents)


#r+ reading and writing
#w+ writing and reading 

with open('myfile.txt' , mode = 'a') as mfile:
	mfile.write('\n How are you?')

with open('myfile.txt', mode = 'r') as mfile:
	print(mfile.read())

with open('newtext.txt' , mode = 'w') as f:
	f.write('I created this file')

with open('newtext.txt', mode = 'r') as f:
	print(f.read())

