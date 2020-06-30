import os
from VALID import ns

def change_dir():
	while True:
		dire = input("Seleccione un directorio valido: ")
		if os.path.isdir(dire):
			os.chdir(dire)
			break

while True:
	print(os.getcwd())
	change_dir()
	filetype = input("Inroduce extension: ")
	count = 0
	for (nombredir, dirs, ficheros) in os.walk('.'):
	    for nombrefichero in ficheros:
			if nombrefichero.endswith(filetype):
				print(os.path.abspath(nombrefichero))
				count = count+1
	print("")
	print (count, 'archivos encontrados')
	
	conti = ns(input("\n¿Continuar?(n/s): "))
	if conti == "n":
		break
