import os
from VALID import ns
#print(os.getcwd())
while True:
	filetype = input("Inroduce extension: ")
	count = 0
	for (nombredir, dirs, ficheros) in os.walk('.'):
	    for nombrefichero in ficheros:
			if nombrefichero.endswith(filetype):
				print(os.path.abspath(nombrefichero))
				count = count+1
	print("")
	print (count, 'archivos encontrados')
	conti = ns(input("¿Desea continuar(n/s)?: ")
	if conti == ("n"):
		break
