#-*-coding: utf-8-*-
import os
from VALID import ns

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
    count = 0
    print("Directorio actual: ",os.getcwd())
    print("\n**********ELIJA OPCIÓN**********")
    print("A) BUSCAR ARCHIVOS POR EXTENSIÓN")
    print("B) BUSCAR UN ARCHIVO")
    print("********************************\n")
    opc = AB()
	
    if opc == 'A':
	change_dir()
	filetype = input("Inroduce extension: ")
	print("BUSCANDO...")
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
	    if os.path.isdir(dir_base):
	        fichero_requerido = input("Inroduce archivo a buscar: ")
		print("BUSCANDO...\n")
		for root, folders, files in os.walk(dir_base):
		    for file in files:
		        if file == fichero_requerido or fichero_requerido in file:
			    count+=1
			    finded = True
			    print('Encontrado '+file+' en '+os.path.join(root, file))
			    break
		if finded == False:
		    print("No se encontró el archivo",fichero_requerido)
		else:
	            print("\nARCHIVO O TERMINO ENCONTRADO {} VECES".format(count))
	    else:
		print("Directorio base no válido.")
					
	conti = ns(input("¿Continuar(n/s)?: "))
	if conti == "n":
	    break
