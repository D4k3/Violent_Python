#!/usr/bin/python

import crypt

def PassTest(cryptPass, salt):
	#salt = cryptPass[:2]
	print salt
	print cryptPass
	dictFile = open('dictionary.txt', 'r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if cryptWord == cryptPass:
			print "Found Password: "+ word
			return
	print "Password Not Found.\n"
	return

def main():
	PassFile = open('passwords.txt', 'r')
	for line in PassFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split('$')[3].strip(' ')
			salt = line.split('$')[2]
			print "Cracking the Password for: " + str(user)
			PassTest(cryptPass, salt)

if __name__ == "__main__":
	main() 