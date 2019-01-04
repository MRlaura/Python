
valor= input("Write a number...")
print (type(valor))
print (valor)
valor = int(valor)
print (type(valor))

try:
	valor= input("Write a number ")
	valor = int(valor)
	
except:
	print ("That is not a number")
else:
    print (valor)	