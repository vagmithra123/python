name  = "Sam"
print("Name is :", name)

lastletters = name[1:]

print("LastLetters of name are : ", lastletters)

print(lastletters * 4)

print("I ", lastletters , "super cool")


print('Sum of 2 and 3 is: ', 2+3)

print(f'Sum of 2 and 3 is :  {2+3}')

print('Sum of 2 and 3 is: {}'.format(2+3))

print("2 concatenated with 3 is :", '2' + '3')

print("2 concatenated with 3 is :{}".format('2' + '3'))

print(f"2 concatenated with 3 is: {'2'+ '3'}")

message = "Today is a beautiful day!"

for i in range(5):
	message = 'Hello!' + message 
	print(message)

#String Methods

x = 'Hello World!'

print('Using upper method for ',x , 'gives ', x.upper())

print('Using lower method on ', x , 'gives ', x.lower())

print('Using split method on ', x, 'gives ', x.split())

x = 'This is a nice string' 

print('Splitting  "',x , ' " by letter i gives ', x.split('i'))

