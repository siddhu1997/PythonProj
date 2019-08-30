import sys

legend = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}


def additive():
	print("Additive Cipher:")
	key = int(input("Enter KEY: "))
	print("\n"+str)
	for i in range(0,len(str)):
		if str[i] == " ":
			print(str[i], end="")
		else:	
			i = (i+key)%26
			print(legend[i], end="")
	print("\n")

def multiply():
	print("Multiplicative Cipher:")
	key = int(input("Enter KEY: "))
	print("\n"+str)
	for i in range(0,len(str)):
		if str[i] == " ":
			print(str[i], end="")
		else:	
			i = (i*key)%26
			print(legend[i], end="")
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
	additive()
	multiply()
	affine()
	vignere()

