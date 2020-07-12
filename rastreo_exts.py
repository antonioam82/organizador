#-*-coding: utf-8-*-
import os
from VALID import ns
print("Directorio actual: ",os.getcwd())

def AB():
	while True:
		op = input("Introduje aquí su opción:")
		if op == "A" or op == "B":
			return op
			break
		else:
			print("Introduce A o B según su opción.")
			
def change_dir():
	while True:
		dire = input("Introduzca un directorio valido: ")
		if os.path.isdir(dire):
			os.chdir(dire)
			break

while True:
	print("\nELIJA OPCIÓN")
	print("A) BUSCAR ARCHIVOS POR EXTENSIÓN")
	print("B) BUSCAR UN ARCHIVO")
	opc = AB()
	
	if opc == 'A':
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
					
	elif opc == "B":
		finded = False
		dir_base = input("Introduce directorio base: ")
		fichero_requerido = input("Inroduce archivo a buscar: ")
		
		for root, folders, files in os.walk(dir_base):
			for file in files:
				if file == fichero_requerido:
					finded = True
					print('Encontrado '+file+' en '+os.path.join(root, file))
					break
		if finded == False:
			print("No se encontró el archivo",fichero_requerido)
					
	conti = ns(input("¿Continuar(n/s)?: "))
	if conti == "n":
		break
