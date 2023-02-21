import argparse

def generate_fibonacci(n):
	'''
	Used to generate fibonacci series
	INPUT - Length of series
	The 'fib' list declared globally stores the final series generated
	'''
	if n < 0:
		print("Please enter a valid password. Password length should be greater than 2 characters")
		exit()
	elif n <= len(fib):
		return fib[n-1]
	else:
		temp = generate_fibonacci(n-1) + generate_fibonacci(n-2)
		fib.append(temp)
		return temp

def encrypt():
	'''
	Encrypts the text.
	Returns the encrypted string.
	'''
	new_words = []
	for w in words:
		#Reversing the word
		temp = w[::-1]
		#Appending password to the word
		temp += password
		for x in range(len(fib)):
			offset = fib[x]
			new_temp = ""
			for i in range(len(temp)):
				#if index is odd, the character is forwarded by 'offset'. Modulus by 129 to maintain ASCII range
				if i % 2 == 1:
					new_temp += chr(((ord(temp[i]) + offset) % 129))
				#if index is even, the character is reversed by 'offset'. Modulus by 129 to maintain ASCII range
				else:
					new_temp += chr(((ord(temp[i]) - offset + 129) % 129))
			#Update the resultant cipher word
			temp = new_temp
		#add the final cipher text of the word to 'new_words'
		new_words.append(temp)
	return " ".join(new_words)

def decrypt():
	'''
	Decrypts the encrypted text. 
	Returns the decrypted string.
	'''
	new_words = []
	for w in words:
		temp = w
		for x in range(len(fib)):
			offset = fib[x]
			new_temp = ""
			for i in range(len(temp)):
				#if index is odd, the character is reversed by 'offset'. Modulus by 129 to maintain ASCII range
				if i % 2 == 1:
					new_temp += chr(((ord(temp[i]) - offset + 129) % 129))
				#if index is even, the character is forwarded by 'offset'. Modulus by 129 to maintain ASCII range
				else:
					new_temp += chr(((ord(temp[i]) + offset) % 129))
			#Update the resultant cipher word
			temp = new_temp
		#Validate password
		if temp[-1*len(password):] != password:
			print("Incorrect Password")
			exit()
		else:
			#Remove the password string from end
			temp = temp[:-1*len(password)]
			#Reverse the resultant cipher to get original text and add to 'new_words'
			new_words.append(temp[::-1])
	return " ".join(new_words)
	
#Parsing command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--method", required=True, help="'e' - for Encryption, 'd' - for Decryption")
ap.add_argument("-i", "--input", required=True, help="Path to input file")
ap.add_argument("-o", "--output", required=True, help="Path to output file")
ap.add_argument("-p", "--password", required=True, help="Password for Encryption/Decryption")
args = vars(ap.parse_args())

#Validating the arguments received
if args["method"] != 'e' and args["method"] != 'd':
	print("Invalid Option. Please refer help [-h] for more details.")
	print("Use:", "python encrypt.py -h")
	exit()

#Opening input file that contains text to be encrypted
ip = open(args["input"], "r")
if ip == None:
	print("Unable to open file")
	exit()
#Reading Data from file
data = ip.read()
ip.close()
#Opening output file to write the output
op = open(args["output"], "w")
password = args["password"]
#Splitting the strings based on " " delimiter
words = data.split()

#Generating fibonacci series equal to length of the password string
fib = [1, 1]
generate_fibonacci(len(password))

#Encrypting/ Decrypting the file
if args["method"] == 'e':
	res = encrypt()
elif args["method"] == 'd':
	res = decrypt()
op.write(res)

'''
ALGORITHM USED -

ENCRYPTION 
- Generate fibonacci series equal to length of password.
- For each word in the text	
	- Reverse the word.
	- Add password to end.
	- For each value in fibonacci series
		- For each character is word
			- if index is even, the character is reversed by 'value'. Ex - value - 3, character - 'b', then cipher - 'z'
			- if index is odd, the character is forwarded by 'value'. Ex - value - 3, character - 'b', then cipher - 'e'
		- Update word.
	
DECRYPTION
- Generate fibonacci series equal to length of password.
- For each word in the text	
	- For each value in fibonacci series
		- For each character is word
			- if index is odd, the character is reversed by 'value'. Ex - value - 3, character - 'b', then cipher - 'z'
			- if index is even, the character is forwarded by 'value'. Ex - value - 3, character - 'b', then cipher - 'e'
		- Update word.
	- Validate Password by checking end of word.
		- If password is correct,
			- Remove the password from end.
			- Reverse the word.
		- Else, exit
'''