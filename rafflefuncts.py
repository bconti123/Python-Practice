import re

#Function to reverse a string

def reverse(s):
	if s == "":
		return s
	else:
		return reverse(s[1:])

############################ add_user function ###############################


def add_user(local_hash):

	# prompt for username & password
	username = input("Enter username: ")
	# strip off special chars from username (ref asmt sheet)
	username = re.sub(r'\W+', '', username)
	# convert username to lowercase (ref asmt sheet)
	username = username.lower()
	#check if username already exists & if so exit, else assign password as value to the hash referenced by username as the key
	if(username in local_hash):
		print("Username already exist!")
		return local_hash
	return local_hash

############################ delete_user function ###############################


def del_user(local_hash):

	# prompt/chomp for username
	username = input("Enter username to delete: ")
	# strip off special chars from username (ref asmt sheet)
	username = re.sub(r'\W+', '', username)
	# convert username to lowercase (ref asmt sheet)
	username = username.lower()
	#check if username DOESNT already exists & if NOT so exit
	if username not in local_hash:
		print("Username does not exist!")
		return local_hash
	#delete key from hash (ref slides)
	del local_hash[username]
	return local_hash

############################ print_list function ###############################


def print_list(local_hash):

	# print out to the screen each key & value pair from hash
	print(local_hash)
	return local_hash


def start_raffle(local_hash):
    
    # print out to the screen who is winner
    name = random.choice(username in local_hash)
    print(random.choice(word))
