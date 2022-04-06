# Caesar Brute Force Cracker

MAX_KEY_SIZE = 26

def getMessage():
	print ('Enter the encrypted text:')
	return input()

def decryptMessage(message, key):
	translated = ''
	
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += -key
			
			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			
			translated += chr(num)
		else:
			translated += symbol
	return translated

message = getMessage()

print ('Translation options:')
print ()

for key in range (1, MAX_KEY_SIZE +1):
	print (key, decryptMessage(message, key))
	print ()

input()



