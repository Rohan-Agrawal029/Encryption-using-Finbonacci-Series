An implementation of an encryption technique using Fibonacci Series for file encryption over the entire ASCII range of characters.

It accepts the following command line arguments -
1) Method: Denotes the program mode - Encryption (e) or Decryption (d).
Usage: >> python Fibonacci-Encrpytion.py --method e 
       >> python Fibonacci-Encrpytion.py -m e
       >> python Fibonacci-Encrpytion.py --method d
       >> python Fibonacci-Encrpytion.py -m d
2) Input File Path: Denotes the path to file to be encrpyted.
Usage: >> python Fibonacci-Encrpytion.py --input encryptMe.txt 
       >> python Fibonacci-Encrpytion.py -i encryptMe.txt
3) Output File Path: Denotes the path to output file that will hold the encrypted text.
Usage: >> python Fibonacci-Encrpytion.py --output encryptedText.txt 
       >> python Fibonacci-Encrpytion.py -o encryptedText.txt
4) Password: Encryption key/password required to encrypt or decrypt the file.
Usage: >> python Fibonacci-Encrpytion.py --password MyP@ssword123456 
       >> python Fibonacci-Encrpytion.py -p MyP@ssword123456 


ALGORITHM USED -

ENCRYPTION:

- Generate fibonacci series equal to length of password.
- For each word in the text	
	- Reverse the word.
	- Add password to end.
	- For each value in fibonacci series
		- For each character is word
			- if index is even, the character is reversed by 'value'. Ex - value - 3, character - 'b', then cipher - 'z'
			- if index is odd, the character is forwarded by 'value'. Ex - value - 3, character - 'b', then cipher - 'e'
		- Update word.
	
DECRYPTION:

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