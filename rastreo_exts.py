import os
from VALID import ns

while True:
	filetype = raw_input("Inroduce extension: ")
	count = 0
	for (nombredir, dirs, ficheros) in os.walk('.'):
	    for nombrefichero in ficheros:
			if nombrefichero.endswith(filetype):
				print(nombrefichero)
				count = count+1
	print("")
	print (count, 'archivos encontrados')
	conti = ns(input("\n¿Desea continuar?(n/s): ")
	if conti == ("n"):
		break
