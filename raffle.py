import rafflefuncts
import random

add_user = rafflefuncts.add_user
del_user = rafflefuncts.del_user
print_list = rafflefuncts.print_list
start_raffle = rafflefuncts.start_raffle

# create a list of functions
function = {'1':add_user, '2':del_user, '3':print_list, '4':start_raffle}

#global var declarations go here
hash = {}
choice = ''

# prompt user for filename & store in variable:"fn"
fn = input("Enter file to open: ")

#Open file for reading
fh = open(fn, "a+")
fh.seek(0)

#transfer file line by line into dictionary (hash) with a while loop, splitting the username and password by the delimiter character ":"
lines = fh.readlines()
for line in lines:
	username = linearray[0]
	
# outer loop until user quits
while(choice != '5'):
	#inner loop until user enters correct option
	while(1):
	# print menu & prompt for user input: $choice
		print ("""
		User Accounts
		---------------------------
		1) Add user account
		2) Delete user account
		3) Print list of user accounts
        4) Start Raffle!
		5) Save and quits
		
		""")
		choice = input("Enter choice: ") 	
	
		# if the user enters a valid choice, exit inner loop	
		if choice in function or choice=='5':
			break
		print ("Unknown choice")
	if (choice=='5'):
		break
	# call appropriate function and assignthe function result to the dictionary (hash) to update it 
	# from anmt sheet: selection = ...
	selection = function[choice]
	hash = selection(hash)
#Close the file for reading
fh.close()
# prompt user to save changes, if so, then print the entire contents of the dictionary (hash) to the file & close the file for writing
saveit = input("Save contents? (y/n) ")
if (saveit == 'y'):
	fh = open(fn, 'w')
	for key, value in hash.items():
		my_string = key 
		fh.write(my_string)
	fh.close()
	


