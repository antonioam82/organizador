#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        dire = input("Introduzca directorio base: ")
        if os.path.isdir(dire):
            os.chdir(dire)
            break
        else:
            print("ERROR, DIRECTORIO NO VÁLIDO")
	
print("\n-----------------------------FILE FINDER------------------------------\n")		

while True:
    count = 0
    print("Directorio actual: {}: ".format(os.getcwd()))
    print("\n**********ELIJA OPCIÓN**********")
    print("A) BUSCAR ARCHIVOS POR EXTENSIÓN")
    print("B) BUSCAR UN ARCHIVO")
    print("********************************\n")
    opc = AB()
	
    if opc == 'A':
        change_dir()
        filetype = input("Introduce extension: ")
        mostrar = ns(input("¿Mostrar ubicación de los archivos?(n/s): "))
        print("BUSCANDO...\n")
        for nombredir, dirs, ficheros in os.walk(os.getcwd()):
            for nombrefichero in ficheros:
                if nombrefichero.endswith(filetype):
                    count+=1
                    if mostrar == "s":
                        print('{}-'.format(count)+os.path.join(nombredir,nombrefichero))
                    else:
                        print('{}-'.format(count)+os.path.abspath(nombrefichero))
                    
        print('\n{} ARCHIVOS ENCONTRADOS.'.format(count))
					
    elif opc == "B":
        finded = False
        change_dir()
        dir_base = os.getcwd()
        fichero_requerido = input("Introduce archivo a buscar o término de busqueda: ")
        print("BUSCANDO...\n")
        for root, folders, files in os.walk(dir_base):
            for file in files:
                if fichero_requerido in file: #file == fichero_requerido
                    count+=1
                    finded = True
                    #print('{}-Encontrado '.format(count)+file+' en '+os.path.join(root,file)+"\n")
                    print('{}-Encontrado '.format(count)+file+' en '+os.path.join(root)+"\n")
                    #print('{}-Encontrado '.format(count)+'archivo'+' en '+os.path.join(root,file)+"\n")
            
        if finded == False:
            print("No se encontró el archivo",fichero_requerido)
        else:
            print("\n{} ARCHIVOS ENCONTRADOS.".format(count))
            
    conti = ns(input("¿Continuar(n/s)?: "))
    if conti == "n":
        break


