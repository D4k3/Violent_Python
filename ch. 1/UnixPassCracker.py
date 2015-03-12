#
# Violent Python Chapter #1
# A simple Unix sha512 password decrypter
# By: Daniyar Kassenov
#


#!/usr/bin/python

import crypt

def PassTest(cryptPass):
	presalt = cryptPass.split('$')[2]
	#adding $6$ to salt string allows crypt() to use sha512 algorithm
	salt = "$6$" + presalt
	dictFile = open('dictionary.txt', 'r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		if crypt.crypt(word, salt) == cryptPass:
			print "Found Password: " + word
			return
	print "Password Not Found.\n"
	return

def main():
	PassFile = open('passwords.txt', 'r')
	for line in PassFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "Cracking the Password for: " + str(user)
			PassTest(cryptPass)

if __name__ == "__main__":
	main() 