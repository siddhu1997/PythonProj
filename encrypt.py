import sys

def additive():
	print("Additive Cipher:")
	key = int(input("Enter KEY: "))
	print("\n"+str)
	for i in str.lower():
		if i == " ":
			print(i, end="")
		else:	
			n = (ord(i)-ord("a"))
			n = n+key
			n = chr((n%26)+65)
			print(n.upper(),end="")
	print("\n")

def multiply():
	print("Multiplicative Cipher:")
	key = int(input("Enter KEY: "))
	print("\n"+str)
	for i in str.lower():
		if i == " ":
			print(i, end="")
		else:	
			n = (ord(i)-ord("a"))
			n = n*key
			n = chr((n%26)+65)
			print(n.upper(),end="")
	print("\n")

def affine():
	print("Affine Cipher: ")
	key1 = int(input("Enter KEY 1:"))
	key2 = int(input("Enter KEY 2:"))
	print("\n"+str)
	for k in str.lower():
		if k==' ':
			print(" ",end="")
		else:
			n = (ord(k)-ord("a"))
			n = n*key1
			n = n+key2
			n = chr((n%26)+65)
			print(n.upper(),end="")
	print("\n")

def vignere():
	print("Vignere Cipher: ")
	str = input("Enter Plain Text")
	key = input("Enter KEY: ")
	i=0
	print("\n"+str)
	for k in str.lower():
		if k==' ':
			print(" ",end="")
		else:
			n = (ord(k)-ord("a"))+(ord(key[i].lower())-ord("a"))
			n = chr((n%26)+65)
			print(n.upper(),end="")
			i=(i+1)%(len(key))
	print("\n")


if __name__ == "__main__":
	str = sys.argv[1]
	option = int(input("\nMENU:\nResults for 1.Additive\t2.Multiplicative\t3.Affine\nResult for 1.Vignere\nEnter your choice (1 for first group | 2 for second group):   "))
	if option == 1:
		additive()
		multiply()
		affine()
	elif option == 2:
		vignere()
	else:
		print("Invalid Option! Exiting Program")
