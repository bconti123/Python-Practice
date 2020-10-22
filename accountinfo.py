import accountinfo_functs 

add_user = accountinfo_functs.add_user
edit_user = accountinfo_functs.edit_user
del_user = accountinfo_functs.del_user
print_list = accountinfo_functs.print_list

# create a list of functions
function = {'1':add_user, '2':edit_user, '3':del_user, '4':print_list}

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
	linearray = line.split(":")
	username = linearray[0]
	password = linearray[1]
	hash[username] = password
	
# outer loop until user quits
while(choice != '5'):
	#inner loop until user enters correct option
	while(1):
	# print menu & prompt for user input: $choice
		print ("""
		User Accounts
		---------------------------
		1) Add user account
		2) Edit existing account
		3) Delete user account
		4) Print list of user accounts
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
		my_string = key + ":" + value
		fh.write(my_string)
	fh.close()
	

