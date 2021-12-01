from pprint import pprint

# some functions ::
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def get_authtoken():
	# Reading the file credentials.txt
	file1 = open("credentials.txt","r+") 

	# Getting only the authtoken from the file
	string = file1.readlines()[0]

	# Finding the occurences
	pos = findOccurrences(string, '"')

	# Closing the file
	file1.close()


	return string[pos[0]:pos[1]+1]



