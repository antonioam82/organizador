import os
from VALID import ns

filetype = input("Inroduce extension: ")

count = 0

for (nombredir, dirs, ficheros) in os.walk('.'):
	for nombrefichero in ficheros:
		if nombrefichero.endswith(filetype):
			print(nombrefichero)
			count = count+1
			
print("")			
print (count, 'archivos encontrados')
			
